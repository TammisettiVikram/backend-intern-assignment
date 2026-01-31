import jwtDecode from "jwt-decode";
import { Routes, Route, useNavigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import AdminDashboard from "./pages/AdminDashboard"; // make sure this exists

const token = localStorage.getItem("token");
const user = token ? jwtDecode(token) : null;
const isAdmin = user?.role === "admin";

export default function App() {
    const navigate = useNavigate();

    return (
        <div>
            {/* Conditionally render Admin Panel button */}
            {isAdmin && (
                <button
                    onClick={() => navigate("/admin")}
                    className="bg-black text-white px-4 py-2 rounded"
                >
                    Admin Panel
                </button>
            )}

            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/dashboard" element={<Dashboard />} />
                {isAdmin && <Route path="/admin" element={<AdminDashboard />} />}
            </Routes>
        </div>
    );
}
