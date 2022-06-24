import os

def get_local_terminal_size():
    """"""
    term_size = os.get_terminal_size()
    return term_size.columns, term_size.lines

def get_local_terminal_type():
    return os.getenv('TERM')