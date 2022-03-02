import requests
import json
import re

def main():
    response = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.load(response.text)

    # 针对数据进行特定解析

def valid():
   username = input('输入用户名')
   qq = input('输入QQ号')

   m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
   if not m1\
           :
       print('无效用户名')

   m2 = re.match(r'^[1-9][0-9]{4,11}$', qq)
   if not m2:
       print('无效QQ')

if __name__ == '__main__':
    # main()
    valid()