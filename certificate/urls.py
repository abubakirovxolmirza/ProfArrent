# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pdf/<int:pk>', views.PDFUserDetailView.as_view(), name='generate_pdf'),
]