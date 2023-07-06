import './App.css';
import Navbar from './Navbar';
import LandingText from './landingtext';
import CardComponent from './cartegorycard';
import Home from './showProperty'; 

function App() {
  return (
    <div className="App">
      <Navbar />
      <LandingText />
      <div style={{ background: '#ccc', textAlign: 'center' }}>
        <h1>OUR PROPERTY CATALOGUE</h1>
      </div>
      <CardComponent />
      <Home/>
    </div>
  );
}

export default App;
