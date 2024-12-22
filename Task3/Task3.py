import json

def UpdateValues(data):
    if "value" in data:
        data["value"] = valuesDict.get(data["id"], data["value"])

    if "values" in data:
        for nestedData in data["values"]:
            UpdateValues(nestedData)

with open("values.json", 'r') as json_values:
    values = json.load(json_values)

with open("tests.json", 'r') as json_tests:
    tests = json.load(json_tests)

valuesDict = {item["id"]: item["value"] for item in values["values"]}

for i in tests["tests"]:
    UpdateValues(i)

with open("reports.json", 'w') as json_reports:
    json.dump(tests, json_reports, indent = 2)
