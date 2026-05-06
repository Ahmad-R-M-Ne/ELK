####################################################################################################
# Name: ELK _ Check Indexs                                                                         #
# Job: This Script connects to the Elasticsearch server and Lists                                  #
#      All Existing INDEXs.                                                                        #
# Author: Ahmad Mojahed                                                                            #
# Date: 2026-01-06                                                                                 #
####################################################################################################

import requests

#====================================================================================================
# ELK SERVER CONFIGURATION
#====================================================================================================
ES_HOST = "http://192.168.0.1:9200"

USERNAME = ""
PASSWORD = ""

#====================================================================================================
# MAIN SCRIPT EXECUTION
#====================================================================================================
if __name__ == "__main__":

    url = f"{ES_HOST}/_cat/indices?format=json"

    try:
        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            timeout=10
        )
        response.raise_for_status()
    except Exception:
        print("Failed to connect to Elasticsearch")
        exit(1)

    indices = response.json()

    if not indices:
        print("No INDEX found")
        exit(0)

    print("Existing INDEXes:\n")
    print("-" * 60)

    for index in indices:
        print(index.get("index"))

    print("-" * 60)

#====================================================================================================
#END
