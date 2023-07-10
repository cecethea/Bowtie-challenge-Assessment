from django.contrib import admin
from doctor.models import Doctor, DoctorSchedule

# Register your models here.

admin.site.register(Doctor)
admin.site.register(DoctorSchedule)

