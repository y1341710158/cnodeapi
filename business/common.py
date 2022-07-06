# 封装公共函数
import  requests
def create_topic(topicdata):
    # topic_data = {
    #     "accesstoken": "e18de36f-d9ce-47e6-a2aa-1cf6508ec10b",
    #     "title": "aaaaa",
    #     "tab": "ask",
    #     "content": "asdasccc"
    # }
    url ="http://47.100.175.62:3000/api/v1/topics"
    res =requests.post(url,json=topicdata)
    return res
def topic_detail(topic_id):
    url="http://47.100.175.62:3000/api/v1/"+topic_id
    return  requests.get(url)

def get_token():
    return "e18de36f-d9ce-47e6-a2aa-1cf6508ec10b"