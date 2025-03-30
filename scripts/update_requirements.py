import subprocess
from pathlib import Path

# Define o caminho para a raiz do projeto (uma pasta acima do script)
root_dir = Path(__file__).resolve().parent.parent
requirements_path = root_dir / "requirements.txt"

# Executa pip freeze e filtra linhas com "@ file:"
result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)

# Escreve o arquivo na raiz
with requirements_path.open("w") as f:
    for line in result.stdout.splitlines():
        if "@ file:" not in line:
            f.write(line + "\n")

# Adiciona o arquivo ao git
subprocess.run(["git", "add", str(requirements_path)])
