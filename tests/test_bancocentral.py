#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from bc.bancocentral import (
    AcessarBancoCentral,
    DataCotacaoNotFound,
    AttributeNotFound,
    Inflacao,
    Poupanca,
    Cambio,
    Selic,
)


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
    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_inflacao_meta(self, mock_request):
        self.assertIsNotNone(self.inflacao.get_meta_tax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_inflacao_meta_maior_zero(self, mock_request):
        self.assertTrue(self.inflacao.get_meta_tax() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_inflacao_acumulada(self, mock_request):
        self.assertIsNotNone(self.inflacao.get_acumulada_tax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_inflacao_acumulada_maior_zero(self, mock_request):
        self.assertTrue(self.inflacao.get_acumulada_tax() > 0)

    """ Poupança """
    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_poupanca(self, mock_request):
        self.assertIsNotNone(self.poupanca.get_poupanca_tax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_poupanca_maior_zero(self, mock_request):
        self.assertTrue(self.poupanca.get_poupanca_tax() > 0)

    """ Câmbio """

    """ Dólar """
    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_compra(self, mock_request):
        self.assertIsNotNone(self.cambio.get_dolar_compra())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_compra_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_dolar_compra_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_compra_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_dolar_compra() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_compra_ptax_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_dolar_compra_ptax() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_venda(self, mock_request):
        self.assertIsNotNone(self.cambio.get_dolar_venda())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_dolar(self, mock_request):
        self.assertIsNotNone(self.cambio.get_data_dolar())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_venda_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_dolar_venda_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_dolar_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_data_dolar_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_venda_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_dolar_venda() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_dolar_venda_ptax_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_dolar_venda_ptax() > 0)

    """ Euro """
    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_compra(self, mock_request):
        self.assertIsNotNone(self.cambio.get_euro_compra())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_compra_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_euro_compra() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_venda(self, mock_request):
        self.assertIsNotNone(self.cambio.get_euro_venda())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_euro(self, mock_request):
        self.assertIsNotNone(self.cambio.get_data_euro())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_venda_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_euro_venda() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_compra_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_euro_compra_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_euro_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_data_euro_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_compra_ptax_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_euro_compra_ptax() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_venda_ptax(self, mock_request):
        self.assertIsNotNone(self.cambio.get_euro_venda_ptax())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_euro_venda_ptax_maior_zero(self, mock_request):
        self.assertTrue(self.cambio.get_euro_venda_ptax() > 0)

    """ Taxa Selic """
    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_selic_meta(self, mock_request):
        self.assertIsNotNone(self.selic.get_selic_meta())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_selic_meta_maior_zero(self, mock_request):
        self.assertTrue(self.selic.get_selic_meta() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_selic_real(self, mock_request):
        self.assertIsNotNone(self.selic.get_selic_real())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_selic_real_maior_zero(self, mock_request):
        self.assertTrue(self.selic.get_selic_real() > 0)

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_selic_meta(self, mock_request):
        self.assertIsNotNone(self.selic.get_data_selic_meta())

    @patch('bc.bancocentral.requests.get', return_value=request_bem_sucedido())
    def test_get_data_selic_real(self, mock_request):
        self.assertIsNotNone(self.selic.get_data_selic_real())

    """ clean Content """
    def test_cleanContent(self):
        mock = "<content>&gt;</content>&lt;&gt;\r\n'"
        lista = ["&lt;", "<content>", "&gt;", "</content>", "&lt;", "&gt;", "\r\n"]
        mock = self.acesso.cleanContent(mock)
        self.assertFalse(([i in mock for i in lista].count(True)) == 0)

    def test_exceptions_datacotacao(self):
        with self.assertRaises(DataCotacaoNotFound) as exp:
            raise DataCotacaoNotFound
        error = exp.exception
        self.assertEqual(str(error), "Não foi possível capturar os dados do site")

    def test_exceptions_attribute(self):
        with self.assertRaises(AttributeNotFound) as exp:
            raise AttributeNotFound
        error = exp.exception
        self.assertEqual(str(error), "Atributo não encontrado")


if __name__ == '__main__':
    unittest.main()
