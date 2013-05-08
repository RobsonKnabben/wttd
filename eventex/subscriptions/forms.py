# coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        # usa exclude pra ignorar campos do modelo
        # pode ser utilizado fields para definir todos os campos a serem mostrados do modelo
        exclude = ('paid',)