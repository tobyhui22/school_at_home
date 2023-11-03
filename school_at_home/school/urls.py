from . import views
from django.urls import path


urlpatterns = [
    path('', views.schoolView.as_view(), name='index'),
    path('<int:id>/', views.schoolDetail, name='school-detail-view' ),
    path('class/<int:id>/', views.classDetail, name='class-detail'),
]