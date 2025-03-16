from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.contrib.auth.models import User, Group

from .models import *


class DoctorTypeSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer - dodaje linki, żeby można było wchodzić w opcje: delete, patch, put poprzez link a nie poprzez wpisywanie w przeglądarkę, jest też bardziej zgodne z filozofią REST: "HATEOAS – Hypermedia as the Engine of Application State"
    specialization = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=DoctorType.objects.all())] # sprawdzenie przed zapisem przy użyciu validators
    )
    
    doctors = serializers.SerializerMethodField

    class Meta:
        model = DoctorType
        fields = ['id', 'specialization']
    
    def get_doctors(self, obj):
        doctors = DoctorName.objects.filter(main_specialization=obj)
        return DoctorNameSimpleSerializer(doctors, many=True).data


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
 

class DoctorNameSerializer(serializers.ModelSerializer):
    # mogę użyć poniższego kodu żeby wyciągnąć nazwę specjalizacji tak żeby nie widniała tylko jako numer
    # main_specialization = serializers.PrimaryKeyRelatedField(queryset=DoctorType.objects.all()) # ściągamy pk z querysetu, "main_specialization" - nazwa variable z modelu
    # specialization_name = serializers.CharField(source="main_specialization.__str__", read_only=True)  # dodajemy pole tylko do odczytu, które poda __str__ z modelu - w ten sposób będzie widać nazwisko lekarza a nie tylko jego numer
    
    # lub użyć metody SlugRelatedField
    # main_specialization = serializers.SlugRelatedField(queryset=DoctorType.objects.all(), slug_field='specialization')
    
    # Jednak rezygnuje z powyższego, żeby zrobic nested serializer, ktory i tak wszystko wyswietli
    main_specialization = DoctorTypeSerializer(read_only=True) 
    
    # kod tylko do zapisu - przy nested nie pojawi nam sie dropdown lista
    main_specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorType.objects.all(),
        source='main_specialization',
        write_only=True
    )

    
    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name', 'main_specialization', 'main_specialization_id']
        # UniqueTogetherValidator - sprawdzamy czy kombinacja danych pól już występuje
        validators = [UniqueTogetherValidator(
            queryset=DoctorName.objects.all(),
            fields=['first_name', 'last_name', 'main_specialization']
        )]


# class AppointmentDatesSerializer(serializers.ModelSerializer):
#     doctor = serializers.PrimaryKeyRelatedField(queryset=DoctorName.objects.all())
#     doctor_details = serializers.CharField(source="doctor.__str__", read_only=True)

#     # kod tylko do zapisu - przy nested nie pojawi nam sie dropdown lista
#     # doctor_specialization = serializers.PrimaryKeyRelatedField(
#     #     queryset=DoctorType.objects.all(),
#     #     source='main_specialization',
#     #     write_only=True
#     # )

#     # doctor = DoctorNameSerializer(read_only=True)

#     class Meta:
#         model = AppointmentDates
#         # fields = ['id','doctor_specialization', 'doctor', 'date', 'time']
#         fields = ['id', 'doctor', 'doctor_details', 'date', 'time']
#         validators = [UniqueTogetherValidator(
#             queryset=AppointmentDates.objects.all(),
#             fields=['doctor', 'date', 'time']
#         )]

class AppointmentDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDates
        fields = ['id', 'date', 'time']


class DoctorNameNestedSerializer(serializers.ModelSerializer):
    appointments = AppointmentDatesSerializer(source='appointmentdates_set', many=True, read_only=True)

    class Meta:
        model = DoctorName
        fields = ['id', 'first_name', 'last_name', 'appointments']





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