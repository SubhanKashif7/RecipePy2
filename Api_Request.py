import requests
from  Methods import  Methods
import time
class Api_Request:
    def __init__(self, recipe):
        self.recipe = recipe
        self.methods = Methods()

        self.url = f"https://api.api-ninjas.com/v1/recipe?query={self.recipe}"
        self.apikey = "WvN7UBmzmUbNYSMYEGqNdg40eJ3p199mYTwHnc1J"

        try:
            response = requests.get(self.url, headers={"X-Api-Key": self.apikey})
            self.data = response.json()
            if response.status_code != 200:
                print(f"Error fetching data. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            self.data = {}

    def showTitles(self):
        for idx, obj in enumerate(self.data):
            self.methods.spacer()
            print(f"{idx} - {obj['title']}")
            self.methods.spacer()

    def showRecipe(self,isDataAvailable=False):
        if (isDataAvailable):
            for recipe in isDataAvailable:
                self.methods.spacer()
                print(isDataAvailable["title"])
                self.methods.spacer()
                print(isDataAvailable["instructions"])
                self.methods.spacer()
                print(isDataAvailable["ingredients"])
                self.methods.spacer()
                print("Status : 2")
                print(time.ctime())
        else:
            for recipe in self.data:
                self.methods.spacer()
                print(recipe["title"])
                self.methods.spacer()
                print(recipe["instructions"])
                self.methods.spacer()
                print(recipe["ingredients"])
                self.methods.spacer()
                print("Status : 2")
                print(time.ctime())

        def returnRecipe(self):
            data = {}
            for recipe in self.data:
                data[recipe['title']] = {
                    'instruction': recipe['instruction'],
                    'ingredients': recipe['ingredients'],
                    'status': recipe['status'],
                    'time': recipe['time']
                }
            return data











