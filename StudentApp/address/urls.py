from django.urls import path
from . import views

app_name = 'Address'

urlpatterns = [
    path('district-list/', views.district_list, name='district-list'),
    path('district-detail-info/<int:id>', views.district_detail, name='district-detail'),
]