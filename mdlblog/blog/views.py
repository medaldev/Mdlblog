from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View, CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = 'partial/index.html'

    def get(self, request):
        return render(request, self.template_name, {})


