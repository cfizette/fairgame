import os
import json
from multiprocessing import Pool
import subprocess


from stores.amazon import AUTOBUY_CONFIG_PATH
# This kills the computer...
if __name__ == "__main__":
    try:
        with open(AUTOBUY_CONFIG_PATH) as f:
            conf = json.load(f)

        processes = []
        for i, c in enumerate(conf["configs"]):
            p = subprocess.Popen("python app.py amazon --test --no-image --p=1 --conf-index={} >> logs/index-logs/{}.log".format(i, i), shell=True)
            processes.append(p)

    except Exception as e:
        print(e)
        for p in processes:
            p.kill

