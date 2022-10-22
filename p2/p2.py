import os
import json

data = {}


def outputData():
    global data
    print(json.dumps(data, indent=2))


def saveData():
    global data
    with open("data.json", "w") as f:
        json.dump(data, f)


def loadData():
    global data
    if os.path.exists("data.json"):
        with open("data.json") as f:
            data = json.load(f)


while True:
    loadData()
    print()
    print("1. Add element")
    print("2. Output by key")
    print("3. Output all")
    try:
        ch = int(input("> "))
    except KeyboardInterrupt:
        exit()
    except:
        continue

    if ch == 1:
        data[input("key=")] = input("value=")

    elif ch == 2:
        key = input("key=")
        print(key, data[key])

    elif ch == 3:
        outputData()

    saveData()
