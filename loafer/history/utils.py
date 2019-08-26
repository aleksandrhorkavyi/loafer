from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import *

class SessionSwitcherMixin:
    key = None
    val_on = True
    val_off = False

    def get(self, request):

        sess_value = request.session.get(self.key, None)
        print('---------------------')
        print(sess_value)
        print('---------------------')

        if sess_value == self.val_on:
            request.session[self.key] = self.val_off
        else:
            request.session[self.key] = self.val_on

        return redirect(request.META.get('HTTP_REFERER'))


class InitSessionSwitchersMixin:

    def initSessionSwitchers(self, request):
        if request.session.get('with_passed', None) is None:
            request.session['with_passed'] = False

        if request.session.get('orig_phrase', None) is None:
            request.session['orig_phrase'] = True

        if request.session.get('transl_phrase', None) is None:
            request.session['transl_phrase'] = True