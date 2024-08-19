import requests

response = requests.get("http://api.open-notify.org/astros")

print(response)

# with open("astronauts.json", "w") as f:
#     f.write(response.text)
