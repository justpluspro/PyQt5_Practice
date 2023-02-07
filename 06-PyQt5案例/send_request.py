import requests


class SendRequest:
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        res = SendRequest.sess.request(self, method=method, url=url, **kwargs)
        return res
