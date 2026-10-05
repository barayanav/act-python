import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("add", type=str, help="add a task with title, priority and creation date")
args = parser.parse_args()
print(json.dumps(args.add))

with open("list.json", mode="w", encoding="utf-8") as write_file:
    json.dump(args.add, write_file)
