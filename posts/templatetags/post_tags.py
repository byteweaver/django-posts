from django import template

from posts.models import Post


register = template.Library()

class PostListNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        context['post_list'] = Post.objects.all()[:self.count]

@register.tag
def get_post_list(parser, token):
    return PostListNode(3)

