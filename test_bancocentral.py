#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from bancocentral import Inflacao, Poupanca, Dolar, Euro, Selic

class TestCase(unittest.TestCase):

	""" Inflação """
	def test_inflacao_meta(self):
		inflacao = Inflacao()
		self.assertIsNotNone(inflacao.get_meta_tax())

	def test_inflacao_meta_maior_zero(self):
		inflacao = Inflacao()
		#inflacao_meta = float(inflacao.get_meta_tax().replace(',','.'))
		self.assertTrue(inflacao.get_meta_tax() > 0)

	def test_inflacao_acumulada(self):
		inflacao = Inflacao()
		self.assertIsNotNone(inflacao.get_acumulada_tax())

	def test_inflacao_acumulada_maior_zero(self):
		inflacao = Inflacao()
		#inflacao_acumulada = float(inflacao.get_acumulada_tax().replace(',','.'))
		self.assertTrue(inflacao.get_acumulada_tax() > 0)

	""" Poupança """
	def test_poupanca(self):
		poupanca = Poupanca()
		self.assertIsNotNone(poupanca.get_poupanca_tax())

	def test_poupanca_maior_zero(self):
		poupanca = Poupanca()
		#poupanca_tax = float(poupanca.get_poupanca_tax().replace(',','.'))
		self.assertTrue(poupanca.get_poupanca_tax() > 0)

	""" Dólar """
	def test_dolar_compra(self):
		dolar = Dolar()
		self.assertIsNotNone(dolar.get_dolar_compra())

	def test_dolar_compra_maior_zero(self):
		dolar = Dolar()
		#dolar_compra = float(dolar.get_dolar_compra().replace(',','.'))
		self.assertTrue(dolar.get_dolar_compra() > 0)

	def test_dolar_venda(self):
		dolar = Dolar()
		self.assertIsNotNone(dolar.get_dolar_venda())

	def test_dolar_venda_maior_zero(self):
		dolar = Dolar()
		#dolar_venda = float(dolar.get_dolar_venda().replace(',','.'))
		self.assertTrue(dolar.get_dolar_venda() > 0)

	""" Euro """
	def test_euro_compra(self):
		euro = Euro()
		self.assertIsNotNone(euro.get_euro_compra())

	def test_euro_compra_maior_zero(self):
		euro = Euro()
		#dolar_compra = float(dolar.get_dolar_compra().replace(',','.'))
		self.assertTrue(euro.get_euro_compra() > 0)

	def test_euro_venda(self):
		euro = Euro()
		self.assertIsNotNone(euro.get_euro_venda())

	def test_euro_venda_maior_zero(self):
		euro = Euro()
		#dolar_venda = float(dolar.get_dolar_venda().replace(',','.'))
		self.assertTrue(euro.get_euro_venda() > 0)

	""" Taxa Selic """
	def test_selic_meta(self):
		selic = Selic()
		self.assertIsNotNone(selic.get_selic_meta())

	def test_selic_meta_maior_zero(self):
		selic = Selic()
		#selic_meta = float(selic.get_selic_meta().replace(',','.'))
		self.assertTrue(selic.get_selic_meta() > 0)

	def test_selic_real(self):
		selic = Selic()
		self.assertIsNotNone(selic.get_selic_real())

	def test_selic_real_maior_zero(self):
		selic = Selic()
		#selic_real = float(selic.get_selic_real().replace(',','.'))
		self.assertTrue(selic.get_selic_real() > 0)

if __name__ == '__main__':
    unittest.main()
