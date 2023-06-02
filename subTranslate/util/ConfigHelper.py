import json
import os

config_data = {
    'translateProvider': [],
    'sourceLang': [],
    'targetLang': []
}


class ConfigHelper:

    def __init__(self):
        self.config_path = os.path.join(os.path.expanduser('~'), 'config.json')

    """
    读取配置文件中的内容
    """

    def get_config(self):
        try:
            with open(self.config_path, 'r', encoding='UTF-8') as file:
                return json.loads(file.read())
        except FileNotFoundError as e:
            with open(self.config_path, 'w', encoding='UTF-8') as file:
                file.write(json.dumps(config_data))
                return config_data

    """
    更新配置文件
    """

    def update_config(self, data: dict):
        with open(self.config_path, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data))


if __name__ == '__main__':
    config_data = {
        'translateProvider': ['百度', '腾讯', '亚马逊', '阿里云'],
        'sourceLang': ['英语', '中文', '德语', '西班牙语', '日语', '韩语'],
        'targetLang': ['英语', '中文', '德语', '西班牙语', '日语', '韩语']
    }
    config_helper = ConfigHelper()
    config_helper.update_config(data=config_data)
    # print(os.getcwd())
    # print(os.path.expanduser('~'))
    # sys_platform = platform.platform().lower()
    # if "windows" in sys_platform:
    #     print('windows')
    # elif "macos" in sys_platform:
    #     print('macos')
    # elif "linux" in sys_platform:
    #     print('linux')
    # else:
    #     print('other')
