# Banco Central do Brasil

[![PyPI version](https://badge.fury.io/py/bancocentralbrasil.svg)](https://badge.fury.io/py/bancocentralbrasil)
[![Build Status](https://travis-ci.org/open-bacen/bancocentralbrasil.svg)](https://travis-ci.org/open-bacen/bancocentralbrasil)
[![codecov](https://codecov.io/gh/open-bacen/bancocentralbrasil/branch/master/graph/badge.svg)](https://codecov.io/gh/open-bacen/bancocentralbrasil) 
[![GitHub issues](https://img.shields.io/github/issues/open-bacen/bancocentralbrasil.svg)](https://github.com/open-bacen/bancocentralbrasil/issues)
[![GitHub forks](https://img.shields.io/github/forks/open-bacen/bancocentralbrasil.svg)](https://github.com/open-bacen/bancocentralbrasil/network)
[![GitHub stars](https://img.shields.io/github/stars/open-bacen/bancocentralbrasil.svg)](https://github.com/open-bacen/bancocentralbrasil/stargazers)
[![GitHub license](https://img.shields.io/github/license/open-bacen/bancocentralbrasil.svg)](https://github.com/open-bacen/bancocentralbrasil)


Sobre
-------

  * Informações sobre taxas oficiais diárias de **Inflação**, **Selic**, **Poupança**, **Dólar**, **Dólar PTAX**, **Euro** e **Euro PTAX** pelo site do Banco Central do Brasil (http://www.bcb.gov.br).

Desenvolvimento
-------

 ```sh
$ virtualenv .venv
$ source .venv/bin/activate
```

Instalação das dependências
-------

```bash
$ pip install -r requirements.txt
```

Instalação
-------

```bash
$ ./setup.py install
```

Utilização
-------

```bash
$ python ./sample.py
Inflação Meta: 3.75
Inflação acumulada 12 últimos meses: 5.2
Poupança: 0.1159
Dólar compra PTAX: 5.7443
Dólar venda PTAX: 5.7449
Dólar PTAX em 10/03/2021 16:03:03
Dólar compra: 5.7443
Dólar venda: 5.7449
Dólar em 10/03/2021 16:03:03
Euro compra PTAX: 6.8323
Euro venda PTAX: 6.8353
Euro PTAX em 10/03/2021 16:03:03
Euro compra: 6.8323
Euro venda: 6.8353
Euro em 10/03/2021 16:03:03
Selic meta: 2.0 em 20/01/2021
Selic real: 1.9 em 10/03/2021
```

```bash
>>> from bc.bancocentral import Inflacao
>>> inflacao = Inflacao()
>>> print('%s' % inflacao.get_acumulada_tax())
4.53
```

```bash
>>> from bc.bancocentral import Selic
>>> selic = bancocentral.Selic()
>>> selic.get_selic_meta()
6.5
```

Testes e cobertura
---------

```bash
$ python -m unittest
..............................
----------------------------------------------------------------------
Ran 30 tests in 47.580s

OK
```

```bash
$ python -m coverage run --source=bc tests/test_bancocentral.py
..............................
----------------------------------------------------------------------
Ran 30 tests in 64.135s

OK
```

```bash
$ coverage report
$ coverage html
```


Licença
-------

[Licença MIT](LICENSE)
