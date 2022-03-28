import requests
import json
import sys

endpointBase = "https://sm.ms/api/v2/"


def getAPIToken(username: str, password: str) -> list:
    endpoint = endpointBase + "token"
    params = {
        "username": username,
        "password": password,
    }
    r = requests.post(url=endpoint, params=params)
    # write token to one file for module test
    tokenfile = sys.path[0] + "/apitoken.py"
    response = r.json()
    with open(tokenfile, "w") as f:
        content = '{} = "{}"'.format("APIToken", response["data"]["token"])
        f.write(content + "\n")
    return response

    # return json file and save to class
    # return j.json()


def getUserProfile(APIToken: str, ContentType: str = "multipart/form-data") -> list:
    endpoint = endpointBase + "profile"
    headers = {
        "Content-Type": ContentType,
        "Authorization": APIToken,
    }
    r = requests.post(url=endpoint, headers=headers)
    return r.json()


def test():
    print(json.dumps(getAPIToken("cascades", "Chen112203"), indent=4))
    from apitoken import APIToken

    print(json.dumps(getUserProfile(APIToken), indent=4))


if __name__ == "__main__":
    test()
