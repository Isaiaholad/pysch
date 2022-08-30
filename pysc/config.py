import sys
from common import singlton_class, flatten_log_msg

from yaml import load as yaml_load

from common import flatten_log_msg
from inventory import Inventory
import log_config

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

console_logger = log_config.get_logger('console_logger')
@singlton_class
class Config():

    def __init__(self, filename) -> None:
        self.filename = filename
        try:
            with open(filename, 'r') as f:
                self.conf_dict = yaml_load(f, Loader)
        except Exception as e:
            console_logger.error(flatten_log_msg(e))
            console_logger.error('Exiting')
            sys.exit(1)

        for k, v in self.conf_dict.items():
            setattr(self, k, v)

    @property
    def inventory(self):
        if not hasattr(self, '_inventory'):
            self._inventory = Inventory(self.inventory_file)
        return self._inventory

    def get_node_config(self, node_name) -> dict:
        pass
