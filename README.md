this is the project records some common basics of python language and pkgs

### topics
* math
* thread, threadpool
* db, dbpool
* oop & class
* file
* exceptions
* logging
* compile/decompile
* others

## others
### sys.path
* set by command line
```sh
# for unix
PYTHONPATH=project_path python somescript.py somecommand

# for windows
## sys_path.bat
@ECHO OFF
setlocal
set PYTHONPATH=%1
python %2 %3
endlocal
## cmd
pythonpath.bat project_path somescript.py somecommand
```
* set in .py(recommended)
```py
import sys
sys.path.append('project_path')
```
