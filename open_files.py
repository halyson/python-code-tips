# Abrir arquivos de forma segura


def do_something(data):
    return data


# USAR O CLOSE
data = open("file.txt")
do_something(data)
data.close()

# OU USAR GERENCIADO DE CONTEXTO, fecha o arquivo sozinho no final
try:
    with open("file.txt") as data:
        do_something(data)
except FileNotFoundError:
    print("O arquivo não existe")

