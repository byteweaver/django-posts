from django.test import TestCase

from posts.tests.factories import PostFactory


class PostTestCase(TestCase):
    def test_create_post(self):
        post = PostFactory.create()
        self.assertTrue(post.pk)
        self.assertTrue(post.author)
        self.assertTrue(post.headline)
        self.assertTrue(post.slug)
        self.assertTrue(post.text)
