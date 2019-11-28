#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re

class BancoCentralException(BaseException):
    pass

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
                request = requests.get(self.url, headers=headers, timeout=None)
                if request.status_code == 200:
                    return request
                elif request.status_code != 200:
                    continue
            except requests.ConnectionError:
                continue

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
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()

    def get_meta_tax(self):
        inflacao = cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=label>Meta</div><div id=rate><div id=value>(\d*\,?\d+)</div>', inflacao).group(1)
        return float(tax.replace(',','.'))

    def get_acumulada_tax(self):
        inflacao = cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=label>Acumulada</div><div id=rate><div id=value>(\d*\,?\d+)</div>', inflacao).group(1)
        return float(tax.replace(',','.'))


class Poupanca:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()

    def get_poupanca_tax(self):
        poupanca = cleanContent(self.req.content.decode('utf-8'))
        tax = re.search(r'<div id=value>(\d*\,?\d+)</div>', poupanca).group(1)
        return float(tax.replace(',','.'))


class Cambio:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()
        self.cambio = cleanContent(self.req.content.decode('utf-8'))

    def get_dolar_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio).group(1)
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(compra.replace(',','.'))

    def get_dolar_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio).group(1)
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(venda.replace(',','.'))

    def get_dolar_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio).group(1)
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(compra.replace(',','.'))

    def get_dolar_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio).group(1)
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(venda.replace(',','.'))

    def get_euro_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio).group(1)
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(compra.replace(',','.'))

    def get_euro_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio).group(1)
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(venda.replace(',','.'))

    def get_euro_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio).group(1)
        compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(compra.replace(',','.'))

    def get_euro_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio).group(1)
        venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*\,?\d+)</div>', data).group(1)
        return float(venda.replace(',','.'))


class Selic:

    def __init__(self): 
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()

    def get_selic_meta(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        selic_meta = re.search(r'<div id=ratevalue>(\d*\,?\d+)</div>', selic).group(1)
        return float(selic_meta.replace(',','.'))

    def get_selic_real(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        selic_real = re.search(r'<div id=dailyratevalue>(\d*\,?\d+)</div>', selic).group(1)
        return float(selic_real.replace(',','.'))
