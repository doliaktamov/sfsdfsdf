from re import template
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from main.models import Worker, Membership
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class WorkerListView(ListView):
    model = Worker
    template_name ='worker_list.html'

    def get_queryset(self):
        q = self.request.GET.get('query')
        if q:
            return self.model.objects.filter(fullname__icontains = q)
        else:
            return self.model.objects.all()

class WorkerCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.WorkerForm
    template_name = 'worker_form.html'

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['membership'] = Membership.objects.filter(worker = self.get_object())
        return context
    
class WorkerDeleteView(DeleteView):
    model = Worker
    success_url = reverse_lazy('worker_delete.html')

class WorkerUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    forms_class = forms.WorkerForm
    template_name = 'worker_form.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


