import factory

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from posts.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('first_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', '123')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    text = factory.Faker('text')
    headline = factory.Faker('sentence', nb_words=4, variable_nb_words=True)

    @factory.lazy_attribute
    def slug(self):
        return slugify(self.headline)
