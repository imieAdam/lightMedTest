import urllib
import requests
import yaml

class ApiConsumer:

    config = None

    def read_config(self):
        with open("./resources/config.yaml", "r") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def login(self):
        url = self.config["url"] + "Account/LogIn"
        payload=('Login={0}&Password={1}'.format( 
            urllib.parse.quote_plus(self.config["login"]), urllib.parse.quote_plus(self.config["password"])))
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        '''
        for h in response.history:
            print("Status code is: " + str(h.status_code))
            print("Redirect URL is: " + h.url)
        print("FINAL Status Code is: " + str(response.status_code) + " Url is: " + response.url)
        '''
        return response

    def logout(self):
        url = self.config["url"] + "Account/LogOut"
        response = requests.request("GET", url, headers=None, data=None)        
        return response