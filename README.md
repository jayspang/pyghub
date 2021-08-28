# Pyghub

Pybhub is a Python library for interfacing with the [Github API](https://docs.github.com/en/rest).


## Prerequisites
1. Python 3.* (tested on 3.6 and 3.9) with [pip](https://pip.pypa.io/en/stable/).
1. Windows (tested on Windows 11)
1. Linux (tested on Ubuntu via [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10))

## Installation
Use [virtualenv](https://docs.python.org/3/tutorial/venv.html). Optional, but recommended:
```bash
pip install virtualenv
python -m virtualenv pyghub
pyghub\Scripts\activate.bat  # `source ./pyghub/bin/activate` for Linux
```
Then...

```bash
pip install -r requirements.txt

set GH_TOKEN=<github personal access token>
python -m pyghub.cli get_repo -o Microsoft -r Terminal
```

## Usage
### From the Command Line:
To invoke Pyghub directly from a command line, see [CLI.md](CLI.md).

### As a Python Module
```python
from pyghub.providers.github import Github
from pyghub.providers.git import Git

# Get Repo information for https://github.com/microsoft/terminal
gh = Github("api_key")
info = gh.get_repo("microsoft", "terminal")

# Clone the same repo to c:\git\terminal
g = Git()
g.clone_repo("https://github.com/microsoft/terminal", "c:\\git\\terminal")

# Pull, push
g.pull("c:\\git\\terminal", "origin", "main")
g.push("https://username:api_token@github.com/microsoft/terminal", "origin", "main") # note the credentials required for pushing)

```


## Testing
```bash
#  Install dev dependencies
pip install -r dev-requirements.txt

#  Linting
python -m pylint pyghub

#  Unit tests (with code coverage)
python -m pytest --cov
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
