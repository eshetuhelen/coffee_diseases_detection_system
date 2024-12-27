from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from .models import CoffeeLeafImage
from .serializers import CoffeeLeafImageSerializer
import os
import json
import subprocess
import threading
import tensorflow as tf

class CoffeeLeafImageListView(APIView):
    def get(self, request):
        images = CoffeeLeafImage.objects.all()
        serializer = CoffeeLeafImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):
    return HttpResponse("Welcome to the Coffee Leaf Detection System!")

def get_dataset_structure(request):
    base_path = "C:/Users/dell/Desktop/archive/ethiopian cofee leaf dataset/train aug"

    dataset_structure = {}
    for dirpath, dirnames, filenames in os.walk(base_path):
        relative_path = os.path.relpath(dirpath, base_path)
        dataset_structure[relative_path] = {
            "num_directories": len(dirnames),
            "num_images": len(filenames),
            "image_names": filenames
        }

    return JsonResponse(dataset_structure)

def create_new_disease(request):
    if request.method == "POST":
        new_disease_name = request.POST.get("disease_name")
        base_path = "C:/Users/dell/Desktop/archive/ethiopian cofee leaf dataset/train aug"

        new_dir_path = os.path.join(base_path, new_disease_name)

        try:
            os.makedirs(new_dir_path, exist_ok=True)
            return JsonResponse({"status": "success", "message": f"Directory '{new_disease_name}' created successfully."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

class TrainModelView(APIView):
    def post(self, request):
        try:
            # Start training in a separate thread
            threading.Thread(target=self.train_model).start()
            return Response({"status": "success", "message": "Training started."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def train_model(self):
        # Path to training script
        training_script = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/notebooks/train_model.py"
        subprocess.run(["python", training_script], shell=True)

class TestModelView(APIView):
    def post(self, request):
        if 'image' not in request.FILES:
            return Response({"status": "error", "message": "No image uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['image']
        # Ensure test directory exists
        test_dir = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/api/media/test"
        os.makedirs(test_dir, exist_ok=True)
        temp_path = os.path.join(test_dir, image.name)
        with open(temp_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        prediction, confidence = self.predict_image(temp_path)

        # Optionally, remove the temporary image after prediction
        os.remove(temp_path)

        return Response({
            "status": "success",
            "predicted_class": prediction,
            "confidence_score": confidence
        }, status=status.HTTP_200_OK)

    def predict_image(self, image_path):
        # Load the trained model
        model_path = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/api/model.h5"
        class_names_path = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/api/class_names.json"

        if not os.path.exists(model_path) or not os.path.exists(class_names_path):
            return "Model or class names not found.", 0.0

        model = tf.keras.models.load_model(model_path)

        with open(class_names_path, 'r') as f:
            class_names = json.load(f)

        # Load and preprocess the image
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis

        # Normalize if required
        img_array /= 255.0

        # Predict
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]
        confidence_score = float(np.max(predictions))

        return predicted_class, confidence_score

import logging
import os
from django.http import JsonResponse

# Set up logger
logger = logging.getLogger(__name__)

def create_new_disease(request):
    if request.method == "POST":
        disease_name = request.POST.get("disease_name")
        
        # Log the received request
        logger.info(f"Received request to add disease: {disease_name}")
        
        base_path = "C:/Users/dell/Desktop/archive/ethiopian cofee leaf dataset/train aug"

        # Assuming disease_name is prefixed with fruit type, e.g., mango_blight or coffee_leaf_rust
        if "_" in disease_name:
            fruit_type, disease = disease_name.split("_", 1)
            # Path for the new fruit and disease directory
            fruit_dir_path = os.path.join(base_path, fruit_type)
            new_dir_path = os.path.join(fruit_dir_path, disease)
        else:
            # If no fruit type is provided, handle it as a generic disease under 'unknown' fruit type
            fruit_dir_path = os.path.join(base_path, "unknown")
            new_dir_path = os.path.join(fruit_dir_path, disease_name)

        try:
            # Create the fruit category directory if it doesn't exist
            os.makedirs(fruit_dir_path, exist_ok=True)
            
            # Create the disease directory for the specific fruit
            os.makedirs(new_dir_path, exist_ok=True)
            
            # Log success
            logger.info(f"Directory '{new_dir_path}' created successfully under '{fruit_type}' category.")
            
            return JsonResponse({"status": "success", "message": f"Directory '{new_dir_path}' created successfully under '{fruit_type}' category."})
        except Exception as e:
            # Log the error if something goes wrong
            logger.error(f"Error creating directory '{new_dir_path}': {str(e)}")
            return JsonResponse({"status": "error", "message": str(e)})

    # Log an invalid request method
    logger.warning("Invalid request method. Only POST requests are allowed.")
    return JsonResponse({"status": "error", "message": "Invalid request method."})
