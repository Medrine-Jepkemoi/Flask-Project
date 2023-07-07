import React from 'react';

const LandingText = () => {
  const headingStyle = {
    color: '#FFFFFF',
    fontSize: '1.5em',
    fontWeight: 800,
    height: '35.5vh',
    letterSpacing: '2%',
    padding: '10%',
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

// import React from 'react';
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
//     <div style={headingStyle}>
//       <div style={blueBackgroundStyle}>
//         <h1>CHATEAU PROPERTIES</h1>
//         <h1>AFFORDABLE & AMAZING PROPERTY</h1>
//       </div>
//       <div className="button-container">
//         <Link className="center-button">CATALOGUE</Link>
//       </div>
//     </div>
//   );
// };

// export default LandingText;

