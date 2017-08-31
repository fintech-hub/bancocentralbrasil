#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from bancocentral import Inflacao
from bancocentral import Poupanca
from bancocentral import Dolar
from bancocentral import Selic

class TestCase(unittest.TestCase):

	def test_inflacao_meta(self):
		inflacao = Inflacao()
		self.assertIsNotNone(inflacao.get_meta_tax())

	def test_inflacao_meta_maior_zero(self):
		inflacao = Inflacao()
		inflacao_meta = float(inflacao.get_meta_tax().replace(',','.'))
		self.assertTrue(inflacao_meta > 0)

	def test_inflacao_acumulada(self):
		inflacao = Inflacao()
		self.assertIsNotNone(inflacao.get_acumulada_tax())

	def test_inflacao_acumulada_maior_zero(self):
		inflacao = Inflacao()
		inflacao_acumulada = float(inflacao.get_acumulada_tax().replace(',','.'))
		self.assertTrue(inflacao_acumulada > 0)

	def test_poupanca(self):
		poupanca = Poupanca()
		self.assertIsNotNone(poupanca.get_poupanca_tax())

	def test_poupanca_maior_zero(self):
		poupanca = Poupanca()
		poupanca_tax = float(poupanca.get_poupanca_tax().replace(',','.'))
		self.assertTrue(poupanca_tax > 0)

	def test_dolar_compra(self):
		dolar = Dolar()
		self.assertIsNotNone(dolar.get_dolar_compra())

	def test_dolar_compra_maior_zero(self):
		dolar = Dolar()
		dolar_compra = float(dolar.get_dolar_compra().replace(',','.'))
		self.assertTrue(dolar_compra > 0)

	def test_dolar_venda(self):
		dolar = Dolar()
		self.assertIsNotNone(dolar.get_dolar_venda())

	def test_dolar_venda_maior_zero(self):
		dolar = Dolar()
		dolar_venda = float(dolar.get_dolar_venda().replace(',','.'))
		self.assertTrue(dolar_venda > 0)

	def test_selic_meta(self):
		selic = Selic()
		self.assertIsNotNone(selic.get_selic_meta())

	def test_selic_meta_maior_zero(self):
		selic = Selic()
		selic_meta = float(selic.get_selic_meta().replace(',','.'))
		self.assertTrue(selic_meta > 0)

	def test_selic_real(self):
		selic = Selic()
		self.assertIsNotNone(selic.get_selic_real())

	def test_selic_real_maior_zero(self):
		selic = Selic()
		selic_real = float(selic.get_selic_real().replace(',','.'))
		self.assertTrue(selic_real > 0)

if __name__ == '__main__':
    unittest.main()
