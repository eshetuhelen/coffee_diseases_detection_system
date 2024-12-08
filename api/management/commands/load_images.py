import os
from django.core.management.base import BaseCommand
from api.models import CoffeeLeafImage

class Command(BaseCommand):
    help = 'Load coffee leaf images into the database'

    def handle(self, *args, **kwargs):
        dataset_path = r"C:\Users\dell\Desktop\archive\ethiopian cofee leaf dataset"  # Ensure correct path

        if not os.path.exists(dataset_path):
            self.stderr.write(f"Error: The dataset path '{dataset_path}' does not exist.")
            return

        self.stdout.write("Starting to process images...")

        # Walk through all directories and subdirectories in both 'train' and 'test'
        for root, dirs, files in os.walk(dataset_path):
            # Skip folders that aren't in 'train' or 'test'
            if 'train' in root or 'test' in root:
                # Process image files in these directories
                for filename in files:
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                        file_path = os.path.join(root, filename)
                        with open(file_path, 'rb') as image_file:
                            CoffeeLeafImage.objects.create(image=image_file.read(), name=filename)
                        self.stdout.write(f"Processed: {file_path}")

        self.stdout.write("All images have been successfully loaded!")
