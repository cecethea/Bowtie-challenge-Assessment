import factory
from factory.django import DjangoModelFactory
from .models import Doctor, DoctorSchedule

class DoctorFactory(DjangoModelFactory):
    class Meta:
        model = Doctor

    country = factory.Faker('country')
    city = factory.Faker('city')
    district = factory.Faker('word')
    address_line1 = factory.Faker('street_address')
    address_line2 = factory.Faker('secondary_address')
    postal_code = factory.Faker('postcode')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    timezone = factory.Faker('timezone')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    speciality = factory.Faker('job')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    membership_exclusive_price = factory.Faker('pystr', max_chars=45)
    language = factory.Faker(
        'random_element', 
        elements=['English', 'French', 'German', 'Spanish', 'Italian', 'Russian', 'Chinese']
    )

class DoctorScheduleFactory(DjangoModelFactory):
    class Meta:
        model = DoctorSchedule

    doctor = factory.SubFactory(DoctorFactory)
    day = factory.Faker(
        'random_element', 
        elements=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )
    start_time = factory.Faker('time')
    end_time = factory.Faker('time')
