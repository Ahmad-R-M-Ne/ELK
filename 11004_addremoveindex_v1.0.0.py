####################################################################################################
# Name: ELK _ Add / Remove Index                                                                   #
# Job: This Script creates or removes an Elasticsearch INDEX                                       #
#      based on user input (add / remove).                                                         #
# Author: Ahmad Mojahed                                                                            #
# Date: 2026-01-06                                                                                 #
####################################################################################################

import requests
import json

#====================================================================================================
# ELK SERVER CONFIGURATION
#====================================================================================================
ES_HOST = "http://192.168.0.1:9200"

USERNAME = ""
PASSWORD = ""

HEADERS = {
    "Content-Type": "application/json"
}

#====================================================================================================
# FUNCTION: CREATE INDEX
#====================================================================================================
def create_index(index_name):
    payload = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        }
    }

    response = requests.put(
        f"{ES_HOST}/{index_name}",
        auth=(USERNAME, PASSWORD),
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=10
    )

    return response

#====================================================================================================
# FUNCTION: DELETE INDEX
#====================================================================================================
def delete_index(index_name):
    response = requests.delete(
        f"{ES_HOST}/{index_name}",
        auth=(USERNAME, PASSWORD),
        timeout=10
    )

    return response

#====================================================================================================
# MAIN SCRIPT EXECUTION
#====================================================================================================
if __name__ == "__main__":

    action = input("Please Enter Action (add/remove): ").strip().lower()
    index_name = input("Please Enter INDEX Name: ").strip()

    if not index_name:
        print("INDEX name cannot be empty")
        exit(1)

    if action == "add":
        response = create_index(index_name)

        if response.status_code == 200:
            print(f"INDEX '{index_name}' created successfully")
        else:
            print(f"Failed to create INDEX '{index_name}'")
            print(response.text)

    elif action == "remove":
        response = delete_index(index_name)

        if response.status_code == 200:
            print(f"INDEX '{index_name}' deleted successfully")
        else:
            print(f"Failed to delete INDEX '{index_name}'")
            print(response.text)

    else:
        print("Invalid action. Please enter 'add' or 'remove'")

#====================================================================================================
#END
