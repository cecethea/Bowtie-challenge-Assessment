from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from doctor.models import Doctor, DoctorSchedule
from doctor.serializers import DoctorSerializer, DoctorScheduleSerializer


class DoctorScheduleViewSet(viewsets.ModelViewSet):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        district = self.request.query_params.get('district')
        category = self.request.query_params.get('category')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        language = self.request.query_params.get('language')

        # Apply filters based on query parameters
        if district:
            queryset = queryset.filter(district=district)
        if category:
            queryset = queryset.filter(speciality=category)
        if price_min:
            queryset = queryset.filter(consultation_fee__gte=price_min)
        if price_max:
            queryset = queryset.filter(consultation_fee__lte=price_max)
        if language:
            queryset = queryset.filter(language=language)

        # Retrieve related schedules for each doctor
        queryset = queryset.prefetch_related('doctorschedule_set')

        print(queryset.query)

        return queryset
