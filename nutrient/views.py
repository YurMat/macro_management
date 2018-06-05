from typing import Type

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView

from nutrient.models import DailyIntake
from .models import DailyIntake
from .forms import DailyIntakeForm

class DailyIntakeListView(ListView):

    model = DailyIntake

class DailyIntakeDetailView(DetailView):

    model = DailyIntake

class DailyIntakeCreateView(CreateView):

    model = DailyIntake
    form_class =  DailyIntakeForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance)
        )
        return result

class DailyIntakeUpdateView(UpdateView):

    model = DailyIntake
    form_class = DailyIntakeForm
    success_url = reverse_lazy()

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance)
        )
        return result

class DailyIntakeDeleteView(DeleteView):

    model = DailyIntake
    form_class = DailyIntakeForm
    success_url = reverse_lazy()

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object)
        )
        return result