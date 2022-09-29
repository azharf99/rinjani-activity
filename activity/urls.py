from django.urls import path
from activity import views

urlpatterns = [
    path('', views.index, name="home"),
    path('general/', views.general, name="general"),
    path('general/<int:pk>', views.general_detail, name="general-detail"),
    path('food/', views.food, name="food"),
    path('food/<int:pk>', views.food_detail, name="food-detail"),
    path('breast/', views.breast, name="breast"),
    path('breast/<int:pk>', views.breast_detail, name="breast-detail"),
    path('sleep/', views.sleep, name="sleep"),
    path('sleep/<int:pk>', views.sleep_detail, name="sleep-detail"),
    path('hygiene/', views.hygiene, name="hygiene"),
    path('hygiene/<int:pk>', views.hygiene_detail, name="hygiene-detail"),
    path('diaper/', views.diaper, name="diaper"),
    path('diaper/<int:pk>', views.diaper_detail, name="diaper-detail"),
    path('medicine/', views.medicine, name="medicine"),
    path('medicine/<int:pk>', views.medicine_detail, name="medicine-detail"),
]