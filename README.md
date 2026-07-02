![Elasticsearch Logo](/assets/Elasticsearch_Logo_1.jpg)
# 🤖 ELK Automation Scripts

## Python scripts to automate monitoring tasks.

This project uses Python to interact with the Elasticsearch REST API and collect log data from an ELK stack.
The script connects directly to the Elasticsearch server, builds time-based search queries,
and retrieves logs from selected indices.
It supports flexible time ranges such as the last 24 hours, last 60 minutes, or last 7 days.
For large log volumes, the script uses the Scroll API to export all matching records safely without losing data.
Collected logs are saved into structured output files such as JSONL for later analysis, backup,
reporting, or integration with other tools.
This approach is useful for network monitoring, log auditing, incident investigation, and automated log collection workflows.

![Elasticsearch Logo](/assets/Elasticsearch_Logo_2.png)

## Versions:
Elasticsearch: 9.2.1
Logstash: 9.2.1
Kibana: 9.2.1

## 🚀 Quick Start

```bash
git clone https://github.com/Ahmad-R-M-Ne/ELK.git
pip install -r requirements.txt
