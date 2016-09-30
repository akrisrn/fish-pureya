import os
import sys
import re

from extract import extract

support_type = "zip|rar|tar.gz|tar.bz2|tar.xz"

if len(sys.argv) < 2:
    print("[Error]Need a file name")
    sys.exit(1)

file_name = sys.argv[1]
if not os.path.exists(file_name):
    print("[Error]Not such a file")
    sys.exit(1)

target_dir = "."
if len(sys.argv) > 2:
    target_dir = sys.argv[2]

pattern = re.compile(".+\.(" + support_type + ")$")
match = pattern.match(file_name)
if match:
    file_type = match.group(1)
    extract(file_name, target_dir, file_type)
else:
    print("[Error]Not support file type")
    sys.exit(1)
