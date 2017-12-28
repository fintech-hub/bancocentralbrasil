#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import re

USER_AGENT = "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"

class Inflacao:

	def __init__(self):
		self.inflacao_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/inflacao"
		self.feed = feedparser.parse(self.inflacao_url, agent=USER_AGENT)

	def get_meta_tax(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				inflacao = item['summary']
				tax = re.search('<div id=label>Meta</div><div id=rate><div id=value>(\d*\,?\d+)</div>', inflacao).group(1)
			return tax
		else: 
			return ("URL error %s" % self.inflacao_url)

	def get_acumulada_tax(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				inflacao = item['summary']
				tax = re.search('<div id=label>Acumulada</div><div id=rate><div id=value>(\d*\,?\d+)</div>', inflacao).group(1)
			return tax
		else: 
			return ("Site error %s" % self.inflacao_url)

class Poupanca:

	def __init__(self):
		self.poupanca_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/poupanca"
		self.feed = feedparser.parse(self.poupanca_url, agent=USER_AGENT)

	def get_poupanca_tax(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				poupanca = item['summary']
				tax = re.search('<div id=value>(\d*\,?\d+)</div>', poupanca).group(1)
			return tax
		else: 
			return ("URL error %s" % self.poupanca_url)

class Dolar:

	def __init__(self):
		self.dolar_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/cambio"
		self.feed = feedparser.parse(self.dolar_url, agent=USER_AGENT)

	def get_dolar_compra(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				title = item['title']
				if re.search('(PTAX)', title) or (re.search('Euro', title)):
					continue
				tax = item['summary']
				compra = re.search('<div id=rate><div id=label>Compra</div><div id=value>(\d*\,?\d+)</div>', tax).group(1)
			
			return compra

		else: 
			return ("URL error %s" % self.dolar_url)

	def get_dolar_venda(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				title = item['title']
				if re.search('(PTAX)', title) or (re.search('Euro', title)):
					continue
				tax = item['summary']
				venda = re.search('<div id=rate><div id=label>Venda</div><div id=value>(\d*\,?\d+)</div>', tax).group(1)
			return venda
		else: 
			return ("Site error %s" % self.dolar_url)

class Selic:

	def __init__(self):
		self.selic_url = "http://conteudo.bcb.gov.br/api/feed/pt-br/PAINEL_INDICADORES/juros"
		self.feed = feedparser.parse(self.selic_url, agent=USER_AGENT)

	def get_selic_meta(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				selic = item['summary']
				selic_meta = re.search('<div id=ratevalue>(\d*\,?\d+)</div>', selic).group(1)
			return selic_meta
		else: 
			return ("Site error %s" % self.selic_url)

	def get_selic_real(self):
		feed = self.feed
		if feed['status'] == 200:
			for item in feed.entries:
				selic = item['summary']
				selic_real = re.search('<div id=dailyratevalue>(\d*\,?\d+)</div>', selic).group(1)
			return selic_real
		else: 
			return ("Site error %s" % self.selic_url)
