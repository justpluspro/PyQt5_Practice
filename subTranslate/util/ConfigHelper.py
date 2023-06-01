import json


class ConfigHelper:
    """
    读取配置文件中的内容
    """

    def get_config(self):
        try:
            with open('D:/config.json', 'r', encoding='UTF-8') as file:
                return json.loads(file.read())
        except FileNotFoundError as e:
            with open('D:/config.json', 'w', encoding='UTF-8') as file:
                config_data = {
                    'translateProvider': [],
                    'sourceLang': [],
                    'targetLang': []
                }
                file.write(json.dumps(config_data))
                return config_data

    """
    更新配置文件
    """

    def update_config(self, config_data: dict):
        with open('D:/config.json', 'w', encoding='UTF-8') as file:
            file.write(json.dumps(config_data))


if __name__ == '__main__':
    config_data = {
        'translateProvider': ['百度', '腾讯', '亚马逊', '阿里云'],
        'sourceLang': ['英语', '中文', '德语', '西班牙语', '日语', '韩语'],
        'targetLang': ['英语', '中文', '德语', '西班牙语', '日语', '韩语']
    }
    config_helper = ConfigHelper()
    config_helper.update_config(config_data=config_data)
