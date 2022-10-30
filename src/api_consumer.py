import json
from urllib import response, parse

import requests
import yaml
import json


class ApiConsumer:

    
    config: dict = {}
    consumer: requests.session = requests.session()
    forgery_token: json = None

    def read_config(self) -> dict:
        with open("src/resources/config.yaml", "r") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def login(self) -> response:
        #self.consumer = requests.session()
        url = self.config["url"] + "Account/LogIn"
        payload=('Login={0}&Password={1}'.format( 
            parse.quote_plus(self.config["login"]), parse.quote_plus(self.config["password"])))
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = self.consumer.post(url, headers=headers, data=payload)
        return response

    def logout(self) -> response:
        url = self.config["url"] + "Account/LogOut"
        response = self.consumer.get(url, headers=None, data=None)        
        return response

    def get_forgery_token(self) -> json:
        url = self.config["url"] + "/NewPortal/security/getforgerytoken"
        payload={}
        headers = {}
        response = self.consumer.get(url, headers=headers, data=payload)
        #print(response.text)
        self.forgery_token = json.loads(response.text)
        return self.forgery_token

    def get_doctors_and_facilities(self) -> json:

        url = "https://portalpacjenta.luxmed.pl/PatientPortal/NewPortal/Dictionary/facilitiesAndDoctors?cityId=3&serviceVariantId=4502&secondServiceVariantId="

        payload={}
        headers = {
        'xsrf-token': self.forgery_token["token"],
        }
        response = self.consumer.get(url, headers=headers, data=payload)
        #print(response)
        return json.loads(response.text)