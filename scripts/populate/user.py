import factory
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = "user.User"
        
    phone_no = factory.LazyAttribute(lambda x: fake.phone_number()[:20])
    password = factory.PostGenerationMethodCall("set_password", fake.password())
    
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "user.Profile"
    
    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    email = factory.Faker('email')
    nation_no = factory.LazyAttribute(lambda x: fake.ssn())
    birth_date = factory.Faker('date_of_birth')
    profile_picture = factory.django.ImageField(color='blue')

class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "user.Address"
        
    user = factory.SubFactory(UserFactory)
    address = factory.Faker('street_address')
    city = factory.Faker('city')
    postal_code = factory.Faker('postcode')
    recipient_name = factory.Faker('name')
    latitude = factory.LazyAttribute(lambda x: float(fake.latitude()))
    longitude = factory.LazyAttribute(lambda x: float(fake.longitude()))
    # is_primary = factory.LazyAttribute(lambda obj: not obj.user.addresses.exists())
    
def generate_user_app_fake_data(num_user=5, num_address=2):
    for _ in range(num_user):
        u = UserFactory.create()
        ProfileFactory.create(user=u)
        
        for _ in range(num_address):
           AddressFactory.create() 