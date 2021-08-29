# Pyghub CLI

Pybhub is designed to run from either a Python script or the CLI. By installing the package with `pip`, we can run `pyghub` as if it were a locally installed executable.


## Prerequisites
1. Python 3.* (tested on 3.6 and 3.9) with [pip](https://pip.pypa.io/en/stable/).
1. Windows (tested on Windows 11)
1. Linux (tested on Ubuntu via [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10))

## Installation
Use [virtualenv](https://docs.python.org/3/tutorial/venv.html). Optional, but recommended:
```bash
pip install virtualenv
python -m virtualenv pyghub
pyghub\Scripts\activate.bat  # `source ./pyghub/scripts/activate` for Linux
```
Then...

```bash
# Install pyghub to the 'output' dir
pip install -e . -t output

# Add your project dir to the PYTHONPATH env var
set PYTHONPATH=%PYTHONPATH%;c:\git\pyghub

# Add the output dir to your PATH
set PATH=%PATH%;c:\git\pyghub\output
```

## Usage
pyghub.exe should reside in the directory we added to PYTHONPATH above (output) and can be called like any executable.
```bash
# Clone a repo
pyghub clone_repo -r https://github.com/microsoft/terminal.git -p c:\git\Terminal

# Or just get some information on it (requires a github access token)
set GH_TOKEN=<your github access token>
pyghub get_repo -o Microsoft -r Terminal


```