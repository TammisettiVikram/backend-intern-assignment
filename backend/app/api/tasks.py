from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.task import TaskUpdate
from fastapi import HTTPException
from typing import List
from app.db.deps import get_db, get_current_user
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskOut

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(
    task_in: TaskCreate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    new_task = Task(
        title=task_in.title,
        description=task_in.description,
        owner_id=current_user["id"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=List[TaskOut])
def read_tasks(
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    # Only returns tasks belonging to the logged-in user
    return db.query(Task).filter(Task.owner_id == current_user["id"]).all()

@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # 1. Find the task and verify ownership (Security Practice)
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user["id"]).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found or you are not the owner"
        )

    # 2. Update the fields
    task.title = task_in.title
    task.description = task_in.description

    # 3. Commit to PostgreSQL
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user["id"]).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return None