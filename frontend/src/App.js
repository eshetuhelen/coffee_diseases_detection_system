import React from 'react';
import AddDisease from './components/AddDisease';
import TrainModel from './components/TrainModel';
import TestModel from './components/TestModel';

const App = () => {
    return (
        <div>
            <h1>Coffee Disease Detection System</h1>
            <AddDisease />
            <TrainModel />
            <TestModel />
        </div>
    );
};

export default App;
