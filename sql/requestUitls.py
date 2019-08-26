
import requests

def doRequest(method, url, datas, jsons, header):
    if method == "get" or method == "GET":
        r = requests.request("get", url, data=datas, json=jsons, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    elif method == "post" or method == "POST":
        r = requests.request("post", url, data=datas, json=jsons, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
