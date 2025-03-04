from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = '__all__'


class DoctorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorName
        fields = '__all__'


class AppointmentDateseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDates
        fields = '__all__'


class FinalAppointmentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalAppointmentDetails
        fields = '__all__'

# poniższe do sprawdzenia jak się będą sprawowały:
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']