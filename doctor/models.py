from datetime import datetime
from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _


class DateMixin(models.Model):
    """
    A mixin allowing developer to
    create and manage models with create
    and update datetime field
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        editable=False,
    )

    def has_been_created_before(self, date: datetime) -> Any:
        return self.created_at < date

    def has_been_created_after(self, date: datetime) -> Any:
        return self.created_at > date

    def has_been_updated(self) -> Any:
        return self.created_at != self.updated_at

    def has_been_updated_before(self, date: datetime) -> Any:
        return self.has_been_updated() and self.updated_at < date

    def has_been_updated_after(self, date: datetime) -> Any:
        return self.has_been_updated() and self.updated_at > date


class Address(DateMixin):
    """Abstract model for address"""

    class Meta:
        abstract = True

    country = models.CharField(
        max_length=45,
        blank=False,
        verbose_name=_("Country"),
    )
    city = models.CharField(
        max_length=50,
        blank=False,
        verbose_name=_("City"),
    )
    district = models.CharField(
        max_length=55,
        blank=False,
        verbose_name=_("district"),
    )
    address_line1 = models.CharField(
        max_length=45,
        verbose_name=_("Address line 1"),
    )
    address_line2 = models.CharField(
        max_length=45,
        blank=True,
        default='',
        verbose_name=_("Address line 2"),
    )
    postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Postal code"),
    )
    latitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_("Latitude"),
    )
    longitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_("Longitude"),
    )
    timezone = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name=_("Timezone"),
    )


class Doctor(Address, DateMixin):
    """Model for doctor"""

    LANGUAGE_CHOICES = (
        ("English", _("English")),
        ("French", _("French")),
        ("German", _("German")),
        ("Spanish", _("Spanish")),
        ("Italian", _("Italian")),
        ("Russian", _("Russian")),
        ("Chinese", _("Chinese")),
    )

    first_name = models.CharField(
        max_length=45,
        blank=False,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=45,
        blank=False,
        verbose_name=_("Last name"),
    )
    email = models.EmailField(
        blank=False,
        verbose_name=_("Email"),
    )
    phone_number = models.CharField(
        max_length=15,
        blank=False,
        verbose_name=_("Phone number"),
    )
    speciality = models.CharField(
        max_length=45,
        blank=False,
        verbose_name=_("Speciality"),
    )
    consultation_fee = models.FloatField(
        blank=False,
        verbose_name=_("Consultation fee"),
    )

    membership_exclusive_price = models.FloatField(
        blank=False,
        verbose_name=_("Membership exclusive price"),
    )

    language = models.CharField(
        max_length=45,
        choices=LANGUAGE_CHOICES,
        blank=False,
        verbose_name=_("Languages"),
    )

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class DoctorSchedule(DateMixin):
    """Model for doctor schedule"""

    DAY_CHOICES = [
        ("Monday", _("Monday")),
        ("Tuesday", _("Tuesday")),
        ("Wednesday", _("Wednesday")),
        ("Thursday", _("Thursday")),
        ("Friday", _("Friday")),
        ("Saturday", _("Saturday")),
        ("Sunday", _("Sunday")),
    ]

    doctor = models.ForeignKey(
        Doctor,
        verbose_name=_("Doctor"),
        related_name='schedules',
        on_delete=models.CASCADE,
    )

    day = models.CharField(
        max_length=15,
        blank=False,
        choices=DAY_CHOICES,
        verbose_name=_("Day"),
    )

    start_time = models.TimeField(
        blank=False,
        verbose_name=_("Start time"),
    )

    end_time = models.TimeField(
        blank=False,
        verbose_name=_("End time"),
    )

    class Meta:
        verbose_name = _("Doctor schedule")
        verbose_name_plural = _("Doctor schedules")

    def __str__(self) -> str:
        return f"{self.doctor} - {self.day}"

    def is_available(self) -> bool:
        return self.start_time < self.end_time

    def is_available_before(self, time: datetime) -> bool:
        return self.is_available() and self.start_time < time

    def is_available_after(self, time: datetime) -> bool:
        return self.is_available() and self.end_time > time
