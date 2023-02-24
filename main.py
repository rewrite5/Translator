import requests
from dataEntry import DataEntry


def main():

    url = "https://api-b2b.backenster.com/b1/api/v3/translate"
    root = DataEntry.menu(None)
    data = DataEntry.paragraphs(None)
    to = DataEntry.menu(None)


    payload = {
        "translateMode": "html",
        "platform": "api",
        "from": root,
        "to": to,
        "data": data
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "a_TcMxJPBG6QwND7OhvjmMwk2OCxpKoPZJqQE3flfOS9J1CVFbhxQgeq3ggc1hI53bajCEGxUJQ7E7EjEG"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)

    if response.status_code == 200:
        translations = response.json()
        print(f'the translation of {root} --> {to}:',translations['result'])

    else:
        print(f"The following error has occurred: {response.status_code}")

if __name__ == '__main__':
    main()

