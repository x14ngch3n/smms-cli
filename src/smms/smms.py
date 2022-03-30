from smms import utils


class Client:
    def __init__(self):
        try:
            from smms.apitoken import APIToken

            self.APIToken = APIToken
        except ImportError:
            import getpass

            print(
                "sm.ms-cli needs username and password to get APIToken(for first time use)"
            )
            username = input("Please input your username: ")
            password = getpass.getpass("Please input your password: ")
            response = utils.getAPIToken(username, password)
            self.APIToken = response["data"]["token"]
            self.betterPrint(response)

    def betterPrint(self, json_data):
        from pygments import highlight, lexers, formatters
        import json

        json_raw = json.dumps(json_data, indent=4)
        print(highlight(json_raw, lexers.JsonLexer(), formatters.TerminalFormatter()))

    def extractUrl(self, response: list) -> str:
        # upload first time
        if response["success"]:
            return response["data"]["url"]
        # uploaded before
        else:
            return response["images"]

    def uploadImage(self, filename: str, output: str):
        response = utils.uploadImage(filename, self.APIToken)
        if output == "json" or not output:
            self.betterPrint(response)
        else:
            url = self.extractUrl(response)
            if output == "md":
                print("![]({})".format(url))
            elif output == "url":
                print(url)

    def getUserProfile(self):
        response = utils.getUserProfile(self.APIToken)
        self.betterPrint(response)

    def getUploadHistory(self):
        response = utils.getUploadHistory(self.APIToken)
        self.betterPrint(response)

    def deleteImage(self, hash: str):
        response = utils.deleteImage(hash)
        self.betterPrint(response)

    def deleteImageByname(self, filename: str):
        response = utils.getUploadHistory(self.APIToken)
        for image in response:
            if image["filename"] == filename.split("/")[-1]:
                self.deleteImage(image["hash"])
                exit(0)
        print("{} has not been uploaded, delete fail!".format(filename))


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple command line HTTP client of https://sm.ms"
    )
    parser.add_argument(
        "method", help="API method: [upload | delete | getprofile | gethistory]"
    )
    parser.add_argument(
        "-f",
        "--filename",
        help="used with [upload | delete], select image to be uploaded or deleted",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="used with upload, specify the output format: [json | md | url], default is json",
    )
    args = parser.parse_args()
    # handle arguments
    c = Client()
    if args.method == "upload":
        c.uploadImage(args.filename, args.output)
    elif args.method == "delete":
        c.deleteImageByname(args.filename)
    elif args.method == "getprofile":
        c.getUserProfile()
    elif args.method == "gethistory":
        c.getUploadHistory()


if __name__ == "__main__":
    main()
