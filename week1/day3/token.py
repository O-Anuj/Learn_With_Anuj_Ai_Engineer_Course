import subprocess
import sys
from pathlib import Path


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    venv_python = project_dir / ".venv" / "Scripts" / "python.exe"
    groq_chat = project_dir / "groq_chat.py"

    if not venv_python.exists():
        raise FileNotFoundError(f"Missing venv interpreter: {venv_python}")

    subprocess.run(
        [
            str(venv_python),
            "-c",
            f"import runpy; runpy.run_path(r'{groq_chat}')",
        ],
        cwd=str(project_dir.parent),
        check=True,
    )


if __name__ == "__main__":
    main()