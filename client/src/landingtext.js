// import React from 'react';

// const LandingText = () => {
//   const headingStyle = {
//     color: '#FFFFFF',
//     fontSize: '1.5em',
//     fontWeight: 800,
//     height: '35.5vh',
//     letterSpacing: '2%',
//     padding: '10%',
//     backgroundImage: 'url(https://images.unsplash.com/photo-1562925246-25f01be5471c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Ymx1ZSUyMGhvdXNlfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60)',
//   };

//   const blueBackgroundStyle = {
//     background: 'rgba(0, 120, 215, 0.2)',
    
//   };

//   return (
//     <h1 style={headingStyle}>
//       <div style={blueBackgroundStyle}>
//         <h1>CHATEAU PROPERTIES</h1>
//         <h1>AFFORDABLE&AMAZING PROPERTY</h1>
//       </div>
//       <div className="button-container">
//         <button className="center-button">CATALOGUE</button>
//       </div>
//     </h1>
//   );
// };

// export default LandingText;

// import React, { useContext } from 'react';
// import { Link } from 'react-router-dom';

// const LandingText = () => {
//   const headingStyle = {
//     color: '#FFFFFF',
//     fontSize: '1.5em',
//     fontWeight: 800,
//     height: '35.5vh',
//     letterSpacing: '2%',
//     padding: '10%',
//   };

//   const blueBackgroundStyle = {
//     background: 'rgba(0, 120, 215, 0.2)',
//   };

//   return (
//     <div>
//       <h1 style={headingStyle}>
//         <div style={blueBackgroundStyle}>
//           <h1>CHATEAU PROPERTIES</h1>
//           <h1>AFFORDABLE & AMAZING PROPERTY</h1>
//         </div>
//         <div className="button-container">
//           <Link to="/catalogue" className="center-button">
//             CATALOGUE
//           </Link>
//         </div>
//       </h1>
//     </div>
//   );
// };

// export default LandingText;

import React from 'react';

const LandingText = () => {
  const headingStyle = {
    color: '#FFFFFF',
    fontSize: '1.5em',
    fontWeight: 800,
    height: '35.5vh',
    letterSpacing: '2%',
    padding: '10%',
    backgroundImage: 'url(https://images.unsplash.com/photo-1562925246-25f01be5471c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Ymx1ZSUyMGhvdXNlfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60)',
    
  };

  const blueBackgroundStyle = {
    background: 'rgba(0, 120, 215, 0.2)',
    
  };

  return (
    <h1 style={headingStyle}>
      <div style={blueBackgroundStyle}>
        <h1>CHATEAU PROPERTIES</h1>
        <h1>AFFORDABLE&AMAZING PROPERTY</h1>
      </div>
      <div className="button-container">
        <button className="center-button">CATALOGUE</button>
      </div>
    </h1>
  );
};

export default LandingText;
