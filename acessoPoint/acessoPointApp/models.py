# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

sexoOpcoes = [
	('F', 'feminino'),
	('M', 'masculino')
	]

class Pessoa(models.Model):
	nome = models.CharField('nome',max_length=20,null=True)
	sobrenome = models.CharField(max_length=50, null=True)
	sexo = models.CharField('sexo', max_length=1,choices=sexoOpcoes,null=True)
	cpf = models.CharField('cpf', max_length=11,null=True)
	rg = models.CharField('rg', max_length=20, null=True)
	orgao_expedidor = models.CharField(max_length=30, null=True)
	telefone = models.CharField('telefone',max_length=9,null=True)
#	email	
	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'

	def __unicode__(self):
		return "%s - %s - %s - %d - %d - %d" %(self.nome, self.sobrenome, self.sexo, self.cpf,self.rg, self.orgao_expedidor, self.telefone)

#class Endereco(models.Model):
#	rua = models.CharField('rua', max_length=50, null=true)
#	numero = models.IntergerField('numero', max_length = 5, null = True)
#	complemento
#	bairro
#	cep
#	cidade
#	estado
#	pais
	
