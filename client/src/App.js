import './App.css';
import Navbar from './Navbar';
import LandingText from './landingtext';
import CardComponent from './cartegorycard';
import About from './about';
import Home from './Home'
// import LoginForm from './loginform';
// import SignUp from './SignUp';

function App() {
  return (
    
    <div className="App">
      {/* <SignUp />
      <LoginForm /> */}
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

// import React from 'react';
// import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
// import './App.css';
// import Navbar from './Navbar';
// import LandingText from './landingtext';
// import CardComponent from './cartegorycard';
// import About from './about';
// import Home from './Home';
// import Catalogue from './Catalogue';

// function App() {
//   return (
//     <Router>
//       <div className="App">
//         <Navbar />
//         <Switch>
//           <Route exact path="/" component={LandingText} />
//           <Route path="/catalogue" component={Catalogue} />
//         </Switch>
//         <div style={{ background: '#ccc', textAlign: 'center' }}>
//           <h1>WHAT WE OFFER</h1>
//         </div>
//         <CardComponent />
//         <About />
//       </div>
//     </Router>
//   );
// }

// export default App;
