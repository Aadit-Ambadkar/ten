from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ten.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ten",
    options = options,
    version = "0.2",
    description = '',
    executables = executables
)