import requests

# Login with Sheety and create a project called 'day39 &40CapstoneFlightTracker'
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/7ec9a9657009ffd6698317797e8c9652/day39 &40CapstoneFlightTracker/'
SHEETY_AUTH = secrets.SHEETY_AUTH

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheety_headers = {'Authorization': f'Basic {SHEETY_AUTH}'}

    def get_destination_data(self):
        response = requests.get(url=f'{SHEETY_PRICES_ENDPOINT}/prices', headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    def check_email(self, email):
        data = requests.get(headers=self.sheety_headers, url=f'{SHEETY_PRICES_ENDPOINT}/users').json()['users']

        for user in data:
            if user['email'] == email:
                return True
            else:
                return False

    def post_new_user(self, name, surname, email):
        self.users_body = {
            'user': {
                'firstName': name,
                'lastName': surname,
                'email': email,
            }
        }
        return requests.post(headers=self.sheety_headers,
                             url=f'{SHEETY_PRICES_ENDPOINT}/users', json=self.users_body).json()

    def get_customer_emails(self):
        customers_endpoint = f'{SHEETY_PRICES_ENDPOINT}/users'
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
