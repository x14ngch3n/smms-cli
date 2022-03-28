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

    def uploadImage(self, filename: str):
        response = utils.uploadImage(filename, self.APIToken)
        self.betterPrint(response)

    def getUserProfile(self):
        response = utils.getUserProfile(self.APIToken)
        self.betterPrint(response)

    def getUploadHistory(self):
        response = utils.getUploadHistory(self.APIToken)
        self.betterPrint(response)

    def deleteImage(self, hash):
        response = utils.deleteImage(hash)
        self.betterPrint(response)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple command line HTTP client of https://sm.ms"
    )
    parser.add_argument(
        "method", help="API method: upload | delete | getprofile | gethistory"
    )
    parser.add_argument(
        "-f", "--filename", help="used with upload, select image to be uploaded"
    )
    parser.add_argument("--hash", help="used with delete, delete image by hash value")

    args = parser.parse_args()
    c = Client()
    if args.method == "upload":
        c.uploadImage(args.filename)
    elif args.method == "delete":
        c.deleteImage(args.hash)
    elif args.method == "getprofile":
        c.getUserProfile()
    elif args.method == "gethistory":
        c.getUploadHistory()


if __name__ == "__main__":
    main()
