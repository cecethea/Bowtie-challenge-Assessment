from rest_framework import serializers
from doctor.models import Doctor, DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = ['day', 'start_time', 'end_time', 'doctor']


class DoctorSerializer(serializers.ModelSerializer):
    schedules = DoctorScheduleSerializer(many=True, read_only=True, source='schedules.all')

    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'speciality',
            'consultation_fee',
            'membership_exclusive_price',
            'language',
            'country',
            'city',
            'district',
            'address_line1',
            'postal_code',
            'timezone',
            "latitude",
            "longitude",
            'schedules',
        ]
