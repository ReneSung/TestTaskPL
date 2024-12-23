import sys
import json

def UpdateValues(data):
    if "value" in data:
        data["value"] = valuesDict.get(data["id"], data["value"])

    if "values" in data:
        for nestedData in data["values"]:
            UpdateValues(nestedData)


files = sys.argv

valuesJson = files[1]
testsJson = files[2]
reportsJson = files[3]

with open(valuesJson, 'r') as json_values:
    values = json.load(json_values)

with open(testsJson, 'r') as json_tests:
    tests = json.load(json_tests)

valuesDict = {item["id"]: item["value"] for item in values["values"]}

for i in tests["tests"]:
    UpdateValues(i)

with open(reportsJson, 'w') as json_reports:
    json.dump(tests, json_reports, indent = 2)
