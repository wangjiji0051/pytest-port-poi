import requests


class BaseAction:
    def __init__(self):
        self.session = requests.Session()

    # 封装所有请求
    def all_send_request(self, **kwargs):
        return self.session.request(**kwargs)
