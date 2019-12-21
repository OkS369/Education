import requests


with open("dataset_24476_3.txt") as f:
    api_url_1 = "http://numbersapi.com/"
    api_url_2 = "/math?json=true"
    lines = f.readlines()
    ans = []
    for l in lines:
        api_url = api_url_1 + l.strip() + api_url_2
        res = requests.get(api_url)
        if res.json()["found"] is True:
            print("Interesting")
        elif res.json()["found"] is False:
            print("Boring")
