# import subprocess
# cmd = ["dir"]
# out = subprocess.run(cmd, capture_output=True, text=True, shell=True)
# if out.returncode != 0:
#     print("Failed")
# print(out.stdout)

import os

files = os.listdir('.')
for f in files:
    print(f)