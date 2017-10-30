import glob
import os
import json
import re


read_files = glob.glob(os.path.join(os.getcwd(), "Document", "*"))
for f in read_files:
    with open (f) as f_input:
        next(f_input)
        next(f_input)
        next(f_input)
        contents = f_input.read()
        contents = re.sub('-1', '', contents)
        record = [f, contents]
        print(json.dumps(record))
