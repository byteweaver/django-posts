from faker import Faker

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from posts.models import Post


faker = Faker()

class UserFactory(object):
    @classmethod
    def create(self):
        user = User()
        user.username = faker.username()
        user.email = faker.email()
        user.set_password('123')
        user.save()
        return user


class PostFactory(object):
    @classmethod
    def create(self):
        headline = ' '.join(faker.lorem().split(' ')[:4])

        post = Post()
        post.author = UserFactory.create()
        post.headline = headline
        post.slug = slugify(headline)
        post.text = faker.lorem()
        post.save()
        return post
