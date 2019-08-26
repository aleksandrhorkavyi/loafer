from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PhraseForm
from .models import Phrase
from .utils import SessionSwitcherMixin
from .utils import InitSessionSwitchersMixin

class DictView(InitSessionSwitchersMixin, View):
    form_model = PhraseForm
    template = 'history/dict.html'

    def get(self, request):
        self.initSessionSwitchers(request)
        with_passed = request.session.get('with_passed', False)
        phrases = Phrase.objects.filter(is_passed=False).all() if \
            with_passed else Phrase.objects.all()

        return render(request, self.template, {
            'form': self.form_model(),
            'phrases': phrases,
            'action': Phrase.get_absolute_url,
            'with_passed': with_passed,
        })

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('dict_url')

        with_passed = request.session.get('with_passed', False)
        phrases = Phrase.objects.filter(is_passed=False).all() if \
            with_passed else Phrase.objects.all()

        return render(request, self.template, {
            'form': bound_form,
            'phrases': phrases,
            'with_passed': with_passed,
        })


class DeletePhrase(InitSessionSwitchersMixin, View):
    def get(self, request, id):
        phrase = Phrase.objects.get(pk=id)
        phrase.delete()

        return redirect('dict_url')


class UpdatePhrase(InitSessionSwitchersMixin, View):
    form_model = PhraseForm
    template = 'history/dict.html'

    def get(self, request, id):
        phrase = Phrase.objects.get(pk=id)
        form = self.form_model(instance=phrase)

        with_passed = request.session.get('with_passed', False)
        phrases = Phrase.objects.filter(is_passed=False).all() if \
            with_passed else Phrase.objects.all()

        return render(request, self.template, {
            'form': form,
            'phrases': phrases,
            'action': Phrase.get_update_url,
            'with_passed': with_passed,
        })

    def post(self, request, id):
        model = Phrase.objects.get(pk=id)
        bound_form = self.form_model(request.POST, instance=model)

        with_passed = request.session.get('with_passed', False)
        phrases = Phrase.objects.filter(is_passed=False).all() if \
            with_passed else Phrase.objects.all()

        if bound_form.is_valid():
            bound_form.save()
            return redirect('dict_url')
        return render(request, self.template, {
            'form': bound_form,
            'phrases': phrases,
            'with_passed': with_passed,

        })


class SuccessPhrase(View):
    def get(self, request, id):
        phrase = Phrase.objects.get(pk=id)
        phrase.is_passed = 1
        phrase.save()
        return redirect('dict_url')


class SwitchTranslPhrase(SessionSwitcherMixin, View):
    key = 'transl_phrase'


class SwitchPassedUrl(SessionSwitcherMixin, View):
    key = 'with_passed'


class ShowOrigPhrase(SessionSwitcherMixin, View):
    key = 'orig_phrase'


class ShowHotkeys(SessionSwitcherMixin, View):
    key = 'show_hotkeys'


def update_items_order(request):
    items = dict(request.POST)
    tuple_items = tuple(items.keys())
    phrases = Phrase.objects.filter(id__in=tuple_items)

    for phrase in phrases:
        p_pos = items.get(str(phrase.pk))
        phrase.position = p_pos[0]
        phrase.save()

    return JsonResponse({'status': 'success'})