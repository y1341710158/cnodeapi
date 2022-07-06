import requests
import pytest
import json
import business.file_utils as f1

test_data=f1.parse_json_file("data/topic.json")
@pytest.mark.parametrize("topic_data,code,msg",test_data)#pytest 参数化的设置
def  test_create_topic(topic_data,code,msg):
    res = requests.post("http://47.100.175.62:3000/api/v1/topics",topic_data)
    print(res.json())
    print(topic_data,code,msg)