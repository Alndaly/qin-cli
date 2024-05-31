import json
from .base import CONFIG_PATH
from ..common.file import read_file

def load_config():
    config_str = read_file(CONFIG_PATH)
    config = json.loads(config_str)
    return config

class Config(dict):
    def __init__(self, d=None):
        super().__init__()
        for k, v in d.items():
            self[k] = v
    
    def __getitem__(self, key):
        return super().__getitem__(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError as e:
            return default
        except Exception as e:
            raise e

config = Config(load_config())
