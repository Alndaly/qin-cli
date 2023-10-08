import os
from typing import Union

class Config:
     def __init__(self) -> None:
        self.USER_HOME = os.path.expanduser("~")
        self.ROOT_PATH = os.path.join(self.USER_HOME, '.qin')
        self.TRASH_PATH = os.path.join(self.ROOT_PATH, 'trash')
        self.CONFIG_PATH = os.path.join(self.ROOT_PATH, 'config.json')
            
config = Config()
