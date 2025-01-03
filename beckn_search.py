import requests
from datetime import datetime
import uuid
import json
from helper import Helper
class BecknSearch:
    def __init__(self, helper):
        self.helper = helper

    def generate_search_request(self, pickup, drop, catalogs, optimization_parameter):
        # Generate the search request using the Helper class
        return self.helper.generate_search_request(pickup, drop, catalogs, optimization_parameter)

    def call_search(self, search_request_body):
        # Placeholder for actual API call to Beckn registry or protocol endpoint
        url = "http://127.0.0.1:5000/mobility/search_by_pickup_drop_location"  # BPP endpoint
        headers = Helper.construct_auth_header(search_request_body)
        try:
                    # Log the request body for debugging
                    print("Request Body:")
                    print(json.dumps(search_request_body, indent=4))
                    
                    # Make the request
                    response = requests.post(url, json=search_request_body, headers=headers)
                    
                    # Log the response status and body for debugging
                    print(f"Response Status Code: {response.status_code}")
                    print(f"Response Body: {response.text}")
                    
                    if response.status_code == 200:
                        return response.json()
                    else:
                        raise Exception(f"Error with the search request: {response.status_code} - {response.text}")
        except Exception as e:
                print(f"Exception occurred: {str(e)}")
                raise
    # @staticmethod
    # def create_context(transaction_id):
    #     return {
    #         "domain": "nic2004:60221",
    #         "country": "IND",
    #         "city": "std:080",
    #         "action": "search",
    #         "core_version": "0.9.1",
    #         "bap_id": "df35-203-192-239-167.ngrok-free.app",  # BAP (client) URI
    #         "bap_uri": "https://df35-203-192-239-167.ngrok-free.app",  # BAP (client) URI
    #         "transaction_id": transaction_id,
    #         "message_id": str(uuid.uuid4()),
    #         "timestamp": datetime.utcnow().isoformat() + 'Z'
    #     }
