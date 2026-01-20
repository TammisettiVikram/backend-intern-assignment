import React, { useEffect, useState } from "react";
import API from "./api";

export default function Dashboard({ setPage }) {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");
    const [editingId, setEditingId] = useState(null);
    const [msg, setMsg] = useState("");

    const loadTasks = async () => {
    const res = await API.get("/tasks");
    setTasks(res.data);
    };

    const createOrUpdateTask = async () => {
    try {
        if (editingId) {
            await API.put(`/tasks/${editingId}`, {
            title,
            description: desc,
        });
        setMsg("Task updated successfully");
        } else {
        await API.post("/tasks", { title, description: desc });
        setMsg("Task created successfully");
    }

        setTitle("");
        setDesc("");
        setEditingId(null);
        loadTasks();
    } catch {
        setMsg("Operation failed");
    }
};

    const editTask = (task) => {
    setTitle(task.title);
    setDesc(task.description || "");
    setEditingId(task.id);
};

    const deleteTask = async (id) => {
    await API.delete(`/tasks/${id}`);
    setMsg("Task deleted successfully");
    loadTasks();
};

    const logout = () => {
    localStorage.removeItem("token");
    setPage("login");
};

    useEffect(() => {
    loadTasks();
}, []);

    return (
    <>
        <h3>Dashboard</h3>

        <input
        placeholder="Task title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        />

        <input
        placeholder="Description"
        value={desc}
        onChange={(e) => setDesc(e.target.value)}
        />

        <button onClick={createOrUpdateTask}>
        {editingId ? "Update Task" : "Create Task"}
        </button>

        {msg && <p className="success">{msg}</p>}

        <h4>Your Tasks</h4>

        {tasks.map((t) => (
        <div className="task" key={t.id}>
            <strong>{t.title}</strong>
            <p>{t.description}</p>

            <button onClick={() => editTask(t)}>Edit</button>

            <button
            style={{ background: "#e74c3c", marginTop: "5px" }}
            onClick={() => deleteTask(t.id)}
            >
            Delete
            </button>
        </div>
    ))}

        <button onClick={logout}>Logout</button>
    </>
);
}
