from rest_framework import serializers

from student.models import Student, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = Student
        fields = '__all__'
