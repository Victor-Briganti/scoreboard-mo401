# Simulador de execução fora de ordem com scoreboard - MO401 - 2s2026

## Executando o Projeto

Antes de iniciar, é necessário preparar o ambiente virtual e instalar o projeto. Para isso os comandos abaixo são necessários:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .

```

O simulador pode ser executado chamando o módulo principal:

```bash
python -m scoreboard -c configs/config01.conf -f examples/example01.s

```

A aplicação exige a passagem de duas *flags* obrigatórias durante a execução:

- `-c`: Define o caminho do arquivo de configuração (disponíveis no diretório `configs/`).
- `-f`: Define o caminho do arquivo de entrada (disponíveis no diretório `examples/`).

## Saídas Esperadas

Os resultados esperados pela aplicação estão sendo salvos no diretório `outputs/` e organizados em subdiretórios baseados na configuração utilizada. Por exemplo, o diretório `outputs/config01/` armazena as execuções de todos os exemplos que rodaram sob o arquivo `config01`.

Os nomes dos arquivos de saída refletem diretamente as suas entradas. Sendo assim, a entrada `example01.s` gera o resultado `output01.md`, o `example02.s` gera o `output02.md`, e assim por diante.
