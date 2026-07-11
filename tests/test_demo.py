import requests


class TestPytestDemo:

    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"

        response = requests.get(f"{base_url}/posts/1")

        assert response.status_code == 200
        assert response.json()["userId"] == 1
        assert response.json()["id"] == 1
    


    def test_post_demo(self):
        base_url = "http://jsonplaceholder.typicode.com"
        requests_data = {
            'title':'foo',
            'body':'bar',
            'userId':'1'
        }
        
        response = requests.post(f"{base_url}/posts", requests_data)

        assert response.status_code == 201
        print(response.json())
        assert response.json()['userId'] == '1'
        assert response.json()[id] == 101




# import requests

# base_url = "https://jsonplaceholder.typicode.com"

# response = requests.get(f"{base_url}/posts/2")

# print("状态码：", response.status_code)
# print("原始文本：", response.text)
# print("JSON数据：", response.json())
# print("userId：", response.json()["userId"])
# print("id：", response.json()["id"])
# print("title：", response.json()["title"])
