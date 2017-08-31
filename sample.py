#!/usr/bin/python
# -*- coding: utf-8 -*-

from bancocentral import Inflacao, Poupanca, Dolar, Selic

infl = Inflacao()
print(u'Inflação Meta: %s' % infl.get_meta_tax())
print(u'Inflação acumulada 12 últimos meses: %s' % infl.get_acumulada_tax())

poup = Poupanca()
print(u'Poupança: %s' % poup.get_poupanca_tax())

dolar = Dolar()
print(u'Dólar compra: %s' % dolar.get_dolar_compra())
print(u'Dólar venda: %s' % dolar.get_dolar_venda())

selic = Selic()
print(u'Selic meta: %s' % selic.get_selic_meta())
print(u'Selic real: %s' % selic.get_selic_real())
