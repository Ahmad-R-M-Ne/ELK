####################################################################################################
# Name: ELK _ GET Log _ v1.1                                                                       #
# Job: This Script connects to the Elasticsearch and Retrieves the Last Logs                       #
#      For a Specific Host IP Address.                                                             #
# Author: Ahmad Mojahed                                                                            #
# Date: 2026-01-05                                                                                 #
####################################################################################################

import requests
import json

#====================================================================================================
# ELK SERVER CONFIGURATION
#====================================================================================================
ES_HOST = "http://192.168.0.1:9200"
INDEX_NAME = "laboratory-network-logs"

USERNAME = ""
PASSWORD = ""

#====================================================================================================
# QUERY TO DATABASE
#====================================================================================================
HEADERS = {
    "Content-Type": "application/json"
}

def fetch_logs(host_ip, size):
    """
    Fetch last logs for a specific host IP address.
    Read-only operation.
    """

    payload = {
        "size": size,
        "sort": [
            {"@timestamp": {"order": "desc"}}
        ],
        "query": {
            "term": {
                "host.ip": host_ip
            }
        }
    }

    url = f"{ES_HOST}/{INDEX_NAME}/_search"

    response = requests.post(
        url,
        auth=(USERNAME, PASSWORD),
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=10
    )

    response.raise_for_status()
    return response.json()

#====================================================================================================
# MAIN SCRIPT EXECUTION
#====================================================================================================
if __name__ == "__main__":

    host_ip = input("Enter Host IP Address to Filter Logs: ")
    logs_count = input("Enter Number of Last Logs to Retrieve: ")

    try:
        logs_count = int(logs_count)
    except ValueError:
        print("Invalid number of logs")
        exit(1)

    data = fetch_logs(host_ip=host_ip, size=logs_count)

    hits = data.get("hits", {}).get("hits", [])

    if not hits:
        print("No logs found for the specified host IP")
        exit(0)

    for hit in hits:
        source = hit.get("_source", {})

        print("Time:", source.get("@timestamp"))
        print("Host IP:", source.get("host", {}).get("ip"))
        print("Device:", source.get("host", {}).get("name"))
        print("Message:", source.get("message"))
        print("-" * 60)

#====================================================================================================
#END
