import base64
import json
import os

# 从SKD包导入相应产品模块
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.iai.v20200303 import iai_client, models

from utils.config import Config


def describe_face_feature(data):
    face_features = data["FaceInfos"][0]["FaceAttributesInfo"]

    gender = "男性" if face_features.get("Gender") >= 50 else "女性"
    age = face_features.get("Age")
    expression = face_features.get("Expression")
    glass = "戴眼镜" if face_features.get("Glass") else "不戴眼镜"
    beauty = face_features.get("Beauty")
    hat = "戴帽子" if face_features.get("Hat") else "不戴帽子"
    mask = "戴口罩" if face_features.get("Mask") else "不戴口罩"
    eye_open = "睁眼" if face_features.get("EyeOpen") else "闭眼"
    hair = face_features.get("Hair")
    hair_length = {
        0: "光头",
        1: "短发",
        2: "中发",
        3: "长发",
        4: "绑发",
    }.get(hair.get("Length"), "Unknown")
    hair_bang = {0: "无刘海", 1: "有刘海"}.get(hair.get("Bang"), "Unknown")
    hair_color = {0: "黑色", 1: "金色", 2: "棕色", 3: "灰白色"}.get(
        hair.get("Color"), "Unknown"
    )

    description = {}
    description["Gender"] = gender
    description["Age"] = age
    description["Smile"] = expression
    description["Glass"] = glass
    description["Beauty"] = beauty
    description["Hat"] = hat
    description["Mask"] = mask
    description["Hair Length"] = hair_length
    description["Hair Bang"] = hair_bang
    description["Hair Color"] = hair_color
    description["Eye Open"] = eye_open

    return description


# 以二进制方式读取图片，然后对读取的图片进行base64编码和解码
def get_json(img_path):
    with open(img_path, "rb") as f:
        base64_data = base64.b64encode(f.read())
        base64_code = base64_data.decode()
    try:
        # 实例化一个请求-响应协议
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"  # 接口请求域名
        # 实例化一个客户端配置对象
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
        # 实例化一个认证对象
        config = Config()
        secretId, secretKey = (
            config.cfg["tencent"]["secret_id"],
            config.cfg["tencent"]["secret_key"],
        )
        cred = credential.Credential(
            secretId, secretKey
        )  # 传入腾讯云账户 secretId，secretKey
        client = iai_client.IaiClient(cred, "ap-beijing", clientProfile)  # 传入地域参数
        # 实例化一个请求对象
        req = models.DetectFaceRequest()

        # 人脸检测参数
        req.MaxFaceNum = 1
        req.Image = base64_code
        req.NeedFaceAttributes = 1
        req.NeedQualityDetection = 1
        req.NeedRotateDetection = 1

        # 通过 client 对象调用想要访问的接口，需要传入请求对象
        resp = client.DetectFace(req)
        # 输出 JSON 格式的字符串回包
        decode_json = json.loads(resp.to_json_string())
        return decode_json

    except TencentCloudSDKException as err:
        print(err)
    return None


def run(img_path):
    json_data = get_json(img_path)
    if json_data is None:
        return None
    return describe_face_feature(json_data)


if __name__ == "__main__":
    # 填入自己新建的访问密钥和图片的详细地址
    test_img_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../resource/know_face.jpeg"
    )
    face_feature = run(test_img_path)
    print(face_feature)
    print(type(face_feature))
