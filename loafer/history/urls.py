from django.urls import path, include

from .views import *

urlpatterns = [
    path('', DictView.as_view(), name='dict_url'),
    path('update-phrase/<id>/', UpdatePhrase.as_view(), name='update_phrase_url'),
    path('delete-phrase/<id>/', DeletePhrase.as_view(), name='delete_phrase_url'),
    path('success-phrase/<id>/', SuccessPhrase.as_view(), name='success_phrase_url'),
    path('switch-transl-phrase/', SwitchTranslPhrase.as_view(), name='switch_transl_phrase_url'),
    path('switch-passed-url/', SwitchPassedUrl.as_view(), name='switch_passed_url'),
    path('switch-orig-phrase/', ShowOrigPhrase.as_view(), name='show_orig_phrase_url'),
    path('show-hotkeys/', ShowHotkeys.as_view(), name='show_hotkeys_url'),
    path('update-items-order/', update_items_order, name='update_items_order_url'),
    path('speach/<int:id>/', speach, name='speach_url')
]
