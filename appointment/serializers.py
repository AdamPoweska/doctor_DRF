from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = '__all__'


class DoctorNameSerializer(serializers.ModelSerializer):
    main_specialization = serializers.PrimaryKeyRelatedField(queryset=DoctorType.objects.all()) # ściągamy pk z querysetu 
    specialization_name = serializers.CharField(source="main_specialization.__str__", read_only=True)  # dodajemy pole tylko do odczytu, które poda __str__ z modelu - w ten sposób będzie widać nazwisko lekarza a nie tylko jego numer

    class Meta:
        model = DoctorName
        fields = '__all__'


class AppointmentDateseSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=DoctorName.objects.all())
    doctor_details = serializers.CharField(source="doctor.__str__", read_only=True)

    class Meta:
        model = AppointmentDates
        fields = '__all__'








# poniższe przy dodawaniu użytkowników
# class FinalAppointmentDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FinalAppointmentDetails
#         fields = '__all__'

# # poniższe do sprawdzenia jak się będą sprawowały:
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']