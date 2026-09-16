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
    parser.add_argument(
        "-p",
        "--print",
        nargs="?",
        const="all",
        default=None,
        choices=["all", "final"],
        dest="debug_print",
        help="Imprime as tabelas de registradores, unidades funcionais e instruções. "
    )
    parser.add_argument(
        "-s",
        "--stop-cycle",
        type=int,
        default=None,
        dest="stop_cycle",
        help="Ciclo em que a execução deve parar.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arg()

    parse_config(args.config)

    cpu = Cpu(parse_assembly(args.filepath))
    cpu.start(
        debug_print=args.debug_print,
        stop_cycle=args.stop_cycle,
    )
    cpu.inst_table.print()
