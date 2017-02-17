简易的爬取 IP 脚本

2017.2.17
<br>
1、文件说明
fetch_ip.py 是爬取 IP 的脚本，爬取了 3 个网站，觉得不够的话可以自己添加代码加入线程池。 extract_ip.py 是提取 IP 的脚本，提供 extract_ip() 函数作为调用接口，extract_ip() 会返回最新抓取的一个 IP 。
demo.py 是测试文件，包含了如何 import 以及使用提取接口。

2、使用方法：
将三个文件复制到自己的爬虫脚本文件夹下；
在爬虫脚本文件中导入 extract_ip() 函数，并完成自己的脚本。详见demo.py；
运行 fetch_ip.py 文件；
待 fetch_ip.py 爬取到可用的 ip 之后，运行爬虫脚本。