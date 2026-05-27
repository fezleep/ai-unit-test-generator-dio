from pathlib import Path


def read_python_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"arquivo nao encontrado: {file_path}")

    if path.suffix != ".py":
        raise ValueError("o arquivo precisa ser um .py")

    return path.read_text(encoding="utf-8")


def save_test_file(output_dir, source_file, content):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    source_path = Path(source_file)
    test_file = output_path / f"test_{source_path.stem}.py"
    test_file.write_text(content.strip() + "\n", encoding="utf-8")

    return test_file
