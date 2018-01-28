# Banco Central do Brasil

[![PyPI version](https://badge.fury.io/py/bancocentralbrasil.svg?1.1.0)](https://pypi.python.org/pypi/bancocentralbrasil/1.1.0)
[![Build Status](https://travis-ci.org/leogregianin/bancocentralbrasil.svg)](https://travis-ci.org/leogregianin/bancocentralbrasil)
[![codecov](https://codecov.io/gh/leogregianin/bancocentralbrasil/branch/master/graph/badge.svg)](https://codecov.io/gh/leogregianin/bancocentralbrasil) [![github closed issues](https://img.shields.io/github/issues-closed-raw/leogregianin/bancocentralbrasil.svg?style=flat-square)](https://github.com/leogregianin/bancocentralbrasil/issues?q=is%3Aissue+is%3Aclosed)


Sobre
-------

  * Informações sobre taxas oficiais diárias de **Inflação**, **Selic**, **Poupança**, **Dólar** e **Euro** pelo site do Banco Central do Brasil (http://www.bcb.gov.br).
   
Pré requisitos
-------

  * Instalação de qualquer versão do Python (http://www.python.org/download)
  
Instalação das dependências
-------

```bash
$ pip install -r requirements.txt
```

Utilização
-------

```bash
$ python .\sample.py
Inflação Meta: 4.5
Inflação acumulada 12 últimos meses: 2.95
Poupança: 0,3994
Dólar compra: 3,135
Dólar venda: 3,1356
Euro compra: 3,8999
Euro venda: 3,9016
Selic meta: 7
Selic real: 6,9
```

```bash
>>> import bancocentral
>>> inflacao = bancocentral.Inflacao()
>>> print('%s' % inflacao.get_acumulada_tax())
2,95
```

```bash
>>> import bancocentral
>>> selic = bancocentral.Selic()
>>> selic.get_selic_meta()
7
```

Testes unitários
---------

```bash
$ python .\test_bancocentral.py
..................
----------------------------------------------------------------------
Ran 18 tests in 2.243s

OK
```

Licença
-------

[Licença MIT](LICENSE)
