import React, { useState } from "react";
import API from "./api";

export default function Register({ setPage }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [msg, setMsg] = useState("");

    const register = async () => {
    try {
        await API.post("/auth/register", { email, password });
        setMsg("Registered successfully");
        setPage("login");
    } catch (err) {
        setMsg(err.response?.data?.detail || "Registration failed");
    }
};

    return (
    <>
        <h3>Register</h3>
        <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
        <br />
        <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
        <br />
        <button onClick={register}>Register</button>
        <p>{msg}</p>
        <button onClick={() => setPage("login")}>Go to Login</button>
    </>
    );
}
