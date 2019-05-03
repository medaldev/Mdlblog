from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View, CreateView, UpdateView, DeleteView

from .models import Post

class Home(TemplateView):
    template_name = 'partial/index.html'

    def get(self, request):
        render_data = {
            "page_title": "Современные технологии IT сферы",
            "posts": Post.objects.all(),
        }
        return render(request, self.template_name, render_data)


class PostView(TemplateView):
    template_name = 'partial/post.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        render_data = {
            "page_title": post.title,
            "post": post,
        }
        return render(request, self.template_name, render_data)
