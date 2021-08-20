# Banco Central do Brasil

[![bancocentralbrasil](https://github.com/open-bacen/bancocentralbrasil/actions/workflows/main.yml/badge.svg)](https://github.com/open-bacen/bancocentralbrasil/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/open-bacen/bancocentralbrasil/branch/main/graph/badge.svg)](https://codecov.io/gh/open-bacen/bancocentralbrasil) 


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
nflação Meta: 3.75
Inflação acumulada 12 últimos meses: 8.99
Poupança: 0.3012
Dólar compra PTAX: 5.4174
Dólar venda PTAX: 5.418
Dólar PTAX em 19/08/2021 16:07:17
Dólar compra: 5.4174
Dólar venda: 5.418
Dólar em 19/08/2021 16:07:17
Euro compra PTAX: 6.3335
Euro venda PTAX: 6.3364
Euro PTAX em 19/08/2021 16:07:17
Euro compra: 6.3335
Euro venda: 6.3364
Euro em 19/08/2021 16:07:17
Selic meta: 5.25 em 04/08/2021
Selic real: 5.15 em 19/08/2021
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
