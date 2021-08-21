# Pyghub

Pybhub is a Python library for interfacing with the [Github API](https://docs.github.com/en/rest).


## Prerequisites
1. Python 3.* (tested on 3.6 and 3.9)
2. [Pip](https://pip.pypa.io/en/stable/)
2. Windows (tested in Windows 11)
3. Linux (tested on Ubuntu via [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10))

## Installation

```bash
pip install -r requirements.txt
```

## Testing
```bash
#  Install dev dependencies
pip install -r dev-requirements.txt

#  Linting
python -m pylint pyghub

#  Unit tests
python -m pytest

#  With code coverage
python -m pytest --cov=.
```

## Usage
```python
from pyghub.Github import Github

#  Lists Events
gh = Github("api_key")
gh.GetEvents()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
