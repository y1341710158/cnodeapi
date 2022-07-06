import requests
# res=requests.get("http://47.100.175.62:3000/api/v1/topics")
# print(res)
# print(res.json())
# print(res.url)
# print(res.text)
# print(res.content)
topic_data={
    "accesstoken":"e18de36f-d9ce-47e6-a2aa-1cf6508ec10b",
    "title":"aaaaa",
    "tab":"ask",
    "content":"asdasccc"
}
url ="http://47.100.175.62:3000/api/v1/topics"
res=requests.post(url=url,data=topic_data)
print(res.status_code)
print(res.json())
print(res.request.headers)