import pytest 
import json
from base.base_action import BaseAction
from conftest import get_token


# 场景:本地即时推送城市下拉列表接口
class TestGetDivisionList:

    @pytest.mark.P
    @pytest.mark.parametrize('bizCode', ['locallife.delivery.address', '原神', ''])
    def test_verify_bizCode(self, bizCode, get_token):
        url = "http://apissl.gifshow.com/rest/kgw/c/zt/poi/search/division/list"
        payload = {
            'mod': 'vivo%28V2285A%29',
            'appver': '13.8.20.99999',
            'ud': '3816980566',
            'kpf': 'ANDROID_PHONE',
            'kpn': 'KUAISHOU',
            'sig': '6147e8f5f8e881c01f6764ec574d4655',
            'did': 'ANDROID_d0f5e2240b1af402',
            'token': get_token
        }
        datas = json.dumps({
            "bizName": "",
            "bizCode": bizCode,
            "adcodeVersion": 1,
            "adcodeLevel": [
                "CITY"
            ]
        })
        headers = {
            'x-ktrace-id-enabled': '0',
            'x-forwarded-proto': 'https',
            'cookie': '__NSWJ=; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAGCirgqx3zCu5jnBlLXiVJlRmi2_AoTs7GBLgslFhWwWTGHFbFWyQ9hcbRXZtusGrJ0xqzfpOGq25YkeNpAOw2QN140x5n3R-qFPTWhd9f7qQVm6FVFrrw4LUFuhfbPppYIw0V4p-jCmUy-iQo9PbJW8Q6KjfbmRYQf9UdVr0n3GoPxOHUpSpSXImK1Enu0XhnsZtrPGfoJMXuoas_-MScuGhJThZNu-rRPH4Mw3KnOATqUKJgiICCkUbi51FwlYlDrpkex4T4jKoZTKKfadl9FaBrdhHOUKAUwAQ; token=9b41bc4fb48c49f6a912c6601d061e2b-3816980566; region_ticket=RT_C121743FA9CAF99ECCAA63AFA43EE7039B3A5AE8DABF2C795C7328801F8651CBE149AE997',
            'accept-language': 'zh-cn',
            'x-kproxy-proto': 'http',
            'ct-context': '{"biz_name":"ATTRIBUTION","error_occurred":false,"sampled":true,"sampled_on_error":true,"segment_id":2133416686,"service_name":"CLIENT_TRACE","span_id":1,"trace_id":"My40MTYyMzAwMzk3OTExOTY1MDcyLjIyMDAxLjE3NTgxODkxMjIyOTEuNA==","upstream_error_occurred":false}',
            'x-forwarded-for': '172.24.141.66',
            'x-requestid': '175818912228995302',
            'page-code': 'MERCHANT_ADDRESS_EDIT_PAGE',
            'x-real-ip': '172.24.141.66',
            'x-ksap-request-uuid': 'eba474b0-712e-480a-8864-e2b7c601a842',
            'usesig3': 'true',
            'x-ksclient-ip': '172.24.141.66',
            'x-kproxy-host': 'apissl.gifshow.com',
            'x-exp': '',
            'content-type': 'application/json',
            'x-client-info': 'model=V2285A;os=Android;nqe-score=-1;network=WIFI;signal-strength=4;',
            'user-agent': 'kwai-android aegon/4.27.0'
        }
        response = BaseAction().all_send_request(method="POST", url=url, headers=headers, params=payload, data=datas)
        response_data = response.json()
        print(response_data)
        # 断言
        assert response.status_code == 200
        assert response_data['code'] == 200 and response_data['errorMsg'] == "成功"
        if 'divisionDetail' in response_data and isinstance(response_data['divisionDetail'], list):
            found_keywords = []
            for item in response_data['divisionDetail']:
                if 'name' in item and '北京' in item['name']:
                    found_keywords.append(item['name'])
            if found_keywords:
                print(f"找到关键字 '北京' 在响应数据中: {found_keywords}")
            else:
                print(f"响应数据中未找到关键字 '北京'")
        else:
            print(f"响应数据中没有 'data' 字段")









