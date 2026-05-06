####################################################################################################
# Name: ELK _ Check Logs                                                                           #
# Job: This Script checks whether each Host has Sent at least one Log                              #
#      to the Elasticsearch Server within a specified time window.                                 #
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

HEADERS = {
    "Content-Type": "application/json"
}

#====================================================================================================
# FUNCTION: CHECK LOG EXISTENCE FOR HOST
#====================================================================================================
def check_host_logs(host_ip, days):
    """
    Check if at least one log exists for a host IP
    within the given time window.
    """

    payload = {
        "size": 1,
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "host.ip": host_ip
                        }
                    },
                    {
                        "range": {
                            "@timestamp": {
                                "gte": f"now-{days}d"
                            }
                        }
                    }
                ]
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
    result = response.json()

    return result.get("hits", {}).get("total", {}).get("value", 0) > 0

#====================================================================================================
# MAIN SCRIPT EXECUTION
#====================================================================================================
if __name__ == "__main__":

    hosts_file = ""
    days = 7                                     # Time Period

    try:
        days = int(days)
    except ValueError:
        print("Invalid number of days")
        exit(1)

    try:
        with open(hosts_file, "r") as f:
            hosts = [line.strip() for line in f if line.strip()]
    except IOError:
        print("Unable to read hosts file")
        exit(1)

    print("\nLog Presence Check Result:\n")
    print("-" * 60)

    for host_ip in hosts:
        try:
            has_logs = check_host_logs(host_ip, days)
        except Exception as e:
            print(f"{host_ip}  -->  ERROR (Elasticsearch query failed)")
            continue

        if has_logs:
            print(f"{host_ip}  -->  OK (Logs received)")
        else:
            print(f"{host_ip}  -->  PROBLEM (No logs in last {days} days)")

    print("-" * 60)

#====================================================================================================
#END
