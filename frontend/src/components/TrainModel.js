import React, { useState } from 'react';

const TrainModel = () => {
    const [statusMessage, setStatusMessage] = useState('');

    const handleTrain = async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/train/", {
                method: "POST",
            });

            const data = await response.json();
            setStatusMessage(data.message);
        } catch (error) {
            setStatusMessage("Error: Unable to start training.");
        }
    };

    return (
        <div>
            <h2>Train Model</h2>
            <button onClick={handleTrain}>Train</button>
            {statusMessage && <p>{statusMessage}</p>}
        </div>
    );
};

export default TrainModel;
