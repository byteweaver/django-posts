from django import template

from posts.models import Post


register = template.Library()

class PostListNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        context['post_list'] = Post.objects.all()[:self.count]
        return u''

@register.tag
def get_post_list(parser, token):
    try:
        tag_name, count_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return PostListNode(count_string)

