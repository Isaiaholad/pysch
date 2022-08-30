import sys
from common import singlton_class, flatten_log_msg

from yaml import load as yaml_load

from common import flatten_log_msg
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
@singlton_class
class Config():

    def __init__(self, filename) -> None:
        self.filename = filename
        try:
            with open(filename, 'r') as f:
                self.conf_dict = yaml_load(f, Loader)
        except Exception as e:
            print(flatten_log_msg(e))
            sys.exit(1)

    def get_node_config(self, node_name) -> dict:
        pass
