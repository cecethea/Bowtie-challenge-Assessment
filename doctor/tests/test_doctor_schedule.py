import json
import pytz
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.conf import settings
from doctor.factories import DoctorScheduleFactory
from necktie.factories import UserFactory

from necktie.testClasses import CustomAPITestCase

LOCAL_TIMEZONE = pytz.timezone(settings.TIME_ZONE)


class DoctorTests(CustomAPITestCase):

    ATTRIBUTES = [
      "doctor",
      "day",
      "end_time",
      "start_time",
    ]

    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.user.set_password('Test123!')
        self.user.save()

        self.schedule = DoctorScheduleFactory()
        self.schedule2 = DoctorScheduleFactory()

    def test_create_new_schedule(self):
        """
        Ensure we can create a new schedule.
        """
        data_post = {
            "day": "Thursday",
            "start_time": "10:00:00",
            "end_time": "14:30:00",
            "doctor": 1
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            reverse('schedule-list'),
            data_post,
            format='json',
        )

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.check_attributes(content)

    def test_update_schedule(self):
        """
        Ensure we can update a schedule.
        """
        day = "Monday"
        data_post = {
            'day': day,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            reverse(
                'schedule-detail',
                kwargs={
                    'pk': self.schedule.id
                },
            ),
            data_post,
            format='json',
        )

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.check_attributes(content)
        self.assertEqual(
            str(content['day']),
            day,
        )

    def test_delete_schedule(self):
        """
        Ensure we can delete a schedule.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse(
                'doctor-detail',
                kwargs={
                    'pk': self.schedule.id
                },
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b'')

    def test_list_position(self):
        """
        Ensure schedule can be listed.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('schedule-list'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
