import subprocess
from datetime import datetime

def auto_commit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Auto commit: {timestamp}"], check=True)
    subprocess.run(["git", "push"], check=True)

    print("\nAlterações enviadas para o repositório!\n")

if __name__ == "__main__":
    input("Pressione Enter após salvar o arquivo para enviar o commit: ")
    auto_commit()