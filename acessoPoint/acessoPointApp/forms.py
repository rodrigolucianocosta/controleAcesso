# -*- coding:utf-8 -*-
from django import forms
from models import Pessoa
from django.contrib.localflavor.br.br_states import STATE_CHOICES	

class FormPessoa(forms.Form):
	nome = forms.CharField()
	sobrenome = forms.CharField()
	sexo = forms.CharField(choices=sexoOpcoes)
	cpf = forms.CharField()
	rg = forms.CharField()
	orgao_expedidor = forms.CharField()
	telefone = forms.CharField()

	class Meta:
		model = Pessoa
		fields = ['nome','sobrenome']
