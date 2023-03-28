import pathlib

from threatexchange.cli.cli_config import CliState
from threatexchange.cli.main import _get_settings
from flask import Flask

app = Flask(__name__)

config = CliState([], pathlib.Path("~/.threatexchange")).get_persistent_config()
settings, _ = _get_settings(config, pathlib.Path("~/.threatexchange"))


from threatexchange.api import routes