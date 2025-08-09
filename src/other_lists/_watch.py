import time
import subprocess
import os
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    def __init__(self, file_to_watch):
        self.FILE_TO_WATCH = os.path.abspath(file_to_watch)
        self.event_handler = Handler(self.FILE_TO_WATCH)
        self.observer = Observer()

    def run(self):
        directory_to_watch = os.path.dirname(self.FILE_TO_WATCH)
        self.observer.schedule(self.event_handler, directory_to_watch, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, file_to_watch):
        self.file_to_watch = file_to_watch

    def on_modified(self, event):
        if event.src_path == self.file_to_watch:
            os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal
            subprocess.run(["python", self.file_to_watch])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Watch a Python file for changes and run it automatically."
    )
    parser.add_argument("filename", type=str, help="The Python file to watch")
    args = parser.parse_args()

    watcher = Watcher(args.filename)
    watcher.run()
