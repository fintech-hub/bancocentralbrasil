#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from bancocentral import Inflacao, Poupanca, Cambio, Selic

class TestCase(unittest.TestCase):

    def setUp(self):
        self.inflacao = Inflacao()
        self.poupanca = Poupanca()
        self.cambio = Cambio()
        self.selic = Selic()

    """ Inflação """
    def test_inflacao_meta(self):
        self.assertIsNotNone(self.inflacao.get_meta_tax())

    def test_inflacao_meta_maior_zero(self):
        self.assertTrue(self.inflacao.get_meta_tax() > 0)

    def test_inflacao_acumulada(self):
        self.assertIsNotNone(self.inflacao.get_acumulada_tax())

    def test_inflacao_acumulada_maior_zero(self):
        self.assertTrue(self.inflacao.get_acumulada_tax() > 0)

    """ Poupança """
    def test_poupanca(self):
        self.assertIsNotNone(self.poupanca.get_poupanca_tax())

    def test_poupanca_maior_zero(self):
        self.assertTrue(self.poupanca.get_poupanca_tax() > 0)

    """ Câmbio """

    """ Dólar """
    def test_dolar_compra(self):
        self.assertIsNotNone(self.cambio.get_dolar_compra())

    def test_dolar_compra_ptax(self):
        self.assertIsNotNone(self.cambio.get_dolar_compra_ptax())

    def test_dolar_compra_maior_zero(self):
        self.assertTrue(self.cambio.get_dolar_compra() > 0)

    def test_dolar_compra_ptax_maior_zero(self):
        self.assertTrue(self.cambio.get_dolar_compra_ptax() > 0)

    def test_dolar_venda(self):
        self.assertIsNotNone(self.cambio.get_dolar_venda())

    def test_dolar_venda_ptax(self):
        self.assertIsNotNone(self.cambio.get_dolar_venda_ptax())

    def test_dolar_venda_maior_zero(self):
        self.assertTrue(self.cambio.get_dolar_venda() > 0)

    def test_dolar_venda_ptax_maior_zero(self):
        self.assertTrue(self.cambio.get_dolar_venda_ptax() > 0)

    """ Euro """
    def test_euro_compra(self):
        self.assertIsNotNone(self.cambio.get_euro_compra())

    def test_euro_compra_maior_zero(self):
        self.assertTrue(self.cambio.get_euro_compra() > 0)

    def test_euro_venda(self):
        self.assertIsNotNone(self.cambio.get_euro_venda())

    def test_euro_venda_maior_zero(self):
        self.assertTrue(self.cambio.get_euro_venda() > 0)

    def test_euro_compra_ptax(self):
        self.assertIsNotNone(self.cambio.get_euro_compra_ptax())

    def test_euro_compra_ptax_maior_zero(self):
        self.assertTrue(self.cambio.get_euro_compra_ptax() > 0)

    def test_euro_venda_ptax(self):
        self.assertIsNotNone(self.cambio.get_euro_venda_ptax())

    def test_euro_venda_ptax_maior_zero(self):
        self.assertTrue(self.cambio.get_euro_venda_ptax() > 0)

    """ Taxa Selic """
    def test_selic_meta(self):
        self.assertIsNotNone(self.selic.get_selic_meta())

    def test_selic_meta_maior_zero(self):
        self.assertTrue(self.selic.get_selic_meta() > 0)

    def test_selic_real(self):
        self.assertIsNotNone(self.selic.get_selic_real())

    def test_selic_real_maior_zero(self):
        self.assertTrue(self.selic.get_selic_real() > 0)
        
    def test_cleanContent(self):
        mock = "<content>&gt;</content>&lt;&gt;\r\n'"
        lista = ["&lt;","<content>","&gt;","</content>","&lt;","&gt;","\r\n"]
        mock = cleanContent(mock)
        self.assertTrue(([i in mock for i in lista].count(True)) == 0 )

    def test_disponibility_of_services(self):
        links = [
        "https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/inflacao"
        ,"https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca"
        ,"https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio"
        ,"https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros"
        ]
        for i in [ requests.get(link) for link in links]:
            elf.assertTrue(i.status_code == 200)

if __name__ == '__main__':
    unittest.main()
