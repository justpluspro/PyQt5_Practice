from PyQt5.QtWidgets import *

from subTranslate.util.ConfigHelper import *


# translate_provider = ['百度', '腾讯', '亚马逊', '阿里云']
# source_langs = ['英语', '中文', '德语', '西班牙语', '日语', '韩语']
# target_langs = ['英语', '中文', '德语', '西班牙语', '日语', '韩语']


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.text_edit = None
        self.config_helper = None
        self.setWindowTitle('Translate-Subtitle-file')

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit)

        h_layout = QHBoxLayout()
        first_layout = QVBoxLayout()
        translate_provider = QLabel('翻译服务商')
        translate_provider_combox = QComboBox()
        self.config_helper = ConfigHelper()

        config_data = self.config_helper.get_config()
        translate_provider_data = config_data['translateProvider']
        translate_provider_combox.addItems(translate_provider_data)
        first_layout.addWidget(translate_provider)
        first_layout.addWidget(translate_provider_combox)

        h_layout.addLayout(first_layout)

        second_layout = QVBoxLayout()
        source_lang = QLabel('源语言')
        source_lang_combox = QComboBox()
        source_lang_data = config_data['sourceLang']
        source_lang_combox.addItems(source_lang_data)
        second_layout.addWidget(source_lang)
        second_layout.addWidget(source_lang_combox)
        h_layout.addLayout(second_layout)

        third_layout = QVBoxLayout()
        target_lang = QLabel('目标语言')
        target_lang_combox = QComboBox()
        target_lang_data = config_data['targetLang']
        target_lang_combox.addItems(target_lang_data)
        third_layout.addWidget(target_lang)
        third_layout.addWidget(target_lang_combox)
        h_layout.addLayout(third_layout)

        h_layout.addStretch(1)
        start_btn = QPushButton('开始翻译')
        h_layout.addWidget(start_btn)
        main_layout.addLayout(h_layout)

        display_table = QTableWidget()
        main_layout.addWidget(display_table)

        self.setGeometry(720, 480, 150, 300)
        self.setLayout(main_layout)
        self.show()
