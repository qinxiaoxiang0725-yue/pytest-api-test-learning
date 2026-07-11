import requests

base_url = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{base_url}/posts/1")

print("状态码：", response.status_code)
print("原始文本：", response.text)
print("JSON数据：", response.json())
print("userId：", response.json()["userId"])
print("id：", response.json()["id"])
print("title：", response.json()["title"])