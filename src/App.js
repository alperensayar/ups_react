import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import Homepage from "./pages/Homepage"
// import Courses from "./Components/Courses"
import StudentLogin from './components/StudentLogin';
import CompanyLogin from './components/CompanyLogin';
import StudentRegister from './components/StudentRegister';

import './App.css';


function App() {
    return (
        <>

            <Router>
                <Switch>
                    <Route exact path="/" 
                        component={Homepage} />

                    <Route exact path="/slogin" 
                        component={StudentLogin} />
                        <Route exact path="/clogin" 
                        component={CompanyLogin} />
                        <Route exact path="/sregister" 
                        component={StudentRegister} />
                </Switch>
            </Router>
        </>
    );
}

export default App;