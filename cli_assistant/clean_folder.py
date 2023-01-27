import sys
import shutil
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_",
               "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
def normalize(name):
    return name.translate(TRANS)

extensions = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "music": ['.mp3', '.ogg', '.wav', '.amr'],
    "archives": ['.zip', '.gz', '.tar'],
    "unknown": [""]
}

def create_folders(path: Path):
    for name in extensions.keys():
        if not path.joinpath(name).exists():
            path.joinpath(name).mkdir()

def sort_files(path: Path):
    for file in path.glob("**/*"):
        new_name = file.with_name(normalize(file.stem)).with_suffix(file.suffix)
        if file.is_file():
            if file.suffix in extensions["images"]:
                file.rename(new_name)
                new_name.replace(path / "images" / new_name.name)

            elif file.suffix in extensions["video"]:
                file.rename(new_name)
                new_name.replace(path / "video" / new_name.name)                    

            elif file.suffix in extensions["documents"]:
                file.rename(new_name)
                new_name.replace(path / "documents" / new_name.name)

            elif file.suffix in extensions["music"]:
                file.rename(new_name)
                new_name.replace(path / "music" / new_name.name)

            elif file.suffix in extensions["archives"]:
                file.rename(new_name)
                new_name.replace(path / "archives" / new_name.name)

            else:
                file.rename(new_name)
                new_name.replace(path / "unknown" / new_name.name)


def delete_folders(path: Path):
    for f in list(path.glob("*/**"))[::-1]:
        if f.is_dir:
            try:
                f.rmdir()
            except OSError:
                pass


def unpack_archives(path: Path):
    path_folder = path / "archives"
    for f in path_folder.iterdir():
        shutil.unpack_archive(f, path / "archives" / f.stem)
        
def main():

    path = None
    try:
        path = Path(sys.argv[1])
        print(f'Start sorting files in folder: {path}')
    except IndexError:
        print("Please enter valid path")

    create_folders(path)
    sort_files(path)
    delete_folders(path)
    unpack_archives(path)
    print("Success")
    
if __name__ == "__main__":
    main()