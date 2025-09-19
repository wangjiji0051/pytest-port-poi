import pytest
from base.base_action import BaseAction
from conftest import get_token


# 场景：带货推广页面,门店推广顶部搜索接口
class TestSearchV4:
    @pytest.mark.P2
    @pytest.mark.parametrize('keyword', ['喜茶', 'qaq', '*', '1', ''])
    def test_search(self, keyword, get_token):
        url = 'http://ks-server-api.staging.kuaishou.com/rest/op/vc/location/searchV4?'
        payload = {
            'mod': 'vivo%28V2285A%29',
            'appver': '13.8.20.99999',
            'ud': '2197576973',
            'egid': 'DFP0252C125AA00DC7F985B578A26CC05259E4BE0F5C9153D076B0498691C69F',
            'kpf': 'ANDROID_PHONE',
            'kpn': 'KUAISHOU',
            'lkvr': 'CbcBXrS27bicELo1I_D1XibpN9q4JIZnU1xt-RAt8e-dgCtRfdOrNJjDJKqK7L5ysmn-Kg',
            'sig': '7a8a7461e2c05bf391b1a7e7c609371b',
            'rdid': 'ANDROID_3b704b7cdf7ded7c',
            'did': 'ANDROID_d0f5e2240b1af402'
        }
        datas = {
            'poiBiz': 'mergedLocalLife',
            'pcursor': '',
            'keyword': keyword,
            'longitude': '{"promoteFilterCommission":false,"promoteSorter":0,"taskId":"6d1422bf-b90d-4f10-85fd-afdfb2afad80","photoId":"","cityLimit":true}',
            'uQaTag': '0##cmPs:11#swLdgl:99#ecPp:--#cmNt:11',
            'latitude': '40.049408',
            'client_key': '3c2cd3f3',
            'cityName': '北京',
            'kuaishou.api_st': 'Cg9rdWFpc2hvdS5hcGkuc3QSoAEHbuGmJATlhXE4yeQhASBhKeVt_TgDfO4JzRSgCwuUXaAhs_S2isPUI3asumsao14fwFrzd3MjPGH2iq9dTPXUrdctndzLi7pW7bvafnQosX91o75Aq5jmcZ6aU4ZahRE3_-czsmWXWe2Hyw7JizSVeTyk7cPkcFigHGhN02ylVMbEs-0e5uhop5CmoaISDCX00g2kK-EC3F5MaIGGqv1lGhJui3CejrANDaJlFiiGcpBZwQ4iIJlZffM8sIvqd-GzmKovv2no6LfYksf33YcEOm1EIuhWKA8wAQ',
            'poiSubBiz': 'search',
            'videoModelCrowdTag': '',
            'os': 'android',
            'sdkStatus': 0,
            'cs': 'false',
            'token': get_token
        }
        headers = {
          'x-ktrace-id-enabled': '0',
          'x-forwarded-proto': 'https',
          'cookie': 'kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEHbuGmJATlhXE4yeQhASBhKeVt_TgDfO4JzRSgCwuUXaAhs_S2isPUI3asumsao14fwFrzd3MjPGH2iq9dTPXUrdctndzLi7pW7bvafnQosX91o75Aq5jmcZ6aU4ZahRE3_-czsmWXWe2Hyw7JizSVeTyk7cPkcFigHGhN02ylVMbEs-0e5uhop5CmoaISDCX00g2kK-EC3F5MaIGGqv1lGhJui3CejrANDaJlFiiGcpBZwQ4iIJlZffM8sIvqd-GzmKovv2no6LfYksf33YcEOm1EIuhWKA8wAQ; __NSWJ=; token=10ac069f4b2a49ebb487aa62c812836c-2197576973; region_ticket=RT_0F1652EA52858323667BA74540C7F2BDCF857840990211235A18AC2FEDC1C33FD64F8E69C; apdid=bb46d02f-56a1-421f-a23d-e578c70070febefb6c42f8787d42260714193fd2ec94:1754815765:1; JSESSIONID=BA75AE24158D3B0EDB2F8F57C8C202F2; accessproxy_session=6fe26115-a26c-48f0-9396-7b4ee7694cba',
          'accept-language': 'zh-cn',
          'x-kproxy-proto': 'http',
          'ct-context': '{"biz_name":"ATTRIBUTION","error_occurred":false,"sampled":true,"sampled_on_error":true,"segment_id":1474159873,"service_name":"CLIENT_TRACE","span_id":1,"trace_id":"My43NzQ2NTAyMDE3NDEzMzk5NjE2LjEyNTQ5LjE3NTgxMDUwNzQ1NjguMTI=","upstream_error_occurred":false}',
          'x-forwarded-for': '172.24.141.66',
          'x-requestid': '175810507456575493',
          'page-code': 'LOCALLIFE_STORE_PROMOTION',
          'x-real-ip': '172.24.141.66',
          'x-ksap-request-uuid': 'c4065a6f-6d50-49ec-b4eb-952da9f5a9d3',
          'x-ksclient-ip': '172.24.141.66',
          'x-kproxy-host': 'ks-server-api.staging.kuaishou.com',
          'content-type': 'application/x-www-form-urlencoded',
          'x-client-info': 'model=V2285A;os=Android;nqe-score=75;network=WIFI;signal-strength=4;',
          'user-agent': 'kwai-android aegon/4.27.0'
        }
        response = BaseAction().all_send_request(method="POST", params=payload, url=url, headers=headers, data=datas)
        response_data = response.json()
        print(response_data)
        """
         获取 data 中的 token:
         token = datas['token']
         print(f"获取到的 token: {token}")
         """
        # 断言
        assert response.status_code == 200
        assert response_data['result'] == 1
        # 判断响应中是否包含关键字
        if 'data' in response_data and isinstance(response_data['data'], list):
            """
            列表推导式:
            found_keywords = [item['name'] for item in response_data['data'] if 'name' in item and keyword in item['name']]
            """
            found_keywords = []
            for item in response_data['data']:
                if 'name' in item and keyword in item['name']:
                    found_keywords.append(item['name'])
            if found_keywords:
                print(f"找到关键字 '{keyword}' 在响应数据中: {found_keywords}")
            else:
                print(f"响应数据中未找到关键字 '{keyword}'")
        else:
            print(f"响应数据中没有 'data' 字段")





