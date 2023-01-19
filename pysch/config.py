import sys
import os.path
from .common import singlton_class, flatten_log_msg

from yaml import load as yaml_load

# from .inventory import Inventory
from .log_config import get_logger

try:
    # from yaml import CLoader as Loader, CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    # from yaml import Loader, Dumper
    from yaml import Loader

console_logger = get_logger('console_logger')


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

        for fname in (
            'inventory_file',
            'keepass_db_file',
            'keepass_key_file'
        ):
            if fname not in self.conf_dict.keys():
                console_logger.error(
                    '{} is not configured. Exiting.'.format(fname)
                )
                sys.exit(1)

        for k, v in self.conf_dict.items():
            setattr(self, k, v)

        for fname in (
            self.inventory_file,
            self.keepass_db_file,
            self.keepass_key_file
        ):
            if not os.path.exists(fname):
                console_logger.error(
                    'File {} not found. Exiting'.format(fname)
                )
                sys.exit(1)

    # @property
    # def inventory(self):
    #     if not hasattr(self, '_inventory'):
    #         self._inventory = Inventory(self.inventory_file)
    #     return self._inventory

    def get_node_config(self, node_name) -> dict:
        pass
