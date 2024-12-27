from django.urls import path
from .views import (
    CoffeeLeafImageListView,
    home,
    get_dataset_structure,
    create_new_disease,
    TrainModelView,
    TestModelView
)

urlpatterns = [
    path('', home, name='home'), 
    path('images/', CoffeeLeafImageListView.as_view(), name='image-list'),
    path('create_disease/', create_new_disease, name='create_disease'),
    path('train/', TrainModelView.as_view(), name='train_model'),
    path('test/', TestModelView.as_view(), name='test_model'),
]
