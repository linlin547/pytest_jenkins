import yaml

# 写入数据
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# yaml写文件
with open("./data3.yml", "a", encoding="utf-8") as f:
    # 调用yaml写如数据
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
