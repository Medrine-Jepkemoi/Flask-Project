// import React, { useState } from 'react';
// import { loginUser } from './api';

// const LoginForm = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState('');

//   const handleEmailChange = (e) => {
//     setEmail(e.target.value);
//   };

//   const handlePasswordChange = (e) => {
//     setPassword(e.target.value);
//   };

//   const handleLogin = async (e) => {
//     e.preventDefault();

//     try {
//       const data = await loginUser(email, password);
//       console.log(data); // Handle successful login
//       // Reset the form
//       setEmail('');
//       setPassword('');
//       setError('');
//     } catch (error) {
//       setError(error.error); // Display the login error
//     }
//   };

//   return (
//     <div>
      
//       {error && <p>{error}</p>}
//       <form onSubmit={handleLogin}>
//         <div>
//           <label>Email:</label>
//           <input type="email" value={email} onChange={handleEmailChange} required />
//         </div>
//         <div>
//           <label>Password:</label>
//           <input type="password" value={password} onChange={handlePasswordChange} required />
//         </div>
//         <button type="submit">Login</button>
//       </form>
//     </div>
//   );
// };

// export default LoginForm;

// import React, { useState } from 'react';
// import { loginUser } from './api';

// const LoginForm = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState('');
//   const [loggedIn, setLoggedIn] = useState(false); // New state variable
//   const [username, setUsername] = useState(''); // New state variable

//   const handleEmailChange = (e) => {
//     setEmail(e.target.value);
//   };

//   const handlePasswordChange = (e) => {
//     setPassword(e.target.value);
//   };

//   const handleLogin = async (e) => {
//     e.preventDefault();

//     try {
//       if (email === 'bkk@gmail.com' && password === 'password') {
//         // Successful login
//         setLoggedIn(true);
//         setUsername(email);
//         setError('');
//       } else {
//         throw new Error('Invalid email or password');
//       }
//     } catch (error) {
//       setError(error.message); // Display the login error
//     }
//   };

//   return (
//     <div>
//       {error && <p>{error}</p>}
//       {loggedIn && <p>Logged in as: {username}</p>}
//       <form onSubmit={handleLogin}>
//         <div>
//           <label>Email:</label>
//           <input type="email" value={email} onChange={handleEmailChange} required />
//         </div>
//         <div>
//           <label>Password:</label>
//           <input type="password" value={password} onChange={handlePasswordChange} required />
//         </div>
//         <button type="submit">Login</button>
//       </form>
//     </div>
//   );
// };

// export default LoginForm;


// import React, { useState } from 'react';
// import { loginUser } from './api';

// const LoginForm = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState('');
//   const [loggedIn, setLoggedIn] = useState(false); // New state variable
//   const [username, setUsername] = useState(''); // New state variable

//   const handleEmailChange = (e) => {
//     setEmail(e.target.value);
//   };

//   const handlePasswordChange = (e) => {
//     setPassword(e.target.value);
//   };

//   const handleLogin = async (e) => {
//     e.preventDefault();

//     try {
//       const allowedEmails = ['bkk@gmail.com', 'medrine@gmail.com', 'ronald@gmail.com', 'bethwel@gmail.com', 'lewis@gmail.com', 'test@gmail.com','brianngeno@gmail.com'];
      
//       if (allowedEmails.includes(email)) {
//         // Successful login
//         setLoggedIn(true);
//         setUsername(email);
//         setError('');
//       } else {
//         throw new Error('Invalid email');
//       }
//     } catch (error) {
//       setError(error.message); // Display the login error
//     }
//   };

//   return (
//     <div>
//       {error && <p>{error}</p>}
//       {loggedIn && <p>Logged in as: {username}</p>}
//       <form onSubmit={handleLogin}>
//         <div>
//           <label>Email:</label>
//           <input type="email" value={email} onChange={handleEmailChange} required />
//         </div>
//         <div>
//           <label>Password:</label>
//           <input type="password" value={password} onChange={handlePasswordChange} required />
//         </div>
//         <button type="submit">Login</button>
//       </form>
//     </div>
//   );
// };

// export default LoginForm;


// import React, { useState } from 'react';
// import { loginUser } from './api';

// const LoginForm = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState('');
//   const [loggedIn, setLoggedIn] = useState(false); // New state variable
//   const [username, setUsername] = useState(''); // New state variable

//   const handleEmailChange = (e) => {
//     setEmail(e.target.value);
//   };

//   const handlePasswordChange = (e) => {
//     setPassword(e.target.value);
//   };

//   const handleLogin = async (e) => {
//     e.preventDefault();

//     try {
//       const allowedEmails = ['bkk@gmail.com', 'medrine@gmail.com', 'ronald@gmail.com', 'bethwel@gmail.com', 'lewis@gmail.com', 'test@gmail.com','brianngeno@gmail.com'];
      
//       if (allowedEmails.includes(email)) {
//         // Successful login
//         setLoggedIn(true);
//         setUsername(email);
//         setError('');
//       } else {
//         throw new Error('Invalid email');
//       }
//     } catch (error) {
//       setError(error.message); // Display the login error
//     }
//   };

//   return (
//     <div style={{ height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center',color:'white' }}>
//       <div>
//         {error && <p>{error}</p>}
//         {loggedIn && <p>Logged in as: {username}</p>}
//         <form onSubmit={handleLogin} style={{ textAlign: 'center', marginTop: '2rem' }}>
//           <div style={{ marginBottom: '1rem' }}>
//             <label style={{ fontWeight: 'bold', display: 'block', marginBottom: '0.5rem' }}>Email:</label>
//             <input type="email" value={email} onChange={handleEmailChange} required />
//           </div>
//           <div style={{ marginBottom: '1rem' }}>
//             <label style={{ fontWeight: 'bold', display: 'block', marginBottom: '0.5rem',color:'white' }}>Password:</label>
//             <input type="password" value={password} onChange={handlePasswordChange} required />
//           </div>
//           <button type="submit" style={{ fontSize: '1.5rem', padding: '0.5rem 1rem' }}>Login</button>
//         </form>
//       </div>
//     </div>
//   );
// };

// export default LoginForm;

import React, { useState } from 'react';
import { loginUser } from './api';
import { login } from './login'; // Import the login function

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loggedIn, setLoggedIn] = useState(false); // New state variable
  const [username, setUsername] = useState(''); // New state variable

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Call the login function from login.js
      login(email, password);
      setLoggedIn(true);
      setUsername(email);
      setError('');
    } catch (error) {
      setError(error.message); // Display the login error
    }
  };

  return (
    <div style={{ height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div>
        {/* {error && <p>{error}</p>} */}
        {loggedIn && <p>Logged in as: {username}</p>}
        <form onSubmit={handleLogin} style={{ textAlign: 'center', marginTop: '2rem' }}>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ fontSize: '1.5em',fontWeight: 800, display: 'block', marginBottom: '0.5rem',color:'white' }}>Email:</label>
            <input type="email" value={email} onChange={handleEmailChange} required />
          </div>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{fontSize: '1.5em',fontWeight: 800, display: 'block', marginBottom: '0.5rem',color:'white'  }}>Password:</label>
            <input type="password" value={password} onChange={handlePasswordChange} required />
          </div>
          <button type="submit" style={{ fontSize: '1.5rem', padding: '0.5rem 1rem' }}>Login</button>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
