import React, { useState, useEffect } from 'react';

const AddDisease = () => {
    const [diseaseName, setDiseaseName] = useState('');
    const [fruitType, setFruitType] = useState('');
    const [responseMessage, setResponseMessage] = useState('');
    const [fruitTypes, setFruitTypes] = useState([]);

    useEffect(() => {
        // Fetch existing fruit types (e.g., coffee, mango)
        fetch("http://127.0.0.1:8000/api/dataset_structure/")
            .then(response => response.json())
            .then(data => {
                const fruits = Object.keys(data).filter(key => key !== '.'); // Exclude root
                setFruitTypes(fruits);
            })
            .catch(error => console.error("Error fetching dataset structure:", error));
    }, []);

    const handleAddDisease = async () => {
        if (!fruitType) {
            setResponseMessage("Please select a fruit type.");
            return;
        }

        const formData = new FormData();
        formData.append("disease_name", fruitType + "_" + diseaseName);  // Example: mango_blight

        try {
            const response = await fetch("http://127.0.0.1:8000/api/create_disease/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            setResponseMessage(data.message);
        } catch (error) {
            setResponseMessage("Error: Unable to create directory.");
        }
    };

    return (
        <div>
            <h2>Add New Disease</h2>
            <select value={fruitType} onChange={(e) => setFruitType(e.target.value)}>
                <option value="">Select Fruit Type</option>
                {fruitTypes.map((fruit, index) => (
                    <option key={index} value={fruit}>{fruit}</option>
                ))}
            </select>
            <input
                type="text"
                value={diseaseName}
                onChange={(e) => setDiseaseName(e.target.value)}
                placeholder="Enter disease name"
            />
            <button onClick={handleAddDisease}>Add Disease</button>
            {responseMessage && <p>{responseMessage}</p>}
        </div>
    );
};

export default AddDisease;
