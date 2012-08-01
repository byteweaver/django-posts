from django.views.generic import ListView, DetailView

from models import Post


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
