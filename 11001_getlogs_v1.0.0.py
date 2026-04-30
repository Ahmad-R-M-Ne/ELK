####################################################################################################
# Name: ELK _ GET Log _ v1.0                                                                       #
# Job: This Script connects to the Elasticsearch and Get Last Logs.                                #
# Author: Ahmad Mojahed                                                                            #
# Date: 2025-12-20                                                                                 #
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

def fetch_logs(size=100, query=None):
    """
    Fetch logs from Elasticsearch index.
    Read-only operation.
    """

    if query is None:
        query = {"match_all": {}}

    payload = {
        "size": size,
        "sort": [
            {"@timestamp": {"order": "desc"}}
        ],
        "query": query
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
    data = fetch_logs(size=10)          # Last 10 Logs

    for hit in data["hits"]["hits"]:
        source = hit["_source"]

        print("Time:", source.get("@timestamp"))
        print("Device:", source.get("host", {}).get("name"))
        print("Message:", source.get("message"))
        print("-" * 60)

#====================================================================================================
#END


