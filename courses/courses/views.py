
# Create your views here.
from rest_framework import generics
from .models import Course, Instance
from .serializers import CourseSerializer, InstanceSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Instance Views
class InstanceListCreateView(generics.ListCreateAPIView):
    serializer_class = InstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return Instance.objects.filter(year=year, semester=semester)

class InstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = InstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['id']
        return Instance.objects.get(year=year, semester=semester, course_id=course_id)
