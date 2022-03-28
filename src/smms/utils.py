import requests

endpointBase = "https://sm.ms/api/v2/"


def getAPIToken(username: str, password: str) -> list:
    endpoint = endpointBase + "token"
    params = {
        "username": username,
        "password": password,
    }
    r = requests.post(url=endpoint, params=params)

    # write token to one file for module test
    modulePath = "/".join(__file__.split("/")[:-1])
    tokenfile = modulePath + "/apitoken.py"
    response = r.json()
    with open(tokenfile, "w") as f:
        content = '{} = "{}"'.format("APIToken", response["data"]["token"])
        f.write(content + "\n")
    return response


def getUserProfile(APIToken: str, ContentType: str = "multipart/form-data") -> list:
    endpoint = endpointBase + "profile"
    headers = {
        "Content-Type": ContentType,
        "Authorization": APIToken,
    }
    r = requests.post(url=endpoint, headers=headers)
    return r.json()


def getUploadHistoryByIP(APIToken: str, format: str = "json") -> list:
    endpoint = endpointBase + "history"
    headers = {
        "Authorization": APIToken,
    }
    params = {"format": format}
    r = requests.get(url=endpoint, params=params, headers=headers)
    return r.json()


def clearUploadHistoryByIP(APIToken: str, format: str = "json") -> list:
    endpoint = endpointBase + "clear"
    headers = {
        "Authorization": APIToken,
    }
    params = {"format": format}
    r = requests.get(url=endpoint, params=params, headers=headers)
    return r.json()


def deleteImage(hash: str, format: str = "json") -> list:
    endpoint = endpointBase + "delete/"
    endpoint += hash
    r = requests.get(url=endpoint)
    return r.json()


def getUploadHistory(APIToken: str, ContentType: str = "multipart/form-data") -> list:
    import itertools
    import json

    history = json.loads("[]")
    endpoint = endpointBase + "upload_history"
    headers = {
        "Authorization": APIToken,
        "Content-Type": ContentType,
    }
    # try access as more pages as possible
    for page in itertools.count(1):
        params = {"page": page}
        r = requests.get(url=endpoint, params=params, headers=headers)
        response = r.json()
        history.append(response["data"])
        # encounter the last page
        if response["CurrentPage"] == response["TotalPages"]:
            break
    # return flattened json, elements are image
    return [item for sublist in history for item in sublist]


def uploadImage(
    filename: str,
    APIToken: str,
    format: str = "json",
) -> list:
    endpoint = endpointBase + "upload"
    headers = {"Authorization": APIToken}
    params = {"format": format}
    files = {"smfile": open(filename, "rb")}
    r = requests.post(url=endpoint, headers=headers, params=params, files=files)
    return r.json()


def test():
    import json
    from apitoken import APIToken

    print(json.dumps(getAPIToken("cascades", "Chen112203"), indent=4))
    print(json.dumps(getUserProfile(APIToken), indent=4))
    print(json.dumps(getUploadHistoryByIP(), indent=4))
    print(json.dumps(clearUploadHistoryByIP(), indent=4))
    print(json.dumps(deleteImage("AdRvXkFcSLiDyHh41ZI2zpP8UM"), indent=4))
    print(json.dumps(getUploadHistory(), indent=4))
    print(json.dumps(uploadImage("tests/avatar.jpeg", APIToken), indent=4))


if __name__ == "__main__":
    test()
