import requests, json, time

all_projects = [970573744]
while True:
    for project in all_projects:
        r = [{"user": "hi", "value": 22}]

        print(r)

        for i in r:

            with open("coins.json", "w") as f:
                time.pause(0.2)
                file = i
                file[i["user"]] = i["value"]
                f.write(str(file))
                


                