import React from 'react';

const CardComponent = () => {
  const cardContainerStyle = {
    display: 'flex',
    height: '60vh',
    justifyContent: 'space-between',
  };

  const cardStyle = {
    flex: 1,
    border: '10px solid #ccc',
    padding: '10px',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    textAlign: 'center',
    fontWeight: 'bold',
    color: 'white',
  };

  const cardData = [
    {
      backgroundImage:
        'url("https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8YXBhcnRtZW50fGVufDB8fDB8fHww&w=1000&q=80")',
      label: 'APPARTMENTS',
    },
    {
      backgroundImage:
        'url("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFuc2lvbnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60")',
      label: 'MANSIONETTES',
    },
    {
      backgroundImage:
        'url("https://media.istockphoto.com/id/516105688/photo/quaint-cape-cod-style-house.webp?b=1&s=170667a&w=0&k=20&c=7tyu9zUW1QNmLCNS8TKRXe_4M_GV_BBsrYCaR_iMsUk=")',
      label: 'COTTAGES',
    },
    {
      backgroundImage:
        'url("https://images.unsplash.com/photo-1605146769289-440113cc3d00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8U01BTEwlMjBIT1VTRXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60")',
      label: 'BUNGALOWS',
    },
    {
      backgroundImage:
        'url("https://images.unsplash.com/photo-1601056645510-77f6d98cf7d9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8QkxVRSUyMEhPVVNFfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60")',
      label: 'GET-AWAY HOMES',
    },
    {
      backgroundImage:
        'url("https://images.unsplash.com/photo-1534237710431-e2fc698436d0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YnVpbGRpbmd8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60")',
      label: 'STUDENT HOSTELS',
    },
  ];

  return (
    <div style={cardContainerStyle}>
      {cardData.map((card, index) => (
        <div key={index} style={{ ...cardStyle, backgroundImage: card.backgroundImage }}>
          {card.label}
        </div>
      ))}
    </div>
  );
};

export default CardComponent;

