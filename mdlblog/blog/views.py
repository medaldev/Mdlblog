from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View, CreateView, UpdateView, DeleteView

from .models import Post, Category


class Home(TemplateView):
    template_name = 'partial/index.html'

    def get(self, request):
        render_data = {
            "page_title": "Современные технологии IT сферы",
            "posts": Post.objects.all(),
            "categories": Category.objects.all(),
        }
        return render(request, self.template_name, render_data)


class PostView(TemplateView):
    template_name = 'partial/post.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        render_data = {
            "page_title": post.title,
            "post": post,
            "categories": Category.objects.all(),

        }
        return render(request, self.template_name, render_data)


class CategoryView(TemplateView):
    template_name = 'partial/category.html'

    def get(self, request, cat_id):
        category = Category.objects.get(id=cat_id)
        render_data = {
            "page_title": category.title,
            "category": category,
            "categories": Category.objects.all(),
            "posts": Post.objects.filter(cat_id=category),
        }
        print("*********************************\n" * 3)
        print(render_data["posts"])
        return render(request, self.template_name, render_data)


class CategoriesView(TemplateView):
    template_name = 'partial/categories.html'

    def get(self, request):
        render_data = {
            "page_title": "Категории",
            "categories": Category.objects.all(),
        }
        return render(request, self.template_name, render_data)


class NotFound(TemplateView):
    template_name = 'partial/404.html'

    def get(self, request):
        render_data = {
            "page_title": "404",
            "categories": Category.objects.all(),
        }
        return render(request, self.template_name, render_data)
