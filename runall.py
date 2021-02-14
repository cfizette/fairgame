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
            f =  open("logs/index-logs/{}.log".format(i), "w")
            p = subprocess.Popen("python app.py amazon --no-image --p=1 --conf-index=3 --headless >> logs/index-logs/{}.log".format(i, i), shell=True, stdout=f)
            #p.communicate()
            processes.append(p)
            break

        while any([p.poll() is None for p in processes]):
            continue
        print("all processess exited")


    except Exception as e:
        print(e)
        for p in processes:
            p.kill

