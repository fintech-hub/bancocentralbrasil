#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from bc.bancocentral import AcessarBancoCentral
from bc.bancocentral import Inflacao, Poupanca, Cambio, Selic, cleanContent


def request_com_erro():
    return MagicMock(status_code=503)


def request_bem_sucedido():
    return MagicMock(status_code=200)


class TestCase(unittest.TestCase):

    def setUp(self):
        self.inflacao = Inflacao()
        self.poupanca = Poupanca()
        self.cambio = Cambio()
        self.selic = Selic()

        self.acesso = AcessarBancoCentral('http://my.url')

    """ Retry """
    @patch('bc.bancocentral.requests.get', return_value=request_com_erro())
    def test_nao_retorna_request_com_erro(self, mock_request):
        self.assertIsNone(self.acesso.getURL())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_retorna_request_bem_sucedido(self, mock_request):
        response = self.acesso.getURL()
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    @patch('bc.bancocentral.requests.get')
    def test_repete_request_enquanto_receber_erros(self, mock_request):
        requests = iter([request_com_erro(), request_bem_sucedido()])
        mock_request.side_effect = lambda *args, **kwargs: next(requests)

        self.assertIsNotNone(self.acesso.getURL())

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

    """ clean Content """
    def test_cleanContent(self):
        mock = "<content>&gt;</content>&lt;&gt;\r\n'"
        lista = ["&lt;", "<content>", "&gt;", "</content>", "&lt;", "&gt;", "\r\n"]
        mock = cleanContent(mock)
        self.assertFalse(([i in mock for i in lista].count(True)) == 0)


if __name__ == '__main__':
    unittest.main()
