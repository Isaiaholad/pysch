import sys
import os
import log_config
import logging
from common import flatten_log_msg

from yaml import load as yaml_load
try:
    from yaml import CLoader as YamlLoader
except ImportError:
    from yaml import Loader as YamlLoader

logger = log_config.get_logger(__name__)

class Inventory():

    def __init__(self, inventory_file) -> None:
        # inventory_path = os.path.abspath(inventory_file)
        inventory_path = os.path.expanduser(inventory_file)
        # yaml.
        try:
            with open(inventory_path, 'r') as f:
                self.inventory_dict = yaml_load(f, YamlLoader)
        except Exception as e:
            logger.error(flatten_log_msg(e))
            sys.exit(1)

        self.hosts = []
        self.groups = []
        for item in self.inventory_dict:
            if isinstance(self.inventory_dict[item], dict):
                self.hosts.append(item)
            elif isinstance(self.inventory_dict[item], list):
                self.groups.append(item)

if __name__ == '__main__':
    # inv = Inventory('/Users/ivanb/dev/pyssh/inventory.yaml')
    inv = Inventory('../inventory.yaml')
    # print(inv.groups)

#     from pprint import PrettyPrinter
#     pp = PrettyPrinter(indent=4)
#     pp.pprint(inv.inventory_dict)

#     pp.pprint(inv.inventory_dict['nas'])

#     pp.pprint(inv.groups)
#     pp.pprint(inv.hosts)