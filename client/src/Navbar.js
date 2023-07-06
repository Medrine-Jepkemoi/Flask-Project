import React from 'react';

const Navbar = () => {
  return (
    <nav style={{ background: 'linear-gradient(to bottom, black, transparent)' }}>
      <ul style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', listStyle: 'none', padding: '1%', border: '1px solid white' }}>
        <li>
          <img src="data:image/png;base64,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" alt="Logo" />
        </li>
        <li style={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
          <a href="#" style={{ textDecoration: 'none', fontWeight: 'bold', fontSize: '32px', color: 'white' }}>PURCHASE OR RENT</a>
        </li>
        {/* <li style={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
          <a href="#" style={{ textDecoration: 'none', fontWeight: 'bold', fontSize: '32px', color: 'white' }}>Rent</a>
        </li> */}
        <li style={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
          <a href="#" style={{ textDecoration: 'none', fontWeight: 'bold', fontSize: '32px', color: 'white' }}>ABOUT US</a>
        </li>
        {/* <li>
          <input type="text" placeholder="Search" style={{ color: 'white' }} />
        </li> */}
        <li style={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
          <a href="#" style={{ textDecoration: 'none', fontWeight: 'bold', fontSize: '32px', color: 'white', padding: '5px 30px' }}>LOG OUT</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;