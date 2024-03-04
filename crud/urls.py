
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home),
   path('delete/<int:id>/', views.delete,name="deletedata"),
   path('<int:id>/', views.updet,name="updet"),
]