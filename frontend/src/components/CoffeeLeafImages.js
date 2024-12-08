import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CoffeeLeafImages() {
    const [images, setImages] = useState([]);

    useEffect(() => {
        const fetchImages = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/images/');
                setImages(response.data);
            } catch (error) {
                console.error('Error fetching images:', error);
            }
        };

        fetchImages();
    }, []);

    return (
        <div>
            <h2>Coffee Leaf Images</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
                {images.map((img) => (
                    <div key={img.id}>
                        <h4>{img.name}</h4>
                        <img 
                            src={`data:image/jpeg;base64,${img.image_base64}`} 
                            alt={img.name} 
                            style={{ width: '200px', height: '200px', objectFit: 'cover' }} 
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}

export default CoffeeLeafImages;
