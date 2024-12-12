import React, { useState } from 'react';

const TestModel = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [predictionResult, setPredictionResult] = useState(null);

    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
    };

    const handleTest = async () => {
        if (!selectedFile) {
            setPredictionResult({ status: 'error', message: 'No file selected.' });
            return;
        }

        const formData = new FormData();
        formData.append("image", selectedFile);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/test/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            setPredictionResult(data);
        } catch (error) {
            setPredictionResult({ status: 'error', message: 'Error: Unable to perform prediction.' });
        }
    };

    return (
        <div>
            <h2>Test Model</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleTest}>Test</button>
            {predictionResult && predictionResult.status === 'success' && (
                <div>
                    <p>Predicted Class: {predictionResult.predicted_class}</p>
                    <p>Confidence Score: {predictionResult.confidence_score}</p>
                </div>
            )}
            {predictionResult && predictionResult.status === 'error' && (
                <p>{predictionResult.message}</p>
            )}
        </div>
    );
};

export default TestModel;
