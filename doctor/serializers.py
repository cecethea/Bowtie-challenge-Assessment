from rest_framework import serializers
from doctor.models import Doctor, DoctorSchedule

class DoctorScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DoctorSchedule
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    schedules = DoctorScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'


