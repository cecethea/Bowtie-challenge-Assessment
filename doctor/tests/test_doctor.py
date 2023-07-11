import json
import pytz
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.conf import settings
from doctor.factories import DoctorFactory
from necktie.factories import UserFactory

from necktie.testClasses import CustomAPITestCase

LOCAL_TIMEZONE = pytz.timezone(settings.TIME_ZONE)


class DoctorTests(CustomAPITestCase):

    ATTRIBUTES = [
      "first_name",
      "last_name",
      "speciality",
      "consultation_fee",
      "membership_exclusive_price",
      "language",
      "country",
      "city",
      "district",
      "address_line1",
      "postal_code",
      "timezone",
      "latitude",
      "longitude",
      "email",
      "phone_number",
    ]

    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.user.set_password('Test123!')
        self.user.save()

        self.doctor = DoctorFactory()
        self.doctor2 = DoctorFactory()

    def test_create_new_doctor(self):
        """
        Ensure we can create a new doctor.
        """
        data_post = {
          "first_name": "张",
          "last_name": "三",
          "speciality": "心脏病学",
          "consultation_fee": 100.00,
          "membership_exclusive_price": 80.00,
          "language": "中文",
          "country": "中国",
          "city": "北京",
          "district": "朝阳区",
          "address_line1": "北京市朝阳区XXX街道XXX号",
          "postal_code": "100000",
          "timezone": "Asia/Shanghai",
          "latitude": 39.9042,
          "longitude": 116.4074,
          "email": "test@gmail.com",
          "phone_number": "+8754845845",
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('doctor-list'),
            data_post,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_doctor(self):
        """
        Ensure we can update a doctor.
        """
        first_name = "Alpha"
        data_post = {
            'first_name': first_name,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            reverse(
                'doctor-detail',
                kwargs={
                    'pk': self.doctor.id
                },
            ),
            data_post,
            format='json',
        )

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            str(content['first_name']),
            first_name,
        )

    def test_delete_doctor(self):
        """
        Ensure we can delete a doctor.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse(
                'doctor-detail',
                kwargs={
                    'pk': self.doctor.id
                },
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b'')

    def test_list_doctor(self):
        """
        Ensure doctor can be listed.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('doctor-list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
