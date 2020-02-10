import os

import yaml


class GetData:
    """
        解析各种数据文件/数据库方法定义
    """

    def get_yml_data(self, yaml_name):
        """
        解析yaml文件
        :param yaml_name: 需要解析yaml文件名字
        :return: 返回yaml文件数据
        """
        with open("./Data" + os.sep + yaml_name, "r") as f:
            # 读取数据
            return yaml.safe_load(f)  # 返回yaml数据 字典格式

    def get_excel_data(self):
        """解析excel"""
