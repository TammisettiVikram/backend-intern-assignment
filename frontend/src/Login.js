import React, { useState } from "react";
import API from "./api";

export default function Login({ setPage }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [msg, setMsg] = useState("");

    const login = async () => {
    try {
        const res = await API.post("/auth/login", { email, password });
        localStorage.setItem("token", res.data.access_token);
        setPage("dashboard");
    } catch {
        setMsg("Invalid credentials");
    }
};

    return (
    <>
        <h3>Login</h3>
        <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
        <br />
        <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
        <br />
        <button onClick={login}>Login</button>
        <p>{msg}</p>
        <button onClick={() => setPage("register")}>Register</button>
    </>
    );
}
