import json
import argparse
import os
import random
from datetime import datetime

QUESTIONS_FILE = "./perguntas_tdah.json"


def load_questions(file_path):
    """
    Load questions from a JSON file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    with open(file_path, "r") as file:
        questions = json.load(file)

    return questions


def log_data(question_id, question, question_file, log_file="log.txt"):
    """
    Log data to a file.

    Args:
        - question_id (int): The ID of the question.
        - question (str): The question text.
        - question_file (str): The file from which the question was loaded.
        - log_file (str): The file to which the log will be written.

    Returns:
        - None
    """
    log_file = "log.txt"
    mode = "a" if os.path.exists(log_file) else "w"
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    txt_log = (
        "---------------------------------------------------------------\n"
        if mode == "w"
        else ""
    )
    txt_log += (
        f"Data e Hora: {data_hora}\n"
        f"Arquivo de Perguntas: {question_file}\n"
        f"Pergunta ID: {question_id}\n"
        f"Pergunta: {question}\n"
        "---------------------------------------------------------------\n"
    )
    with open(log_file, mode=mode, encoding="UTF-8") as file:
        file.write(txt_log)


def main():
    parser = argparse.ArgumentParser()
    # modifica o texto do help
    parser.description = (
        "72 Perguntas sobre TDAH para você. "
        "Esse script irá fazer uma pergunta aleatória e registrar a resposta."
    )
    parser.epilog = "Contato: " "kylefelipe@gmail.com"
    parser.add_argument(
        "-q",
        "--question-file",
        type=str,
        default=QUESTIONS_FILE,
        help="Indique o arquivo de perguntas a ser usado.",
    )
    parser.add_argument(
        "-l",
        "--log-file",
        type=str,
        default="log.txt",
        help="Indique o arquivo de log a ser usado.",
    )
    args = parser.parse_args()

    questions = load_questions(args.question_file)
    qt_questions = len(questions)
    question_id = random.randint(0, qt_questions - 1)
    question = questions[question_id]
    print("Aqui está uma pergunta para você:")
    print("---------------------------------------------------------------")
    print(question)
    print("---------------------------------------------------------------")
    print("Lembre-se de anotar no bullet a resposta da pergunta.")
    print("Bye!")
    log_data(
        question_id=question_id,
        question=question,
        question_file=args.question_file,
        log_file=args.log_file,
    )


if __name__ == "__main__":
    main()
