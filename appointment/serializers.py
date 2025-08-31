from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=DoctorType.objects.all())]
    )

    class Meta:
        model = DoctorType
        fields = ['id', 'specialization']


class DoctorNameSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name']


class DoctorNameDetailSerializer(serializers.ModelSerializer):
    appointments = serializers.SerializerMethodField()

    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name', 'main_specialization', 'appointments']
    
    def get_appointments(self, obj):
        visits = AppointmentDates.objects.filter(doctor=obj)
        return AppointmentDatesSerializer(visits, many=True).data
 

class AppointmentDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDates
        fields = ['id', 'date', 'time']


class DoctorNameNestedSerializer(serializers.ModelSerializer):
    appointments = AppointmentDatesSerializer(source='appointmentdates_set', many=True, read_only=True)

    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name', 'appointments']


class DoctorTypeSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = ['id', 'specialization']


class DoctorNameSerializer(serializers.ModelSerializer):
    main_specialization = DoctorTypeSimpleSerializer(read_only=True) 
    
    main_specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorType.objects.all(),
        source='main_specialization',
        write_only=True
    )

    
    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name', 'main_specialization', 'main_specialization_id']
        validators = [UniqueTogetherValidator(
            queryset=DoctorName.objects.all(),
            fields=['first_name', 'last_name', 'main_specialization']
        )]
