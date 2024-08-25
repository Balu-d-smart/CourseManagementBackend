from django.urls import path
from . import views

urlpatterns = [
    # Course URLs
    path('api/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),

    # Instance URLs
    path('api/instances/<int:year>/<int:semester>/', views.InstanceListCreateView.as_view(), name='instance-list-create'),
    path('api/instances/<int:year>/<int:semester>/<int:id>/', views.InstanceDetailView.as_view(), name='instance-detail'),
]
