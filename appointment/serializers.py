from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.HyperlinkedModelSerializer): #HyperlinkedModelSerializer - dodaje linki, żeby można było wchodzić w opcje: delete, patch, put poprzez link a nie poprzez wpisywanie w przeglądarkę, jest też bardziej zgodne z filozofią REST: "HATEOAS – Hypermedia as the Engine of Application State"
    specialization = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=DoctorType.objects.all())] # sprawdzenie przed zapisem przy użyciu validators
    )
    
    class Meta:
        model = DoctorType
        fields = ['url', 'id', 'specialization']


class DoctorNameSerializer(serializers.HyperlinkedModelSerializer):
    # mogę użyć poniższego kodu żeby wyciągnąć nazwę specjalizacji tak żeby nie widniała tylko jako numer
    # main_specialization = serializers.PrimaryKeyRelatedField(queryset=DoctorType.objects.all()) # ściągamy pk z querysetu, "main_specialization" - nazwa variable z modelu
    # specialization_name = serializers.CharField(source="main_specialization.__str__", read_only=True)  # dodajemy pole tylko do odczytu, które poda __str__ z modelu - w ten sposób będzie widać nazwisko lekarza a nie tylko jego numer
    
    # lub użyć metody SlugRelatedField
    # main_specialization = serializers.SlugRelatedField(queryset=DoctorType.objects.all(), slug_field='specialization')
    
    # Jednak rezygnuje z powyższego, żeby zrobic nested serializer, ktory i tak wszystko wyswietli
    main_specialization = DoctorTypeSerializer(read_only=True)
    

    class Meta:
        model = DoctorName
        fields = ['url', 'id', 'first_name', 'last_name', 'main_specialization']
        # UniqueTogetherValidator - sprawdzamy czy kombinacja danych pól już występuje
        validators = [UniqueTogetherValidator(
            queryset=DoctorName.objects.all(),
            fields=['first_name', 'last_name', 'main_specialization']
        )]


class AppointmentDatesSerializer(serializers.HyperlinkedModelSerializer):
    # doctor = serializers.PrimaryKeyRelatedField(queryset=DoctorName.objects.all())
    # doctor_details = serializers.CharField(source="doctor.__str__", read_only=True)

    doctor = DoctorNameSerializer(read_only=True)

    class Meta:
        model = AppointmentDates
        fields = ['url', 'id', 'doctor', 'date', 'time']
        validators = [UniqueTogetherValidator(
            queryset=AppointmentDates.objects.all(),
            fields=['doctor', 'date', 'time']
        )]










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