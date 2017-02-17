##简易的爬取 IP 脚本


####2017.2.17

####1、文件说明
<code>fetch_ip.py</code> 是爬取 IP 的脚本，爬取了 3 个网站，觉得不够的话可以自己添加代码加入线程池。
 <br>
 <code>extract_ip.py </code>是提取 IP 的脚本，提供 <code>extract_ip()</code> 函数作为调用接口，extract_ip() 会返回最新抓取的一个 IP 。
 <br>
<code>demo.py </code>是测试文件，包含了如何<code> import </code>以及使用提取接口。

####2、使用方法：
1. 将三个文件复制到自己的爬虫脚本文件夹下；
2. 在爬虫脚本文件中导入<code> extract_ip() </code>函数，并完成自己的脚本。详见<code>demo.py</code>；
3. 运行 <code>fetch_ip.py <code>文件；
4. 待 <code>fetch_ip.py</code> 爬取到可用的 ip 之后，运行爬虫脚本。