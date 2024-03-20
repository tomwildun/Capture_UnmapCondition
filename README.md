# Contract NEC Billing Code Updater
This Python script updates the conditionSetId field of contracts with specific NEC billing codes on the unnamed platform using their API service.

Prerequisites
Python 3.x
requests library (install via pip install requests)
Usage
Replace the auth_token variable with your actual authentication token obtained from website.
Update the contract_mappings list with the NEC billing codes of the contracts you want to update.
Run the script.
Description
The script sends a GET request to retrieve contract data from the webpage API.
It then searches for contracts with NEC billing codes specified in the contract_mappings list.
If found, it retrieves the details of the contract and updates the conditionSetId field to None.
Finally, it sends a PUT request to update the contract information on the platform.
Important Note
Ensure that the provided NEC billing codes correspond to existing contracts in the CaptureRx system.

Disclaimer
This script is provided as-is and without warranty. Use it responsibly and at your own risk.
