#!/usr/bin/python
# -*- coding: utf-8 -*-

from bc.bancocentral import Inflacao, Poupanca, Cambio, Selic

inflacao = Inflacao()
print(u'Inflação Meta: %s' % inflacao.get_meta_tax())
print(u'Inflação acumulada 12 últimos meses: %s' % inflacao.get_acumulada_tax())

poupanca = Poupanca()
print(u'Poupança: %s' % poupanca.get_poupanca_tax())

cambio = Cambio()
print(u'Dólar compra PTAX: %s' % cambio.get_dolar_compra_ptax())
print(u'Dólar venda PTAX: %s' % cambio.get_dolar_venda_ptax())
print(u'Dólar compra: %s' % cambio.get_dolar_compra())
print(u'Dólar venda: %s' % cambio.get_dolar_venda())
print(u'Euro compra PTAX: %s' % cambio.get_euro_compra_ptax())
print(u'Euro venda PTAX: %s' % cambio.get_euro_venda_ptax())
print(u'Euro compra: %s' % cambio.get_euro_compra())
print(u'Euro venda: %s' % cambio.get_euro_venda())

selic = Selic()
print(u'Selic meta: %s' % selic.get_selic_meta())
print(u'Selic real: %s' % selic.get_selic_real())
