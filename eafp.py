# EAFP
# Easy Ask Fogiveness than permission.
# pt-BR: É melhor pedir perdão do que permissão


class UserNotFoundError(BaseException):
    """Raise exception"""
    pass


def do_something(data):
    return data


def get_user(data):
    return data


try:
    with open("file.txt") as data:
        do_something(data)
except FileNotFoundError:
    print("O arquivo não existe")


try:
    user = get_user("name")
except UserNotFoundError:
    print("User não encontrado.")
except Exception as Error:
    print(f"Erro desconhecido: {str(Error)}")
