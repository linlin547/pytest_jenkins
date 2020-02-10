import os

import pytest
from Base.getData import GetData


def get_yaml():
    # 空列表
    data_l = []
    # 返回yaml文件中的数据
    data = GetData().get_yml_data("sum.yml")
    # 获取data字典的所有value
    for i in data.values():
        # 解析组装数据
        data_l.append(tuple(i.values()))

    return data_l

"""
目标：[(1, 2, 3), (2, 3, 5), (4, 5, 6)]
data={
'test_001': {'a': 1, 'b': 2, 'c': 3}, 
'test_002': {'a': 2, 'b': 3, 'c': 5}, 
'test_003': {'a': 4, 'b': 5, 'c': 6}
}
# 0.定义空列表存储数据
    data_l = []
# 1.获取data字典的所有value
    data.values()  # 返回结果列表 data_list = [{'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'b': 3, 'c': 5}, {'a': 4, 'b': 5, 'c': 6}]
# 2.遍历 data_list 取每一个小字典
    for i in data_list: # i={'a': 1, 'b': 2, 'c': 3} / i={'a': 2, 'b': 3, 'c': 5} / i={'a': 4, 'b': 5, 'c': 6}
        3. 取i.values()  # 返回结果 [1,2,3] [2,3,5]  [4,5,6]
        4.列表转元组
            tuple(i.values())  # 返回结果 (1,2,3) (2,3,5)  (4,5,6)
        5.追加元组到列表
            data_l.append(tuple(i.values()))
"""


class TestSum:
    # @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 3, 5), (4, 5, 6)])
    @pytest.mark.parametrize("a, b, c", get_yaml())  # 数据驱动方式
    def test_s(self, a, b, c):
        """
        计算两个数之和等于第三个数 a+b==c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print("\n{}+{}={}".format(a, b, c))
        # 断言
        assert a + b == c
