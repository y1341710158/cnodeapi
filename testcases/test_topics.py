import requests
import business.common as common  #引用业务代码下的封装函数
base_ulr="http://47.100.175.62:3000/api/v1"

def test_topic_index_page():
    query_params={
        'page':1,
        'tab':'ask',
        'limit':2,
        "mdrender":"false"
    }
    res = requests.get(base_ulr+'/topics',params=query_params)
    assert res.status_code ==200
    assert res.json()['success']==True
    data = res.json()['data']
    assert  len(data) == query_params['limit']
    for topic in data:
        assert topic['tab']==query_params['tab']


def test_create_topic():
    topic_data = {
         "accesstoken": common.get_token(),
        "title": "aaaaa",
        "tab": "ask",
        "content": "asdasccc"
    }

    topic_data2 = {
        "accesstoken": common.get_token(),
        "title": "aaaaa11",
        "tab": "ask",
        "content": "asdasccc123123"
    }
    res = common.create_topic(topic_data2)
    print(res.json())
    assert res.status_code==200
    assert res.json()['success'] ==True

    # res2=common.create_topic(topic_data)
    # print(res2)  res2 返回z值只有<Response [200]> 无法做断言
    # assert  not res.json('topic_id')  ==  res2.json('topic_id')  #这个内容只有code没有topic


def test_topic_update():
    topic_data = {
        "accesstoken": common.get_token(),
        "title": "aaaaa",
        "tab": "ask",
        "content": "asdasccc"
    }
    res = common.create_topic(topic_data)
    topic_id = res.json()['topic_id']
    update_topic_data = {
        "accesstoken": common.get_token(),
        "title": "aaaaa11",
        "topic_id":topic_id,
        "tab": "ask",
        "content": "asdasccc123123"
    }
    update_res =requests.post(base_ulr+'/topics/update',update_topic_data)
    print(update_res.json())
    assert  update_res.json()['success']  == True

    # detail_res=common.topic_detail(topic_id)
    # print(detail_res)
    # detail_res1= detail_res.json()
    # assert  detail_res1['success']==True #因为借口不同所有无法验证断言是否正确


test_topic_update()