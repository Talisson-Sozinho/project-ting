from os import path
import sys


def txt_importer(path_file):
    extension = path.splitext(path_file)[1]

    if extension != '.txt':
        return print('Formato inválido', file=sys.stderr)

    try:
        with open(path_file) as file:
            return [row for row in file.read().split('\n')]

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
