from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm
from django.db.models import Q

def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query)
        )
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', {
        'posts': posts
    })


class PostView(ObjectDetailMixin, View):
    model = Post
    template = 'blog/view.html'


def tags(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', {'tags': tags})


class TagView(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_view.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    template = 'blog/tag_update.html'
    model = Tag
    form_model = TagForm


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    template = 'blog/post_update.html'
    form_model = PostForm


class PostDelete(View):

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('blog_index'))

class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_url'))

