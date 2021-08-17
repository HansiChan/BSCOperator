import os
import sys

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
# 导入模块
from conf import settings
from core import BSCOperator

# 执行函数
if __name__ == '__main__':
    my_address = "0x2F42fCd8D06A840C242814ea5AaAa60699C3D69c"
    my_api_key = ""
    BSCOperator.getBNB_BALANCE(my_address, my_api_key)
