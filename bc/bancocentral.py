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
        if not inflacao:
          return None
        try:
          tax = re.search(r'<div id=label>Meta</div><div id=rate><div id=value>(\d*[\.\,]?\d+)</div>', inflacao).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(tax.replace(',','.'))

    def get_acumulada_tax(self):
        inflacao = cleanContent(self.req.content.decode('utf-8'))
        if not inflacao:
          return None
        try:
          tax = re.search(r'<div id=label>Acumulada</div><div id=rate><div id=value>(\d*[\.\,]?\d+)</div>', inflacao).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(tax.replace(',','.'))


class Poupanca:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()

    def get_poupanca_tax(self):
        poupanca = cleanContent(self.req.content.decode('utf-8'))
        if not poupanca:
          return None
        try:
          tax = re.search(r'<div id=value>(\d*[\.\,]?\d+)</div>', poupanca).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(tax.replace(',','.'))


class Cambio:

    def __init__(self):
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()
        self.cambio = cleanContent(self.req.content.decode('utf-8'))

    def get_dolar_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(compra.replace(',','.'))

    def get_dolar_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(venda.replace(',','.'))

    def get_data_dolar_ptax(self):
        # A data da cotacao eh a mesma para compra e venda
        data = re.search(r'INDICADOR_CAMBIO_DOLAR_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          data_dolar_ptax = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_dolar_ptax

    def get_dolar_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(compra.replace(',','.'))

    def get_dolar_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(venda.replace(',','.'))

    def get_data_dolar(self):
        # A data da cotacao eh a mesma para compra e venda
        data = re.search(r'INDICADOR_CAMBIO_DOLAR(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          data_dolar_ptax = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_dolar_ptax

    def get_euro_compra_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(compra.replace(',','.'))

    def get_euro_venda_ptax(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(venda.replace(',','.'))

    def get_data_euro_ptax(self):
        # A data da cotacao eh a mesma para compra e venda
        data = re.search(r'INDICADOR_CAMBIO_EURO_PTAX(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          data_euro_ptax = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_euro_ptax

    def get_euro_compra(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          compra = re.search(r'<div id=rate><div id=label>Compra</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(compra.replace(',','.'))

    def get_euro_venda(self):
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          venda = re.search(r'<div id=rate><div id=label>Venda</div><div id=value>(\d*[\.\,]?\d+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(venda.replace(',','.'))

    def get_data_euro(self):
        # A data da cotacao eh a mesma para compra e venda
        data = re.search(r'INDICADOR_CAMBIO_EURO(.*)</entry>', self.cambio).group(1)
        if not data:
          return None
        try:
          data_euro = re.search(r'<div id=data>[a-zA-Z\s]*([\d/]+\s[\d:]+)</div>', data).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_euro


class Selic:

    def __init__(self): 
        self.query_url = 'https://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros'
        acesso = AcessarBancoCentral(self.query_url)
        self.req = acesso.getURL()

    def get_selic_meta(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        if not selic:
          return None
        try:
          selic_meta = re.search(r'<div id=ratevalue>(\d*[\.\,]?\d+)</div>', selic).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(selic_meta.replace(',','.'))

    def get_data_selic_meta(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        if not selic:
          return None
        try:
          data_selic_meta = re.search(r'<div=ratedate>([\d/]+)</div>', selic).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_selic_meta

    def get_selic_real(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        if not selic:
          return None
        try:
          selic_real = re.search(r'<div id=dailyratevalue>(\d*[\.\,]?\d+)</div>', selic).group(1)
        except AttributeError:
          return None
        except:
          raise
        return float(selic_real.replace(',','.'))
    
    def get_data_selic_real(self):
        selic = cleanContent(self.req.content.decode('utf-8'))
        if not selic:
          return None
        try:
          data_selic_real = re.search(r'<div id=dailyratedate>([\d/]+)</div>', selic).group(1)
        except AttributeError:
          return None
        except:
          raise
        return data_selic_real
