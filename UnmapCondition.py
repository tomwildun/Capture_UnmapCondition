# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:35:16 2019

@author: thomas.dunn
"""

import requests

#-------------------------------------------------------------MAPPINGS--------------------------------------------------------------#

contract_mappings = ['NEC478-A5']


#------------------------------------------------------------PARAMETERS-------------------------------------------------------------#

auth_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJoMjNmNWUzLTE2bEd3dmdzOG1fRXRWYWF2anhlNXpqTkZxNUs0ZmF5eVM4In0.eyJqdGkiOiJmYTg0NGM2Yi1mYjhhLTQyNTMtYmJiZC0zNTY4OTkyMWIwZjYiLCJleHAiOjE1NTQ0MTg0MDIsIm5iZiI6MCwiaWF0IjoxNTU0NDE0ODAyLCJpc3MiOiJodHRwczovL2JldGEuY2FwdHVyZXJ4LmNvbS9hdXRoL3JlYWxtcy9jYXB0dXJlcngiLCJhdWQiOiJjdW11bHVzNHVpIiwic3ViIjoiYzAzYjg1MTctMmM0ZS00ZGNmLWE2OTQtZjJlZDUxMzY0NmVjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY3VtdWx1czR1aSIsIm5vbmNlIjoiNjMwOTk2NzAtMTNkZC00MTQ5LTgyMDYtZjk4N2NiM2M5NWYyIiwiYXV0aF90aW1lIjoxNTU0NDE0ODAyLCJzZXNzaW9uX3N0YXRlIjoiODFhYjRkM2ItOTJkZS00Y2U0LThlN2ItYjZlNTZkZTcyZjE4IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIiwiaHR0cHM6Ly9iZXRhLmNhcHR1cmVyeC5jb20iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImM0X2NhbkNyZWF0ZUZlZVNldHMiLCJjNF9pbnRlcm5hbFJlYWQiLCJjNF9jYW5DcmVhdGVDb25kaXRpb25TZXRzIiwiYzRfY2FuUmVhZFZpcnR1YWxJbnZlbnRvcnkiLCJjNF9jYW5DcmVhdGVDb3ZlcmVkRW50aXR5IiwiYzRfY2FuQ3JlYXRlQ29udHJhY3RzIiwiYzRfY2FuUmVhZFJlZmVyRG9jIiwiYzRfY2FuUmVhZFVzZXJzIiwiYzRfY2FuUmVhZEFjdGlvbkxvZyIsImM0X2NhblJlYWRTY2hlZHVsZXIiLCJjNF9jYW5SZWFkUmVwbGVuaXNobWVudFJ1bGVTZXQiLCJjNF9jYW5DcmVhdGVPcnBoYW5zIiwiYzRfY2FuUmVhZENsYWltcyIsImM0X2NhblJlYWRBbmFseXRpY2FsU2VhcmNoIiwiYzRfY2FuQ3JlYXRlUmVwbGVuaXNobWVudCIsImM0X2NhblJlYWRQaGFybWFjeSIsImM0X2NhblJlYWRDZW50cmFsZmlsbCIsInVtYV9hdXRob3JpemF0aW9uIiwiYzRfY2FuUmVhZFdob2xlU2FsZXJBY2NvdW50cyIsImM0X2NhbkNyZWF0ZVNjaGVkdWxlciIsImM0X2NhbkNyZWF0ZVBhdGllbnRFbmNvdW50ZXIiLCJjNF9jYW5SZWFkQ292ZXJlZEVudGl0eSIsImM0X2NhblJlYWREcnVnTGlzdHMiLCJjNF9jYW5SZWFkUGF5b3JDbGFzc2lmaWNhdGlvbiIsImM0X2NhbkNyZWF0ZVBoYXJtYWN5Q2hhaW4iLCJjNF9jYW5DcmVhdGVVc2VycyIsImM0X2NhblJlYWRDb250cmFjdHMiLCJjNF9jYW5SZWFkQ3VtdWx1czQiLCJjNF9jYW5DcmVhdGVWaXJ0dWFsSW52ZW50b3J5IiwiYzRfY2FuQ3JlYXRlUGF5b3JDbGFzc2lmaWNhdGlvbiIsImM0X2NhbkNyZWF0ZUdsb2JhbFBheW9yQ2xhc3NpZmljYXRpb24iLCJjNF9jYW5SZWFkUmVwb3J0cyIsImM0X2NhbkNyZWF0ZUFjdGlvbkxvZyIsImM0X2NhblJlYWRDaGlsZFNpdGVzIiwiYzRfY2FuUmVhZFByZXNjcmliZXIiLCJjNF9jYW5DcmVhdGVXaG9sZXNhbGVycyIsImM0X2NhblJlYWRGb3JtdWxhcnkiLCJjNF9jYW5DcmVhdGVEcnVnTGlzdHMiLCJjNF9jYW5SZWFkR2xvYmFsUGF5b3JDbGFzc2lmaWNhdGlvbiIsImM0X2ludGVybmFsIiwiYzRfY2FuUmVhZFBoYXJtYWN5Q2hhaW4iLCJjNF9jYW5DcmVhdGVQaGFybWFjeSIsImM0X2NhbkNyZWF0ZVJlZmVyRG9jIiwiYzRfY2FuUmVhZFBhdGllbnRFbmNvdW50ZXIiLCJjNF9jYW5DcmVhdGVFbGlnaWJpbGl0eVBvbGljeSIsImM0X2NhblJlYWRPcnBoYW5zIiwiYzRfY2FuQ3JlYXRlQ2VudHJhbGZpbGwiLCJjNF9jYW5SZWFkVHJhbnNwb3J0cyIsImM0X2NhblJlYWRDbGFpbXN1YyIsImM0X2NhbkNyZWF0ZUNoaWxkU2l0ZXMiLCJjNF9jYW5DcmVhdGVGb3JtdWxhcnkiLCJjNF9jYW5SZWFkQ29uZGl0aW9uU2V0cyIsImM0X2NhblJlYWRSZXBsZW5pc2htZW50IiwiYzRfY2FuQ3JlYXRlQW5hbHl0aWNhbFNlYXJjaCIsImM0X2NhblJlYWRIZWFsdGhTeXN0ZW1zIiwiYzRfY2FuQ3JlYXRlSGVhbHRoU3lzdGVtcyIsImM0X2NhbkNyZWF0ZVJlcGxlbmlzaG1lbnREZXRhaWxzIiwiYzRfY2FuQ3JlYXRlQ2xhaW1zIiwiYzRfY2FuQ3JlYXRlV2hvbGVTYWxlckFjY291bnRzIiwiYzRfY2FuUmVhZFdob2xlc2FsZXJzIiwiYzRfY2FuUmVhZEVsaWdpYmlsaXR5UG9saWN5IiwiYzRfY2FuQ3JlYXRlUHJlc2NyaWJlciIsInVzZXIiLCJjNF9jYW5DcmVhdGVSZXBsZW5pc2htZW50UnVsZVNldCIsImM0X2NhblJlYWRGZWVTZXRzIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnt9LCJuYW1lIjoiVGhvbWFzIER1bm4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0aG9tYXMuZHVubkBjYXB0dXJlcnguY29tIiwiZ2l2ZW5fbmFtZSI6IlRob21hcyIsImZhbWlseV9uYW1lIjoiRHVubiIsImVtYWlsIjoidGhvbWFzLmR1bm5AY2FwdHVyZXJ4LmNvbSJ9.iYHee3Q-MNxBAqC59YTO-n_tMt9UeBMGqanwVoSI2LXB5fSFF_YmpBSsIvG5S1CFdIt1Vw_fZBusX857C1MUOojosK54hWbTbkLKZK9SfgWhybWFnfjYaTVju5R301u7e1IvH87alDfr_aluGbvk0rGvNl3z9yZMwLLCnACrLY7zNm-YXI4dd5EQfP-uzebxwuUfW50TOgK2fUqaKV08BQS_7OA9ByeuVsrkpE0TnE6GkHa158eBEQhTK5aT3YkkdMMJJuu9r6Nc0PgYfimrXamygT6Jwp7HzUrFAx-mtPzaqReQElaoLNXbHeDsBjk8ZqrBVFhTSvLgUAZAqb8JMw'
URL = 'https://beta.capturerx.com/apiservice/cumulus/v1/contracts/'


#-----------------------------------------------------------------------------------------------------------------------------------#

header = {'Authorization': 'Bearer ' + auth_token}


response = requests.get(URL,headers=header)
contracts = response.json()

failures = []


for mapping in contract_mappings:
	contract_to_update = {}
	for contract in contracts:
		if contract['necBillingCode'] == mapping:
			contract_to_update = contract
			break
	
	if(bool(contract_to_update) != False):
		response2 = requests.get(URL + contract['id'], headers=header)
		contract = response2.json()	
		contract['conditionSetId'] = None 
		body = contract


		final_response = requests.put(URL,json=body,headers=header)
		print(final_response)
		print(final_response.text)
	else:
		failures.append(mapping)
		print(failures)
