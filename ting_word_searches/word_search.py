def exists_word(word, instance):
    response = []

    for position_on_queue in range(len(instance)):
        file = instance.search(position_on_queue)

        possible_occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for row_index, row in enumerate(file["linhas_do_arquivo"], 1):
            if word.lower() in row.lower():
                possible_occurrences["ocorrencias"].append({
                    "linha": row_index
                })

        if possible_occurrences["ocorrencias"]:
            response.append(possible_occurrences)

    return response


def search_by_word(word, instance):
    response = []

    for position_on_queue in range(len(instance)):
        file = instance.search(position_on_queue)

        possible_occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for row_index, row in enumerate(file["linhas_do_arquivo"], 1):
            if word.lower() in row.lower():
                possible_occurrences["ocorrencias"].append({
                    "linha": row_index,
                    "conteudo": row
                })

        if possible_occurrences["ocorrencias"]:
            response.append(possible_occurrences)

    return response
