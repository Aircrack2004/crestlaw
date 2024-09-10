from django.urls import path
from . import views

urlpatterns = [
    path('', views.representative_form_view, name='representative_form'),  # This will load the form
    path('submit/', views.representative_form_view, name='submit_form'),  # This handles the form submission
    path('success/', views.success_view, name='success'),  # This is the success page
]
