import os
import getpass
from datetime import datetime
from pprint import pprint

from xdo import Xdo
from pymonitor.db import collection


def main():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    # export DISPLAY=:0.0

    xdo = Xdo()
    win_id = xdo.get_active_window()
    win_name = xdo.get_window_name(win_id).decode("utf-8")
    username = getpass.getuser()
    now = datetime.now()

    table = {"window_name": win_name, "datetime": now, "user": username}

    record_id = collection.insert_one(table).inserted_id
    pprint(table)
