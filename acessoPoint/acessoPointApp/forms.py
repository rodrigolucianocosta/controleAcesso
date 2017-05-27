# -*- coding:utf-8 -*-
from django import forms
from django.contrib.localflavor.br.br_states import STATE_CHOICES	

class FormPessoa(forms.Form):
	nome = forms.CharField()
	sobrenome = forms.CharField()
