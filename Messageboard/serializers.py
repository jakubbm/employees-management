from rest_framework import serializers

from .models import Message
from Employees.models import Employee


class MessageSerializer(serializers.ModelSerializer):
    employee_firstname = serializers.CharField(source='employee.first_name')
    employee_lastname = serializers.CharField(source='employee.last_name')
    profile_picture = serializers.ImageField(source='employee.profile_picture')

    class Meta:
        model = Message
        fields = ["message", "date", "employee_firstname", "employee_lastname", "profile_picture"]
        read_only_fields = ("employee_firstname", "employee_lastname", "date")


class MessageSerializerWrite(serializers.ModelSerializer):
    userId = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = ["message", "userId"]

    def create(self, validated_data):
        employee_id = validated_data.pop('userId')
        employee = Employee.objects.get(id=employee_id)
        message = validated_data.pop('message')
        post = Message.objects.create(employee=employee, message=message)
        return post
