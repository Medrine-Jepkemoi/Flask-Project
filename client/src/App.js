import './App.css';
import Navbar from './Navbar';
import LandingText from './landingtext';
import CardComponent from './cartegorycard';
import About from './about';
import Home from './Home'
import LoginForm from './loginform';

function App() {
  return (
    
    <div className="App">
      <LoginForm />
      <Navbar />
      <LandingText />
      <div style={{ background: '#ccc', textAlign: 'center' }}>
        <h1>WHAT WE OFFER</h1>
      </div>
      <CardComponent /> 
      <About />
      
      <Home />
      
      
    </div>
    
  );
}

export default App;
