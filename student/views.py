from rest_framework.generics import ListAPIView

from student.models import Student
from student.serializers import StudentSerializer


class StudentListView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
