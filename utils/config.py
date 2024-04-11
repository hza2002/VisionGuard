import json
import os


class Config:
    def __init__(self):
        self.config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../resource/config.json"
        )
        self.cfg = self.load()

    def load(self):
        with open(self.config_path, "r") as file:
            return json.load(file)

    def save(self):
        with open(self.config_path, "w") as file:
            json.dump(self.cfg, file, indent=4)


if __name__ == "__main__":
    config = Config()

    print(config.cfg)
    # 保存修改后的配置
    config.save()
