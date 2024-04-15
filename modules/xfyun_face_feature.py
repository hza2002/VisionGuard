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

from utils.config import Config


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


class FaceDesc:
    def __init__(self, json):
        self.property = json["face_1"]["property"]

    def convert_beard(self):
        beard = int(self.property["beard"])
        if beard == 0:
            result = "没有胡子"
        elif beard == 1:
            result = "有胡子"
        else:
            result = "错误"
        self.property["beard"] = result

    def convert_expression(self):
        expression = int(self.property["expression"])
        if expression == 0:
            result = "惊讶"
        elif expression == 1:
            result = "害怕"
        elif expression == 2:
            result = "厌恶"
        elif expression == 3:
            result = "高兴"
        elif expression == 4:
            result = "悲伤"
        elif expression == 5:
            result = "生气"
        elif expression == 6:
            result = "正常"
        else:
            result = "错误"
        self.property["expression"] = result

    def convert_gender(self):
        gender = int(self.property["gender"])
        if gender == 0:
            result = "男人"
        elif gender == 1:
            result = "女人"
        else:
            result = "错误"
        self.property["gender"] = result

    def convert_glass(self):
        glass = int(self.property["glass"])
        if glass == 0:
            result = "不戴眼镜"
        elif glass == 1:
            result = "戴眼镜"
        else:
            result = "错误"
        self.property["glass"] = result

    def convert_hair(self):
        hair = int(self.property["hair"])
        if hair == 0:
            result = "光头"
        elif hair == 1:
            result = "短发"
        elif hair == 2:
            result = "长发"
        else:
            result = "错误"
        self.property["hair"] = result

    def convert_mask(self):
        mask = int(self.property["mask"])
        if mask == 0:
            result = "没戴口罩"
        elif mask == 1:
            result = "戴口罩"
        else:
            result = "错误"
        self.property["mask"] = result

    def __call__(self):
        self.convert_beard()
        self.convert_expression()
        self.convert_gender()
        self.convert_glass()
        self.convert_hair()
        self.convert_mask()
        return self.property


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
    config = Config()
    appid, api_key, api_secret = (
        config.cfg["xfyun"]["appid"],
        config.cfg["xfyun"]["api_key"],
        config.cfg["xfyun"]["api_secret"],
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
    print(decode_json)
    face_desc = FaceDesc(decode_json)
    translated_json = face_desc()
    return translated_json


if __name__ == "__main__":
    test_img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/know_face.jpeg"
    )
    print(run(test_img_path))
