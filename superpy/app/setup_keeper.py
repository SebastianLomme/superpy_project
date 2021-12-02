import os
from app.variable import current_path_files, current_path_today, current_path_bought
from app.bought_keeper import Bought_keeper


class Setup_keeper:
    def first_run(self):
        if not os.path.exists(current_path_files):
            os.mkdir(current_path_files)
        if not os.path.exists(current_path_bought):
            Bought_keeper(current_path_bought).write_bought_file()
