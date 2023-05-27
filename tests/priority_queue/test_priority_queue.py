from ting_file_management.priority_queue import PriorityQueue
import pytest

processed_files = [{
        "nome_do_arquivo": "path1/exemple.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "path2/exemple.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "path3/exemple.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "path4/exemple.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "path5/exemple.txt",
        "qtd_linhas": 1,
        "linhas_do_arquivo": []
    }
]


def test_basic_priority_queueing():
    queue_for_test = PriorityQueue()

    for processed_file in processed_files:
        queue_for_test.enqueue(processed_file)

    assert queue_for_test.dequeue() == processed_files[1]
    assert queue_for_test.search(3) == processed_files[2]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue_for_test.search(len(processed_files) + 10)
