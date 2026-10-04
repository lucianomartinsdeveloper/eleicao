from django.urls import path

from . import views

app_name = 'person'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('new/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]
