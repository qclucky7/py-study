import requests

if __name__ == '__main__':

    response: requests.Response = requests.get("https://www.baidu.com")

    print(response.content)
    print(response.text)
    print(response.ok)
    print(response.status_code)
    print(response.headers)
    print(response.reason)
