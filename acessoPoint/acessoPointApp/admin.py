# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	list_display =  ['nome', 'sobrenome','sexo', 'cpf', 'rg','orgao_expedidor','telefone']
	save_as=True

admin.site.register(Pessoa,PessoaAdmin)
