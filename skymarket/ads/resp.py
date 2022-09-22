import requests

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNDIxNTg2LCJqdGkiOiI2NmM2ODdhZDg0NWE0ZGQyOTg0ZDllNjJiMGI0NzI1MSIsInVzZXJfaWQiOjZ9.RkdlZrUB0E6VhJCntVM-o0aB38Cts1f_RfhfyMEpYiU'
}
response = requests.get('http://127.0.0.1:8000/api/users/me/', headers=headers)
json_resp = response.json()
print(json_resp['id'])
