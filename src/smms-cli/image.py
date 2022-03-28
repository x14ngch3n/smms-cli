import requests
import json

endpointBase = "https://sm.ms/api/v2/"


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
        history.append(response)
        # encounter the last page
        if response["CurrentPage"] == response["TotalPages"]:
            break

    return history


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
    from apitoken import APIToken

    # print(json.dumps(getUploadHistoryByIP(), indent=4))
    # print(json.dumps(clearUploadHistoryByIP(), indent=4))
    # print(json.dumps(deleteImage("AdRvXkFcSLiDyHh41ZI2zpP8UM"), indent=4))
    # print(json.dumps(getUploadHistory(), indent=4))
    print(json.dumps(uploadImage("tests/avatar.jpeg", APIToken), indent=4))


if __name__ == "__main__":
    test()
