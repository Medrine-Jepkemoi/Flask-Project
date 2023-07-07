// import React, { useState } from 'react';

// function SignupForm() {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     // Create an object with the form data
//     const formData = {
//       email,
//       password,
//     };

//     try {
//       // Send a POST request to your Flask server
//       const response = await fetch('/user/signup', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(formData),
//       });

//       if (response.ok) {
//         // User sign-up successful
//         // Redirect to another page or show a success message
//       } else {
//         // Handle error response from the server
//         const errorData = await response.json();
//         console.log('Sign-up error:', errorData.error);
//       }
//     } catch (error) {
//       console.log('Error:', error.message);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <div>
//         <label>Email:</label>
//         <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
//       </div>
//       <div>
//         <label>Password:</label>
//         <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
//       </div>
//       <button type="submit">Sign Up</button>
//     </form>
//   );
// }

// export default SignupForm;

import { useFormik } from 'formik';
import * as Yup from 'yup';
import React, { useEffect } from 'react';

function SignUp() {
  const formSchema = Yup.object().shape({
    email: Yup.string().required('Email must be entered').email('Invalid email'),
    password: Yup.string().required('Must enter password').min(8).max(15),
  });

  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch('http://localhost:5555/user/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          if (response.ok) {
            alert('YOU HAVE SUCCESSFULLY JOINED INSTATOK');
          } else {
            alert('SORRY, IT APPEARS THERE WAS A PROBLEM. PLEASE TRY AGAIN LATER');
          }
        })
        .catch((error) => {
          console.log('Error:', error.message);
        });
    },
  });

  useEffect(() => {
    fetch('http://localhost:5555/user/signup')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log('Error:', error.message);
      });
  }, []);

  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="email">Enter email</label>
      <input
        type="text"
        onChange={formik.handleChange}
        value={formik.values.email}
        name="email"
      />
      {formik.errors.email && formik.touched.email && <p>{formik.errors.email}</p>}

      <label htmlFor="password">Enter password</label>
      <input
        type="text"
        onChange={formik.handleChange}
        value={formik.values.password}
        name="password"
      />
      {formik.errors.password && formik.touched.password && <p>{formik.errors.password}</p>}

      <input type="submit" value="Register" />
    </form>
  );
}

export default SignUp;
