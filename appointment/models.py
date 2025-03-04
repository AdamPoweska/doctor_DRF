# Create your models here.
from django.db import models


class DoctorType(models.Model):
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.specialization}"


class DoctorName(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    main_specialization = models.ForeignKey(DoctorType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.main_specialization}"


class AppointmentDates(models.Model):
    doctor = models.ForeignKey(DoctorName, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.date} at {self.time}"
    

class FinalAppointmentDetails(models.Model):
    doctor_type = models.ForeignKey(DoctorType, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(DoctorName, on_delete=models.CASCADE)
    visit_date = models.ForeignKey(AppointmentDates, on_delete=models.CASCADE)

    def __str__(self):
        return f"Your visit with {self.doctor_name} ({self.doctor_type}) as of: {self.visit_date.date} at: {self.visit_date.time}"
