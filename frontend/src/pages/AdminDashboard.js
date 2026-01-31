import { useEffect, useState } from "react";
import api from "../api";

export default function AdminDashboard() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        api.get("/users")
            .then(res => setUsers(res.data))
            .catch(() => alert("Access denied"));
    }, []);

    return (
        <div className="min-h-screen p-6 bg-gray-100">
            <div className="max-w-5xl mx-auto bg-white rounded-xl p-6 shadow">
                <h1 className="text-3xl font-bold mb-6">Admin Dashboard</h1>

                <table className="w-full border">
                    <thead className="bg-gray-200">
                        <tr>
                            <th className="p-2">ID</th>
                            <th className="p-2">Email</th>
                            <th className="p-2">Role</th>
                        </tr>
                    </thead>
                    <tbody>
                        {users.map(u => (
                            <tr key={u.id} className="border-t">
                                <td className="p-2">{u.id}</td>
                                <td className="p-2">{u.email}</td>
                                <td className="p-2 font-semibold">{u.role}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
