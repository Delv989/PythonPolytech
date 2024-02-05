import json


def task() -> float:
    filename = "input.json"

    with open(filename, 'r') as file:
        json_data = json.load(file)

    values = [item["score"] * item["weight"] for item in json_data]
    return round(sum(values), ndigits=3)


print(task())
