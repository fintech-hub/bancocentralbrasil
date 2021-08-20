#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re


class DataCotacaoNotFound(Exception):
    def __str__(self):
        return "Não foi possível capturar os dados do site"


class AttributeNotFound(Exception):
    def __str__(self):
        return "Atributo não encontrado"


class AcessarBancoCentral:

    def __init__(self, url):
        self.url = url

    def getURL(self):
        headers = {
            'Host': 'conteudo.bcb.gov.br',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'DNT': '1',
            'Content-Type': 'application/atom+xml',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6'
        }

        # Server very unstable. Test 10x http 200 response
        for _ in range(10):
            try:
                request = requests.get(self.url, headers=headers, timeout=50)
                if request.status_code != 200:
                    continue
                return request
            except requests.ConnectionError:
                continue

    @staticmethod
    def cleanContent(content):
        fix = {'&lt;': '<', '&gt;': '>'}
        for key, value in fix.items():
            content = content.replace(key, value)
        content = content.replace('\r\n', '')
        content = content.replace('/>    <content', '/> <content')
        return content


class Inflacao:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/inflacao'
        self.acesso = AcessarBancoCentral(self.query_url)
        self.req = self.acesso.getURL()

    def get_meta_tax(self):
        inflacao = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=label>Meta</div><div id=rate><div id=value>(\d*[\.\,]?\d+)</div>', inflacao)
        if not tax:
            raise DataCotacaoNotFound
        return float(tax.group(1).replace(',', '.'))

    def get_acumulada_tax(self):
        inflacao = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=label>Acumulada</div><div id=rate><div id=value>(\d*[\.\,]?\d+)</div>', inflacao)
        if not tax:
            raise DataCotacaoNotFound
        return float(tax.group(1).replace(',', '.'))


class Poupanca:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca'
        self.acesso = AcessarBancoCentral(self.query_url)
        self.req = self.acesso.getURL()

    def get_poupanca_tax(self):
        poupanca = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=value>(\d*[\.\,]?\d+)</div>', poupanca)
        if not tax:
            raise DataCotacaoNotFound
        return float(tax.group(1).replace(',', '.'))


class Cambio:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio'
        self.acesso = AcessarBancoCentral(self.query_url)
        self.req = self.acesso.getURL()
        self.cambio = self.acesso.cleanContent(self.req.content.decode('utf-8'))

    def get_dolar_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not compra:
            raise DataCotacaoNotFound
        return float(compra.group(1).replace(',', '.'))

    def get_dolar_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not venda:
            raise DataCotacaoNotFound
        return float(venda.group(1).replace(',', '.'))

    def get_data_dolar_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        search = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data.group(1))
        if not search:
            raise AttributeNotFound
        return search.group(1)

    def get_dolar_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not compra:
            raise DataCotacaoNotFound
        return float(compra.group(1).replace(',', '.'))

    def get_dolar_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not venda:
            raise DataCotacaoNotFound
        return float(venda.group(1).replace(',', '.'))

    def get_data_dolar(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        search = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data.group(1))
        if not search:
            raise AttributeNotFound
        return search.group(1)

    def get_euro_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not compra:
            raise DataCotacaoNotFound
        return float(compra.group(1).replace(',', '.'))

    def get_euro_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not venda:
            raise DataCotacaoNotFound
        return float(venda.group(1).replace(',', '.'))

    def get_data_euro_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        search = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data.group(1))
        if not search:
            raise AttributeNotFound
        return search.group(1)

    def get_euro_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not compra:
            raise DataCotacaoNotFound
        return float(compra.group(1).replace(',', '.'))

    def get_euro_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data.group(1))
        if not venda:
            raise DataCotacaoNotFound
        return float(venda.group(1).replace(',', '.'))

    def get_data_euro(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio)
        if not data:
            raise DataCotacaoNotFound
        search = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data.group(1))
        if not search:
            raise AttributeNotFound
        return search.group(1)


class Selic:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros'
        self.acesso = AcessarBancoCentral(self.query_url)
        self.req = self.acesso.getURL()

    def get_selic_meta(self):
        selic = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        selic_meta = re.search(r'<div id=ratevalue>(\d*[\.\,]?\d+)</div>', selic)
        if not selic_meta:
            raise DataCotacaoNotFound
        return float(selic_meta.group(1).replace(',', '.'))

    def get_data_selic_meta(self):
        selic = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        search = re.search(r'<div=ratedate>([\d/]+)</div>', selic)
        if not search:
            raise AttributeNotFound
        return search.group(1)

    def get_selic_real(self):
        selic = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        selic_real = re.search(r'<div id=dailyratevalue>(\d*[\.\,]?\d+)</div>', selic)
        if not selic_real:
            raise DataCotacaoNotFound
        return float(selic_real.group(1).replace(',', '.'))

    def get_data_selic_real(self):
        selic = self.acesso.cleanContent(self.req.content.decode('utf-8'))
        search = re.search(r'<div id=dailyratedate>([\d/]+)</div>', selic)
        if not search:
            raise AttributeNotFound
        return search.group(1)
