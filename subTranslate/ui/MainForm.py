from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from subTranslate.util.ConfigHelper import *
from subTranslate.components.ChooseFileTextArea import *


# translate_provider = ['百度', '腾讯', '亚马逊', '阿里云']
# source_langs = ['英语', '中文', '德语', '西班牙语', '日语', '韩语']
# target_langs = ['英语', '中文', '德语', '西班牙语', '日语', '韩语']


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.text_edit = None
        self.config_helper = None
        self.start_btn = None
        self.translate_provider_combox = None
        self.source_lang_combox = None
        self.target_lang_combox = None
        self.setWindowTitle('Translate-Subtitle-File')
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        self.file_input = ChooseFileTextArea()
        main_layout.addWidget(self.file_input)

        h_layout = QHBoxLayout()
        first_layout = QVBoxLayout()
        translate_provider = QLabel('翻译服务商')
        self.translate_provider_combox = QComboBox()
        self.config_helper = ConfigHelper()

        config_data = self.config_helper.get_config()
        translate_provider_data = config_data['translateProvider']
        self.translate_provider_combox.addItems(translate_provider_data)
        self.translate_provider_combox.setCurrentIndex(0)
        first_layout.addWidget(translate_provider)
        first_layout.addWidget(self.translate_provider_combox)

        h_layout.addLayout(first_layout)

        second_layout = QVBoxLayout()
        source_lang = QLabel('源语言')
        self.source_lang_combox = QComboBox()
        source_lang_data = config_data['sourceLang']
        self.source_lang_combox.addItems(source_lang_data)
        self.source_lang_combox.setCurrentIndex(0)
        second_layout.addWidget(source_lang)
        second_layout.addWidget(self.source_lang_combox)
        h_layout.addLayout(second_layout)

        third_layout = QVBoxLayout()
        target_lang = QLabel('目标语言')
        self.target_lang_combox = QComboBox()
        target_lang_data = config_data['targetLang']
        self.target_lang_combox.addItems(target_lang_data)
        self.target_lang_combox.setCurrentIndex(0)
        third_layout.addWidget(target_lang)
        third_layout.addWidget(self.target_lang_combox)
        h_layout.addLayout(third_layout)

        h_layout.addStretch(1)
        self.start_btn = QPushButton('开始翻译')
        self.start_btn.clicked.connect(self.start_translate_task)
        h_layout.addWidget(self.start_btn)
        main_layout.addLayout(h_layout)

        self.display_table = QTableWidget()
        # 设置表格只有三列
        self.display_table.setColumnCount(3)
        self.display_table.setFrameShape(QFrame.NoFrame)  ## 无边框表格
        self.display_table.setHorizontalHeaderLabels(['状态', '文件名', '说明'])
        self.display_table.horizontalHeader().setSectionsClickable(False) # 表头禁止点击
        # 让表头铺满整个 table 控件
        self.display_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        main_layout.addWidget(self.display_table)



        last_layout = QHBoxLayout()
        last_layout.addStretch(1)
        self.clear_btn = QPushButton('清空表格（不会删除文件）',)
        last_layout.addWidget(self.clear_btn)
        self.clear_btn.clicked.connect(self.clear_translate_task)

        main_layout.addLayout(last_layout)


        self.setMinimumSize(720, 480)
        self.setLayout(main_layout)
        self.show()

    def start_translate_task(self):
        # print(f'点击 {type(self.translate_provider_combox)}')
        translate_provider = self.translate_provider_combox.currentText()
        target_lang = self.target_lang_combox.currentText()
        source_lang = self.source_lang_combox.currentText()
        print(translate_provider, source_lang, target_lang)

        if source_lang == target_lang:
            QMessageBox.critical(self, '错误', '源语言和目标语言不能一致', QMessageBox.Cancel | QMessageBox.Close, QMessageBox.Cancel)
            return


    def clear_translate_task(self):
        print('清空表格')