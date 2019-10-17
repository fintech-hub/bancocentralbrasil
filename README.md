# Banco Central do Brasil

[![PyPI version](https://badge.fury.io/py/bancocentralbrasil.svg)](https://badge.fury.io/py/bancocentralbrasil)
[![Build Status](https://travis-ci.org/leogregianin/bancocentralbrasil.svg)](https://travis-ci.org/leogregianin/bancocentralbrasil)
[![codecov](https://codecov.io/gh/leogregianin/bancocentralbrasil/branch/master/graph/badge.svg)](https://codecov.io/gh/leogregianin/bancocentralbrasil) [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fleogregianin%2Fbancocentralbrasil.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fleogregianin%2Fbancocentralbrasil?ref=badge_shield)

[![GitHub issues](https://img.shields.io/github/issues/leogregianin/bancocentralbrasil.svg)](https://github.com/leogregianin/bancocentralbrasil/issues)
[![GitHub forks](https://img.shields.io/github/forks/leogregianin/bancocentralbrasil.svg)](https://github.com/leogregianin/bancocentralbrasil/network)
[![GitHub stars](https://img.shields.io/github/stars/leogregianin/bancocentralbrasil.svg)](https://github.com/leogregianin/bancocentralbrasil/stargazers)
[![GitHub license](https://img.shields.io/github/license/leogregianin/bancocentralbrasil.svg)](https://github.com/leogregianin/bancocentralbrasil)


Sobre
-------

  * Informações sobre taxas oficiais diárias de **Inflação**, **Selic**, **Poupança**, **Dólar**, **Dólar PTAX**, **Euro** e **Euro PTAX** pelo site do Banco Central do Brasil (http://www.bcb.gov.br).
   
Pré requisitos
-------

  * Instalação da versão do Python (http://www.python.org/download) preferencialmente 3.4 ou 3.6. 
  
Instalação das dependências
-------

```bash
$ pip install -r requirements.txt
```

Utilização
-------

```bash
$ python .\sample.py
Inflação Meta: 4.0
Inflação acumulada 12 últimos meses: 4.53
Poupança: 0.3715
Dólar compra PTAX: 3.7326
Dólar venda PTAX: 3.7332
Dólar compra: 3.7234
Dólar venda: 3.724
Euro compra PTAX: 4.3276
Euro venda PTAX: 4.3286
Euro compra: 4.3169
Euro venda: 4.318
Selic meta: 6.5
Selic real: 6.4
```

```bash
>>> import bancocentral
>>> inflacao = bancocentral.Inflacao()
>>> print('%s' % inflacao.get_acumulada_tax())
4.53
```

```bash
>>> import bancocentral
>>> selic = bancocentral.Selic()
>>> selic.get_selic_meta()
6.5
```

Testes unitários
---------

```bash
$ python .\test_bancocentral.py
..............................
----------------------------------------------------------------------
Ran 30 tests in 47.580s

OK
```

Licença
-------

[Licença MIT](LICENSE)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fleogregianin%2Fbancocentralbrasil.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fleogregianin%2Fbancocentralbrasil?ref=badge_large)