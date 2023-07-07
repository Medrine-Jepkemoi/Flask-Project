import React, { useState } from 'react';
import { loginUser } from './api';

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    let user = new FormData();
    user.append("email", email);
    user.append("password", password);
    try {
      const data = await loginUser(user);
      console.log(data); // Handle successful login
      // Reset the form
      setEmail("");
      setPassword("");
      setError("");
    } catch (error) {
      setError(error.error); // Display the login error
    }
  };

  return (
    <div>
      {error && <p>{error}</p>}
      <form onSubmit={handleLogin}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={handleEmailChange}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

