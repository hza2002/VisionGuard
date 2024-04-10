# 人脸检测和属性分析 WebAPI 接口调用示例 运行前：请先填写Appid、APIKey、APISecret以及图片路径
# 运行方法：直接运行 main 即可
# 结果： 控制台输出结果信息
#
# 接口文档（必看）：https://www.xfyun.cn/doc/face/xf-face-detect/API.html

import base64
import hashlib
import hmac
import json
import os
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import requests
from dotenv import dotenv_values


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


# 进行sha256加密和base64编码
def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding="utf-8")
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3 :]
    schema = requset_url[: stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    u = Url(host, path, schema)
    return u


def assemble_ws_auth_url(requset_url, method="GET", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date = format_date_time(mktime(now.timetuple()))
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(
        host, date, method, path
    )
    signature_sha = hmac.new(
        api_secret.encode("utf-8"),
        signature_origin.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding="utf-8")
    authorization_origin = (
        'api_key="%s", algorithm="%s", headers="%s", signature="%s"'
        % (api_key, "hmac-sha256", "host date request-line", signature_sha)
    )
    authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode(
        encoding="utf-8"
    )
    values = {"host": host, "date": date, "authorization": authorization}

    return requset_url + "?" + urlencode(values)


def gen_body(appid, img_path, server_id):
    with open(img_path, "rb") as f:
        img_data = f.read()
    body = {
        "header": {"app_id": appid, "status": 3},
        "parameter": {
            server_id: {
                "service_kind": "face_detect",
                # "detect_points": "1", #检测特征点
                "detect_property": "1",  # 检测人脸属性
                "face_detect_result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "json",
                },
            }
        },
        "payload": {
            "input1": {
                "encoding": "jpg",
                "status": 3,
                "image": str(base64.b64encode(img_data), "utf-8"),
            }
        },
    }
    return json.dumps(body)


def run(img_path, server_id="s67c9c78c"):
    env_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/.env"
    )
    cfg = dotenv_values(env_path)
    appid, api_secret, api_key = (
        cfg["APPID"],
        cfg["APISECRET"],
        cfg["APIKEY"],
    )

    url = "http://api.xf-yun.com/v1/private/{}".format(server_id)
    request_url = assemble_ws_auth_url(url, "POST", api_key, api_secret)
    headers = {
        "content-type": "application/json",
        "host": "api.xf-yun.com",
        "app_id": appid,
    }
    response = requests.post(
        request_url, data=gen_body(appid, img_path, server_id), headers=headers
    )
    resp_data = json.loads(response.content.decode("utf-8"))
    decode_json = json.loads(
        base64.b64decode(resp_data["payload"]["face_detect_result"]["text"]).decode()
    )
    return decode_json


# 请填写控制台获取的APPID、APISecret、APIKey以及要检测的图片路径
if __name__ == "__main__":
    test_img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/know_face.jpeg"
    )
    print(run(test_img_path))
