#!/usr/bin/env python3

import sys
import json
from google.protobuf import json_format
from generated import types_pb2, level_pb2

def main():
	if len(sys.argv) < 3:
		print('python3 Convert.py input.* output.*')
		return

	if sys.argv[1].endswith(".level") and sys.argv[2].endswith(".json"):
		levelData = {}
		with open(sys.argv[1], 'rb') as inputFile:
			level = level_pb2.Level()
			level.ParseFromString(inputFile.read())
			levelData = json_format.MessageToDict(level)

		with open(sys.argv[2], "w") as outputFile:
			outputFile.write(json.dumps(levelData, sort_keys=True, indent=4))


	elif sys.argv[1].endswith(".json") and sys.argv[2].endswith(".level"):
		level = level_pb2.Level()
		with open(sys.argv[1], 'r') as inputFile:
			json_format.Parse(inputFile.read(), level)

		with open(sys.argv[2], "wb") as outputFile:
			outputFile.write(level.SerializeToString())


if __name__ == '__main__':
	main()
