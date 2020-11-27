from pathlib import Path
from itertools import islice
import io


file = io.open("log.txt", 'w', encoding="utf-8")

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '

def tree(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
         length_limit: int=10000):
    #Given a directory Path object, print a visual tree structure
    dir_path = Path(dir_path)  # accept string coerceable to Path
    files = 0
    directories = 0
    def inner(dir_path: Path, prefix: str='', level=-1):
        nonlocal files, directories
        if not level: 
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in sorted(dir_path.iterdir()) if d.is_dir()]
        else: 
            contents = list(sorted(dir_path.iterdir()))
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            #Remove .directories from selection
            if path.name[0] != "." and path.name != "Robot Stuff - from Liz" and path.name != "ess":
                if path.is_dir():
                    yield prefix + pointer + path.name
                    directories += 1
                    extension = branch if pointer == tee else space 
                    yield from inner(path, prefix=prefix+extension, level=level-1)
                elif not limit_to_directories:
                    info = prefix + pointer + path.name
                    try: 
                        with path.open('r') as f:
                            n_lines = len(f.readlines())
                            loc = f'  LOC: {n_lines}'
                        info += loc
                        #print(info)
                    except UnicodeDecodeError: 
                        pass 
                    yield info
    file.write(dir_path.name + "\n")
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        file.write(line + "\n")
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    file.write(f'\n{directories} directories' + (f', {files} files' if files else ''))


tree('C:/Users/Harry/University of Warwick/STEPHENS, SAM (UG) - ES410 Group Project', limit_to_directories=True)

file.close()

#tree('C:/Users/Harry/Desktop/PythonAdventures')