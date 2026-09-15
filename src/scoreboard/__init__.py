from tables import FunctionalStatus
from tables import RegisterResult


def main() -> None:
    print("Resultado dos Registradores")
    reg = RegisterResult()
    reg.print()

    print("Unidade Funcional")
    func = FunctionalStatus()
    func.print()
