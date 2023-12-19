import configparser


class ConfigTool:
    def __init__(self, file_path='配置文件.ini', encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding
        self.config = configparser.ConfigParser()

    def write_config(self, sections):
        # 写入配置
        for section, options in sections.items():
            self.config[section] = options

        # 将配置写入文件
        with open(self.file_path, 'w', encoding=self.encoding) as configfile:
            self.config.write(configfile)

    def read_config(self, section, key):
        # 读取配置文件
        self.config.read(self.file_path, encoding=self.encoding)

        # 获取配置项的值
        value = self.config.get(section, key)

        return value
