
import requests

url = 'https://portal.cqucc.com.cn/zfca/login'

req = requests.get(url,verify=False)

print(req.text)


# 3月9晚20点，Crossin 斗鱼直播
#
# 这次的主题，是一个我快要被问疯掉的问题：
# Python 2 和 Python 3，我到底该学哪一个？
# 我会讲一讲它俩的区别，以及版本选择的建议。将重点比较下二者在字符编码这件事情上的变化。
# 依然欢迎现场提问。
# 直播间地址：https://www.douyu.com/crossin11
# 或在斗鱼上搜索 Crossin的编程教室
