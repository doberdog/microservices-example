import React, { Component } from 'react';
import './App.css';
import ZipCodeForm from "../components/ZipCodeForm";

class App extends Component {

    render() {
        return (
            <div className="app">
                <div className="content">
                    <div className="heading">
                        Get the Weather
                    </div>
                    <div className='form-content'>
                        <ZipCodeForm/>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
