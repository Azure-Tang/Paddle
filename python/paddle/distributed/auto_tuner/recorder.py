import csv
import os 
<<<<<<< HEAD
from typing import Tuple
=======
>>>>>>> 589ad5fa568283facd0845e68aa52ec14e1badc0
class History_recorder:
    # NOTE increase extenable ablitity
    def __init__(self) -> None:
        self.history = []
        self.store_path = None
<<<<<<< HEAD
        # self.cur_configs = {"dp":1, "mp":1, "pp":1, "sharding_degree":1, "sharding_stage":1, "mbs":1, "recompute":1, "granularity":1, "matrix":0}
        
    def add_cfg(self, **kwargs):
        cur_configs = {}
        for key, val in kwargs.items():
            cur_configs[key] = val
        self.history.append(cur_configs)
=======
        self.cur_configs = {"dp":1, "mp":1, "pp":1, "sharding_degree":1, "sharding_stage":1, "mbs":1, "recompute":1, "granularity":1, "matrix":0}
        
    def add_cfg(self, **kwargs):
        for key, val in kwargs:
            self.cur_configs[key] = val
        self.history.append(self.cur_configs)
>>>>>>> 589ad5fa568283facd0845e68aa52ec14e1badc0
        
    def sort_metric(self, direction, metric_name)-> None:
        if direction == 'Maximize':
            self.history.sort(key=lambda x:x[metric_name], reverse=True)
        else:
            self.history.sort(key=lambda x:x[metric_name])
        return 
    
    def get_best(self, metric, direction)->Tuple[dict, bool]:
        self.sort_metric(direction=direction, metric_name=metric)
        if(len(self.history) == 0):
            return (self.history[0],True)
        return (self.history[0],False)
        
    def store_history(self, path="./history.csv"):
        """Store history to csv file."""
        self.store_path = path
        with open(self.store_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.history[0].keys())
            for row in self.history:
                writer.writerow(row.values())

<<<<<<< HEAD
    def load_history(self, path="./history.csv")->Tuple[list,bool]:
=======
    def load_history(self, path="./history.csv")->tuple(list(dict),bool):
>>>>>>> 589ad5fa568283facd0845e68aa52ec14e1badc0
        """Load history from csv file."""
        err = False
        if(self.store_path is None):
            self.store_path = path
        if not os.path.exists(self.store_path):
            err = True
<<<<<<< HEAD
        else:
            with open(self.store_path, "r") as f:
                reader = csv.reader(f)
                self.history = list(reader)
=======
            return (self.history, True)
        with open(self.store_path, "r") as f:
            reader = csv.reader(f)
            self.history = list(reader)
>>>>>>> 589ad5fa568283facd0845e68aa52ec14e1badc0
        return (self.history, err)