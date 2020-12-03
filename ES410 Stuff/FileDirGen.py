import io
from pathlib import Path
from itertools import islice


file = io.open("FileDirectory.txt", 'w', encoding="utf-8")

space =  "    "
branch = "│   "
tee =    "├── "
last =   "└── "

def tree(dir_path: Path, level: int=-1, limit_to_directories: bool=False, MaxLength: int=10000):
    #Given a directory Path object, print a visual tree structure
    dir_path = Path(dir_path)
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
            #Remove .directories from selection (Exclusion/Inclusion List)
            if path.name[0] != "." and path.name != "Robot Stuff - from Liz" and path.name != "ess":
                if path.is_dir():
                    yield prefix + pointer + path.name
                    directories += 1
                    if pointer == tee:
                        extension = branch
                    else:
                        extension = space 
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
    Repeater = inner(dir_path, level=level)

    for line in islice(Repeater, MaxLength):
        file.write(line + "\n")
    if next(Repeater, None):
        print(f'... MaxLength, {MaxLength}, reached, counted:')
    file.write(f'\n{directories} directories' + (f', {files} files' if files else ''))


tree('C:/Users/Harry/University of Warwick/STEPHENS, SAM (UG) - ES410 Group Project', limit_to_directories=True)

file.close()

#tree('C:/Users/Harry/Desktop/PythonAdventures')