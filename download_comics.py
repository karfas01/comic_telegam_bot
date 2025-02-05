import random
import requests


def download_img(img_url, file_name):
    response_img = requests.get(img_url)
    response_img.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response_img.content)


def get_comic(file_name):
    current_url = "https://xkcd.com/info.0.json"
    response = requests.get(current_url)
    response.raise_for_status()
    max_num = response.json()["num"]
    num = random.randint(1, max_num)

    url = f"https://xkcd.com/{num}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()

    download_img(response.json()["img"], file_name)
