#!/usr/bin/python

"""
    Summary:
    -------
        This code is to POST to a Webhook and test
        to see if the Azure Automation Powershell
        Runbook is triggered.
    
    References:
    ----------
    - https://pep8.org/?msclkid=13a03ac8bb8e11eca7c7f4facb57ac49

    Use:
    ---
    python3 post_to_webhook.py

"""


import requests

webhook_url = "https://xxxxxx.webhook.ae.azure-automation.net/webhooks?token=xxxxxx"
print(webhook_url)

params = {
    "resourceGroupName": "API_INTEGRATION_TEST",
    "email": "xxxxxx@email.com",
    "APIManagementServiceName": "api-integration-test-1" 
}

response = requests.post(url=f"{webhook_url}", json=params)
response.encoding = 'utf-8'
response.json()
print(response, response.text)