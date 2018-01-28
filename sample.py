#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancocentral import Inflacao, Poupanca, Dolar, Euro, Selic

inflacao = Inflacao()
print(u'Inflação Meta: %s' % inflacao.get_meta_tax())
print(u'Inflação acumulada 12 últimos meses: %s' % inflacao.get_acumulada_tax())

poupanca = Poupanca()
print(u'Poupança: %s' % poupanca.get_poupanca_tax())

dolar = Dolar()
print(u'Dólar compra: %s' % dolar.get_dolar_compra())
print(u'Dólar venda: %s' % dolar.get_dolar_venda())

euro = Euro()
print(u'Euro compra: %s' % euro.get_euro_compra())
print(u'Euro venda: %s' % euro.get_euro_venda())

selic = Selic()
print(u'Selic meta: %s' % selic.get_selic_meta())
print(u'Selic real: %s' % selic.get_selic_real())
