# import shutil
# shutil.copy("Aditya.txt", "Utsav.txt")


# import requests
# response = requests.get("https://api.github.com")
# print(response.text)

# import requests
# response = requests.get("https://api.github.com")
# data = response.json()
# print(data["current_user_url"])
import requests
data = {
    "username": "admin",
    "password": "1234"
}
response = requests.post("https://httpbin.org/post", data=data)
print(response.json())


