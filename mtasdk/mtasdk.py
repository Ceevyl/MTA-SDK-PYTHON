import requests

class Mta:

    def __init__(self, url, auth ) -> None:

        self.url = url

        self.Auth = auth;
    
    def call(self, resourceName ,function, args):

        self.url = self.url + "/" + resourceName + "/call/" + function

        try:

            self.response = requests.post(self.url, headers={"Content-Type": "application/json"}, auth=self.Auth, json=args )

            if self.response.status_code != 200:

                return self.response;
                
            else:

                return self.response;
            
        except:

            return

