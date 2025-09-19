import jsonpath
import pytest

from base.base_action import BaseAction


# 获取token
@pytest.fixture(scope='session', autouse=True)
def get_token():
    url = "https://ks-server-api.staging.kuaishou.com/rest/n/user/login/mobile?vague=0&earphoneMode=1&mod=iPhone16%2C2&keyconfig_state=1&appver=13.8.20.2866118&isp=&lkvr=OEQ3QTk1RjUtOTIztnxnkK8h7cC6MeoT0porPo_MbOEx0wd972ww1kk5mhjoIV4tSSL1Dg&cdid_tag=2&sys=ios26.0&did_tag=0&egid=DFP8DE665294623BF7401A86B053BF32D76D27B95FBCCB85D48B67C8132CF85F&cold_launch_time_ms=1757594579061&sh=2796&browseType=4&deviceBit=0&net=_5&kcv=1588&kpf=IPHONE&ver=13.8&is_background=0&oDid=65B2CA51-2F49-44E3-811B-68DE8EB23DF4&c=BETA&sw=1290&kpn=KUAISHOU&ll_client_time=1757594571225.142&icaver=1&grant_browse_type=AUTHORIZED&rdid=65B2CA51-2F49-44E3-811B-68DE8EB23DF4&darkMode=false&did=4AEC7977-974F-C927-E796-65250EA4627C"
    payload = '__NS_xfalcon=HUDR_sFnX%2B35uAUNVsMPNK3DOP5wnti1Lc8Axjy5z88T61A%3D%3D%24TE_bba43d5a5b87a8aacad5f087a8aacad5f0f1f7f2f0c72f685c4ae778d247ee5ed8a979f1aaa6ce2a8ba6ce0bf0&language=zh-Hans-CN%3Bq%3D1%2C%20zh-Hant-HK%3Bq%3D0.9%2C%20en-CN%3Bq%3D0.8%2C%20yue-Hant-CN%3Bq%3D0.7&secret=eTgYZ%2BSj%2FwnhVYl3rhtEqoN45yleRd%2FUMNbQnipm1u8S0%2Bc8mZIifYs%2FAzPGnwpHEbOPQWHqeNoqtASwBd3OHEKxDRZ%2BTyc9duQq8DCNk8rT1uoo9SQiWzB1Zq5kQHfI1A%2B%2BfivW3tbQi84YHosIuZgVBUVQG7XJqYI80IvZicrfx5rJ9nyWmm9t8d798RvDsGydK1kMc2FmUeFd3veadoUpUM7QWzfObTxQNZVucEfuh9eclKADUO1EkqRro0TJ03cxveRNMb6CjFRL33ftUdUUauZuj11MdokwBf2imwjEng8kUZuxk4N1C8j0DKNvrRelj%2Fc8WOhmXy6qiMgpOg%3D%3D&sig=a8f60714764d57aa4e248960fc88a93b&client_key=56c3713c&password=73f4a33d231345c656d72cdcbeceaa7543ab9f1e06c87a07d1fc83d21f579c00183fb3cffec3604e328331250695901707e6459a6db42562ba86bb20247b0663&power_mode=0&thermal=10000&mobileCountryCode=%2B86&global_id=DFPAC6A9493C3A64C55300B31B42BFF3FEA602417EC4D695CCD38CD27F14A02B&mobile=19291004830&raw=1757594614570&passport_account_image=VIMG_IDho6US3ggh17xXZDQJ7HxGGWjuAwWOylRH34yOal0bYA571ZOFrcSXA2SY3GSfWfzbC0Hy7g%2BxYAPyCkrzOWU3BSDiXJM5tUTyRZwSJZ9Fdsi7n46H8DVbnnNEP%2F6neKQ1AJ1FMNVuiBn9T03QlRz2b4ard%2FCDqXZO%2FtceDwIv6fn0OHal5dmvPWwuzO3ABw62siPKgSUpI66mU1j52K1QO5JaB9YmLIc8qKDrijunsy0QDy9Y87wNDlDE2YwsWhpq4bYYjZbBf0GPvoj0eityjyiawshklE6HKpmjb2fU8i49Y2XabdI8FOXKBWO5oAaMSzFsC3YXrEyhmPECCYxIJW5%2FSKmMUJSFhuZAMaPlLkWNvx3CDTTjSDV8Tzyt3lOOYwjRtX0u0bTGBqpD8aSSu2lXAeE12ulTdNg%3D%3D%24AI_418e70e1d3b38fe15fe748c549dcd322&token=&cs=false&__NS_sig3=bfaed1ed43be3eb38ff7f4f5d87635b9182c2e85eae6e8fe&country_code=cn'
    headers = {
            'kaw': 'MDHkM+9ErbyvSEMqyw6JZ2eIb3L/bGgOFNiqIfG6kS+gKDXDzcbtCZq8ttrY/ERt8qxzFaIxwGvvqUTkNoxR8Yjymu/lKeXh24qsDjEkDNYLoGE9jJGbytMAIV4x/JaN7pAx1AqYSmPJ/sbdgajix2uCY4NY8lQOXIdtKFRxJVhWl0yd9xPU1cIekPDkpV1i/MaN0PP4UcVmsPBfQohgc2GpXY/Cs6dzBI+ki/oP+zOTNTgQydhmWsl2HB3C8t08/w72M6LrstIP/GydA5KK3mtrfV+/zPj1Sww/ikessboA',
            'x-ktrace-id-enabled': '0',
            'x-forwarded-proto': 'https',
            'cookie': '__NSWJ=bssOqy7WnsY9eudP20MY8NuLmtx1clFXYaKWmQUaEYLWDxJezm99MCWkpcZoc7CNAAAAEQ==; apdid=bb46d02f-56a1-421f-a23d-e578c70070febefb6c42f8787d42260714193fd2ec94:1754815765:1; accessproxy_session=4c877d54-84a9-429d-802b-64439fb18dc7',
            'accept-language': 'zh-Hans-CN;q=1, zh-Hant-HK;q=0.9, en-CN;q=0.8, yue-Hant-CN;q=0.7',
            'x-kproxy-proto': 'https',
            'ct-context': '{"biz_name":"ATTRIBUTION","error_occurred":false,"sampled":false,"sampled_on_error":false,"segment_id":418462597,"service_name":"CLIENT_TRACE","span_id":1,"trace_id":"My4zMTgxMTE4Mjk0NjIxNDE5OTYuNzI2Ni4xNzU3NTk0NjE0NjM4LjM4","upstream_error_occurred":false}',
            'x-forwarded-for': '172.23.229.76',
            'x-requestid': '175759461463798969',
            'page-code': 'PHONE_NUMBER_LOGIN_PAGE',
            'accept': 'application/json',
            'x-real-ip': '172.23.229.76',
            'x-ksap-request-uuid': '04a4759b-a160-46ff-9bf4-2601b578236d',
            'x-ksclient-ip': '172.23.229.76',
            'x-kproxy-host': 'ks-server-api.staging.kuaishou.com',
            'content-type': 'application/x-www-form-urlencoded',
            'kas': '001a8e24e3d0e38de659e249ca4fd88f28',
            'x-client-info': 'model=iPhone16,2;os=iOS;nqe-score=-1;network=WIFI;',
            'user-agent': 'kwai-ios'
        }
    response = BaseAction().all_send_request(method='POST', url=url, headers=headers, data=payload)
    login_response = response.json()
    # token_value = jsonpath.jsonpath(login_response, "$.token")
    token = login_response.get('token')
    print(f'当前执行token为:{token}')
    return token



