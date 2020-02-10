# 导入yaml库
import yaml

# 读取文件
# with open("./data1.yaml", "r") as f:  # windows 会出现gbk编码错误
with open("./data2.yml", "r", encoding="utf-8") as f:  # windows
    # yaml库解析文件
    value = yaml.safe_load(f)  # 返回值 字典
    # 打印解析数据
    print("value={}".format(value))
    # 打印类型
    print("类型={}".format(type(value)))
