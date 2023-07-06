import React, { useState, useEffect } from 'react';
import axios from 'axios';
import HomeCard from './showProperty';


const Home = () => {
  const [homes, setHomes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/user/products')
      .then(response => {
        setHomes(response.data);
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      {homes.map(home => (
        <HomeCard key={home.property_id} home={home} />
      ))}
    </div>
  );
};

export default Home;
