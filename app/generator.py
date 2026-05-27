import argparse
from pathlib import Path

from app.mock_llm import MockLLM
from app.prompts import build_test_generation_prompt
from app.utils import read_python_file, save_test_file


def generate_tests(source_file, output_dir="generated_tests", llm=None):
    source_code = read_python_file(source_file)
    file_name = Path(source_file).name
    prompt = build_test_generation_prompt(file_name, source_code)

    llm = llm or MockLLM()
    test_code = llm.invoke(prompt)

    return save_test_file(output_dir, source_file, test_code)


def main():
    parser = argparse.ArgumentParser(
        description="gera testes pytest para um arquivo python usando um mock llm local"
    )
    parser.add_argument("source_file", help="caminho do arquivo python que sera lido")
    parser.add_argument(
        "--output-dir",
        default="generated_tests",
        help="pasta onde o arquivo de teste sera salvo",
    )

    args = parser.parse_args()
    test_file = generate_tests(args.source_file, args.output_dir)
    print(f"teste gerado em: {test_file}")


if __name__ == "__main__":
    main()
