import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Configuração do handler para monitorar mudanças nos arquivos
class GitAutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return  # Ignorar mudanças em diretórios
        
        print(f"Arquivo modificado: {event.src_path}")

        # Comandos do Git para commit e push automáticos
        subprocess.run(["git", "add", "."], check=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "commit", "-m", f"auto.commit_atualizado em {timestamp}"], check=True)
        subprocess.run(["git", "push"], check=True)
        
        print("Alterações enviadas para o repositório remoto!")

# Diretório que será monitorado
DIRECTORY_TO_WATCH = "."

# Inicializa o observer
observer = Observer()
event_handler = GitAutoCommitHandler()
observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)

print("Monitorando arquivos... Pressione Ctrl+C para sair.")

try:
    observer.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("Monitoramento encerrado.")

observer.join()


