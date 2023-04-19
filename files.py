import sys
import time
import random


import os
import shutil


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/fabur/Downloads"              # Adicione o caminho da sua pasta "Downloads".
to_dir = "C:/Users/fabur/Desktop/arquivos_documentos" # Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo.




dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileEventHandler(FileSystemEventHandler):


    def on_created(self, event):

        print(f"olá, {event.src_path} foi criado!")
    def on_deleted(self, event):

        print(f"Opa! alguem excluiu {event.src_path}!")


        


event_handler = FileEventHandler()

observer = Observer()


observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()


