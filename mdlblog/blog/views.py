from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View, CreateView, UpdateView, DeleteView

"""class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})
"""


def home(request):
    return render(request, "partial/index.html")

