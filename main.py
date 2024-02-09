import argparse
from pathlib import Path
import logging
from threading import Thread
from shutil import copyfile
import time

parser = argparse.ArgumentParser(description='Sorting file')
parser.add_argument('--source', '-s', help='Source file', required=True)
parser.add_argument('--output', '-o', help='Output file', default='finish_sorted')

args = vars(parser.parse_args())

source = Path(args.get('source'))
output = Path(args.get('output'))

folders = []


def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            sort_file(el)


def copy_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            logging.info(f"Найденные файлы: # {el}")
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
                logging.info(f"Скопированные файлы: ::::: {el}")
            except OSError as err:
                logging.error(err)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')

    folders.append(source)
    sort_file(source)
    print(f"Поиск файлов будет в этих катологах: {folders}\n")

    threads = []

    start = time.time()
    for folder in folders:
        th = Thread(target=copy_file, args=(folder, ))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    end = time.time()
    execution_time = end - start
    print("Время выполнения:", execution_time, "секунд\n")
    print(f"Файлы из папки: {source}  #ОТСОРТИРОВАНЫ\n")
