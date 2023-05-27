from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    txt_rows_list = txt_importer(path_file)

    file_for_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_rows_list),
        "linhas_do_arquivo": txt_rows_list
    }

    instance.enqueue(file_for_process)

    print(file_for_process)


def remove(instance):
    response = instance.dequeue()

    if response is None:
        return print('Não há elementos')

    path = response['nome_do_arquivo']

    return print(f'Arquivo {path} removido com sucesso')


def file_metadata(instance, position):
    try:
        response = instance.search(position)
        print(response)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
