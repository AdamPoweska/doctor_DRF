from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.HyperlinkedModelSerializer): #HyperlinkedModelSerializer - dodaje linki, żeby można było wchodzić w opcje: delete, patch, put poprzez link a nie poprzez wpisywanie w przeglądarkę
    class Meta:
        model = DoctorType
        fields = ['url', 'id', 'specialization']


class DoctorNameSerializer(serializers.HyperlinkedModelSerializer):
    main_specialization = serializers.PrimaryKeyRelatedField(queryset=DoctorType.objects.all()) # ściągamy pk z querysetu, "main_specialization" - nazwa variable z modelu
    specialization_name = serializers.CharField(source="main_specialization.__str__", read_only=True)  # dodajemy pole tylko do odczytu, które poda __str__ z modelu - w ten sposób będzie widać nazwisko lekarza a nie tylko jego numer

    class Meta:
        model = DoctorName
        fields = ['url', 'id', 'first_name', 'last_name', 'main_specialization', 'specialization_name']


class AppointmentDatesSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=DoctorName.objects.all())
    doctor_details = serializers.CharField(source="doctor.__str__", read_only=True)

    class Meta:
        model = AppointmentDates
        fields = ['url', 'id', 'doctor', 'date', 'time', 'doctor_details']












# poniższe przy dodawaniu użytkowników - z tutoriala
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