## 2. API Authentication ##

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token ..."}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response, this token corresponds to the account of Vik Paruchuri.
print(response.json())

response1 = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
orgs = response1.json()

## 3. Endpoints and Objects ##

response = requests.get("https://api.github.com/users/torvalds", headers = headers)
torvalds = response.json()

## 4. Other Objects ##

response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers = headers)
hello_world = response.json()

## 5. Pagination ##

params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()

params2 = {"per_page": 50, "page": 2}
response2 = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params2)
page2_repos = response2.json()

## 6. User-Level Endpoints ##

response = requests.get("https://api.github.com/user", headers=headers)
user = (response.json())

## 7. POST Requests ##

# Create the data that is passed into the API endpoint.
payload = {"name": "learning-about-apis"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = (response.status_code)

## 8. PUT/PATCH Requests ##

payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)

payload1 = {"description": "Learning about requests!", "name": "learning-about-apis"}
response1 = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload1, headers=headers)
status = response1.status_code

## 9. DELETE Requests ##

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

reponse1 = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status = reponse1.status_code