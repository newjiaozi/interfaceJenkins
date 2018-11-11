#coding=utf-8
import requests

def searchBaiDu(sk):
    params = {"wd":sk}
    resp = requests.get("http://www.baidu.com/s",params=params)
    if resp.ok:
        assert sk in resp.text
        print("SUCCESS")
    else:
        print("CHECK NOTHING")

if __name__ == "__main__":
    searchBaiDu("jmeter")
    searchBaiDu("jenkins")
