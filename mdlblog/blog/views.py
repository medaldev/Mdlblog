from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View, CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = 'partial/index.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Post(TemplateView):
    template_name = 'partial/post.html'

    def get(self, request, post_id):
        return render(request, self.template_name, {})
