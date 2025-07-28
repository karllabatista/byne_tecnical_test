import requests

send_data = requests.get("http://localhost:8000/helloworld")

print(send_data.status_code)
data = send_data.json()
print(data)


send_data2 = requests.get("http://localhost:8000/integer_info")

print(send_data2.status_code)
data = send_data2.json()
print(data)