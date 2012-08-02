from django import template

from posts.models import Post


register = template.Library()

class PostListNode(template.Node):
    def render(self, context):
        context['post_list'] = Post.objects.all()

@register.tag
def get_post_list(parser, token):
    return PostListNode()

