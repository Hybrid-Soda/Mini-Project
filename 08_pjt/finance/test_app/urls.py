from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.change_to_dataframe),
    path('missing_data/', views.processing_missing_value),
    path('avg_age/', views.calculate_avg_age),
]