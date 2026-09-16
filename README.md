# Simulador de execução fora de ordem com scoreboard - MO401 - 2s2026

## Executando o Projeto

Antes de iniciar é importante configurar o projeto, isso é feito utilizando o seguinte comando:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Feito isso o sistema pode ser executado com o comando abaixo:

```bash
python -m scoreboard examples/example1.s
```

## Configurações da Arquitetura

Caso queira alterar a quantidade de unidades funcionais ou a quantidade de ciclos que o sistema vai utilizar basta alterar o arquivo `src/utils/arch.py`.

A configuração de unidades funcionais se dá pela variável global `FUNCTION_UNITS`, onde o primeiro valor é o número de unidades funcionais daquele tipo e o segundo é a quantida de ciclos que ela leva para executar a operação.
