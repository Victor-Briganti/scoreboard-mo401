from argparse import ArgumentParser

from cpu import Cpu
from utils import parse_assembly
from utils.parser import parse_config


def parse_arg():
    parser = ArgumentParser(description="Simulador do algoritmo de scoreboard.")

    parser.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help="Caminho do arquivo a ser executado",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        required=True,
        help="Arquivo de configuração da arquitetura.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arg()

    parse_config(args.config)

    cpu = Cpu(parse_assembly(args.filepath))
    cpu.start()
    cpu.inst_table.print()
