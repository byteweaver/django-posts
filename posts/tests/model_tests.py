from django.test import TestCase

from posts.tests.factories import PostFactory


class PostTestCase(TestCase):

    def test_model(self):
        post = PostFactory()
        self.assertTrue(post.__unicode__()=='headline')
