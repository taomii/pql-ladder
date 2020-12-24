from dataclasses import dataclass
from logging import Logger
from  configparser import ConfigParser

@dataclass
class Context:
    logger: Logger
    config: ConfigParser