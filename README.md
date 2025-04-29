# 72 Perguntas Para TDAH

Um simples questionário para ajudar a enfrentar o TDAH.

## Instalação

```bash
git clone git@github.com:kylefelipe/perguntas-tdah.git
cd 72-perguntas-para-tdah
pip install .

# ou usando o Poetry

poetry install
```

## Uso

Para exibir uma pegunta aleatória, use o seguinte comando:

```bash
pergunta-tdah

```

## Opções

- `-h`, `--help`: exibe a ajuda e sai.
- `-q`, `--question-file`: especifica o arquivo de perguntas a ser usado. O padrão é `perguntas_tdah.json`.
- `-l`, `--log-file`: especifica o arquivo de log a ser usado. O padrão é `log.txt`.

## Criando arquivo de perguntas

Pode criar um arquivo de perguntas em formato JSON. O arquivo deve conter uma lista de perguntas, onde cada pergunta é uma string. Exemplo:

```json
[
    "Você tem dificuldade em prestar atenção em detalhes?",
    "Você frequentemente perde coisas necessárias para tarefas e atividades?",
    "Você tem dificuldade em seguir instruções e completar tarefas?"
]
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.
