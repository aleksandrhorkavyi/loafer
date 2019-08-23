from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        return render(request, self.template, {'form': self.form_model()})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_form_model = bound_form.save()
            return redirect(new_form_model)
        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    template = None
    form_model = None
    model = None

    def get(self, request, slug):
        model = self.model.objects.get(slug__iexact=slug)
        form_model = self.form_model(instance=model)
        return render(request, self.template, {
            'form': form_model,
            'model': self.model.__name__.lower(),
        })

    def post(self, request, slug):
        model = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=model)

        if bound_form.is_valid():
            new_form_model = bound_form.save()
            return redirect(new_form_model)
        return render(request, self.template, {
            'form': bound_form,
            self.model.__name__.lower(): model
        })
