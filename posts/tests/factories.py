import factory

from django.contrib.auth.models import User

from posts.models import Post


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = 'user'
    email = 'mail@example.com'

class PostFactory(factory.Factory):
    FACTORY_FOR = Post

    author = factory.LazyAttribute(lambda a: UserFactory())
    headline = 'headline'
    text = 'text'
