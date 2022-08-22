import sys

from cx_Freeze import setup, Executable

build_exe_options ={
  "packages": ["os", "pandas"]
}

base = None

if sys.platform == "win32":
  base = "Win32GUI"
  
setup(
name="trial",
version="1.0",
options={"build_exe":build_exe_options},
executables=[Executable("trial.py")]
)
