import './App.css';
import Navbar from './Navbar';
import LandingText from './landingtext';
import CardComponent from './cartegorycard';
import HomeCard from './showProperty'; 

function App() {
  return (
    <div className="App">
      <Navbar />
      <LandingText />
      <div style={{ background: '#ccc', textAlign: 'center' }}>
        <h1>OUR PROPERTY CATALOGUE</h1>
      </div>
      <CardComponent />
      <HomeCard />
    </div>
  );
}

export default App;
