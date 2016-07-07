#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import re

class Inflacao:

	def __init__(self):

		inflacao_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/inflacao"
		self.feed = feedparser.parse(inflacao_url)

	def get_meta_tax(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				inflacao = item['summary']
				tax = re.search('<div id=label>Meta</div><div id=rate><div id=value>(\d+,\d+)</div>', inflacao).group(1)
			return tax
		else: 
			return ("Site error %s" % inflacao_url)

	def get_acumulada_tax(self):
		
		feed = self.feed
		
		if feed['status'] == 200:
			for item in feed.entries:
				inflacao = item['summary']
				tax = re.search('<div id=label>Acumulada</div><div id=rate><div id=value>(\d+,\d+)</div>', inflacao).group(1)
			return tax
		else: 
			return ("Site error %s" % inflacao_url)

class Poupanca:

	def __init__(self):

		poupanca_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca"
		self.feed = feedparser.parse(poupanca_url)

	def get_poupanca_tax(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				poupanca = item['summary']
				tax = re.search('<div id=value>(\d+,\d+)</div>', poupanca).group(1)
			return tax
		else: 
			return ("Site error %s" % poupanca_url)

class Dolar:

	def __init__(self):

		dolar_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio"
		self.feed = feedparser.parse(dolar_url)

	def get_dolar_compra(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				title = item['title']
				if re.search('(PTAX)', title) or (re.search('Euro', title)):
					continue
				tax = item['summary']
				compra = re.search('<div id=rate><div id=label>Compra</div><div id=value>(\d+,\d+)</div>', tax).group(1)
			
			return compra

		else: 
			return ("Site error %s" % dolar_url)

	def get_dolar_venda(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				title = item['title']
				if re.search('(PTAX)', title) or (re.search('Euro', title)):
					continue
				tax = item['summary']
				venda = re.search('<div id=rate><div id=label>Venda</div><div id=value>(\d+,\d+)</div>', tax).group(1)
			return venda
		else: 
			return ("Site error %s" % dolar_url)

class Selic:

	def __init__(self):

		selic_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros"
		self.feed = feedparser.parse(selic_url)

	def get_selic_meta(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				selic = item['summary']
				selic_meta = re.search('<div id=label>Meta:</div><div id=rate><div id=ratevalue>(\d+,\d+)</div>', selic).group(1)
			return selic_meta
		else: 
			return ("Site error %s" % selic_url)

	def get_selic_real(self):

		feed = self.feed

		if feed['status'] == 200:
			for item in feed.entries:
				selic = item['summary']
				selic_real = re.search('<div id=dailyrate><div id=dailyratevalue>(\d+,\d+)</div>', selic).group(1)
			return selic_real
		else: 
			return ("Site error %s" % selic_url)

if __name__ == '__main__':

	infl = Inflacao()
	print('Inflacao Meta: %s' % infl.get_meta_tax())
	print('Inflacao acumulada 12 ultimos meses: %s' % infl.get_acumulada_tax())

	poup = Poupanca()
	print('Poupanca: %s' % poup.get_poupanca_tax())

	dolar = Dolar()
	print('Dolar compra: %s' % dolar.get_dolar_compra())
	print('Dolar venda: %s' % dolar.get_dolar_venda())

	selic = Selic()
	print('Selic meta: %s' % selic.get_selic_meta())
	print('Selic real: %s' % selic.get_selic_real())
