from django.urls import reverse
from rest_framework.generics import ListCreateAPIView, GenericAPIView
import requests
from rest_framework.response import Response

from student.models import Student, Address
from student.serializers import StudentSerializer


class StudentListView(ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ReverseStudentJson(GenericAPIView):

    serializer_class = StudentSerializer

    def get_queryset(self):
        return []

    def get_students_json(self):
        # can change handler method to post
        # and get json from post.data
        return requests.get(f'http://localhost:8000{reverse("list")}').json()

    def get(self, request, *args, **kwargs):
        try:
            students_list = self.get_students_json()
        except Exception:
            return Response(status=400)
        self.get_serializer(data=students_list, many=True).is_valid(raise_exception=True)

        students_objects_list = []
        for student in students_list:
            address = student.pop('address')
            address_object = Address(**address)

            student_object = Student(**student, address=address_object)
            students_objects_list.append(student_object)

        return Response(
            data=self.get_serializer(
                reversed(students_objects_list), many=True
            ).data
        )

