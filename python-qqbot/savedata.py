
from handle_r_dt import Resource_dt


ZHIHU_R = [
        ['微信机器人进化指南', 'https://zhuanlan.zhihu.com/p/26319288','微信;wechat;机器人','none'],
        ['喏，你们要的 PyCharm 快速上手指南', 'https://zhuanlan.zhihu.com/p/26066151','pycharm' ,'none'],
        ['世界上最伟大的巫师「咪蒙」', 'https://zhuanlan.zhihu.com/p/25927165', '咪蒙;运营','none'],
        ['给伸手党的福利：Python 新手入门引导', 'https://zhuanlan.zhihu.com/p/25824007','python;入门建议' ,'none'],
        ['只学2个月编程能写出什么代码？', 'https://zhuanlan.zhihu.com/p/25639903','编程展示;成果', 'none'],
        ['如何用100行Python代码做出魔性声控游戏“八分音符酱”', 'https://zhuanlan.zhihu.com/p/25499306','皮皮虾;声控;cocos2d;游戏', 'none'],
        ['还你系统空间的 Python 小程序', 'https://zhuanlan.zhihu.com/p/25231609','os;删除文件', 'none'],
        ['我去扒了杜蕾斯的微博', 'https://zhuanlan.zhihu.com/p/25208016', '杜蕾斯;echarts','none'],
        ['Python3.6新特性官方文档中文版', 'https://zhuanlan.zhihu.com/p/24550488', 'python3.6','none'],
        ['数据分析：当赵雷唱民谣时他唱些什么？', 'https://zhuanlan.zhihu.com/p/25109074','赵雷;数据分析;歌词分析','none'],
        ['一行代码扫出“敬业福”', 'https://zhuanlan.zhihu.com/p/25009370','支付宝;扫码', 'none'],
        ['ECharts+Python 给你的数据做“美颜”', 'https://zhuanlan.zhihu.com/p/24952863', 'echats','none'],
        ['在这个什么都看脸的时代，如何用 GUI 提高 python 程序的颜值？', 'https://zhuanlan.zhihu.com/p/24865235','gui' ,'none'],
        ['史上首个 Python x 微信小程序', 'https://zhuanlan.zhihu.com/p/24833133', '微信小程序','none'],
        ['个人开发者如何申请微信小程序', 'https://zhuanlan.zhihu.com/p/24810538', '微信小程序','none'],
        ['把你开发的网站免费发布到互联网上', 'https://zhuanlan.zhihu.com/p/24650061','网站部署;pythonanywhere', 'none'],
        ['今天，你抢到票了吗？', 'https://zhuanlan.zhihu.com/p/24606846', '抢票','none'],
        ['我在想，究竟是什么让编程“隔行如隔山”', 'https://zhuanlan.zhihu.com/p/24492294', '码上行动','none'],
        ['简单三步，用 Python 发邮件', 'https://zhuanlan.zhihu.com/p/24180606', 'email','none'],
        ['Python-Excel 模块哪家强？', 'https://zhuanlan.zhihu.com/p/23998083','excel', 'none'],
        ['用Python分析公开数据选出高送转预期股票', 'https://zhuanlan.zhihu.com/p/23829205', '股票','none'],
        ['NBA 举办编程马拉松 - 数据分析时代的到来', 'https://zhuanlan.zhihu.com/p/22917775', 'NBA;数据分析','none'],
        ['Hexo(2)-部署博客及更新博文', 'https://zhuanlan.zhihu.com/p/22498474', '网站部署;Hexo','none'],
        ['爆款游戏《贪吃蛇大作战》的 Python 实现', 'https://zhuanlan.zhihu.com/p/22339492','游戏;贪吃蛇;cocos2d', 'none'],
        ['Python 与 Excel 不得不说的事', 'https://zhuanlan.zhihu.com/p/22261597', 'excel','none'],
        ['用 GitHub + Hexo 建立你的第一个博客', 'https://zhuanlan.zhihu.com/p/22191919', '网站部署;Hexo','none'],
        ['想用 Python 做数据分析？先玩玩这个再说', 'https://zhuanlan.zhihu.com/p/21886694', 'TuShare;数据分析;财经','none'],
        ['用 Python 实现你的量化交易策略', 'https://zhuanlan.zhihu.com/p/21624000','量化交易', 'none'],
        ['极简 Github 上手教程', 'https://zhuanlan.zhihu.com/p/21438729', 'github','none'],
        ['如何在 Python 中使用断点调试', 'https://zhuanlan.zhihu.com/p/21304838','pycharm;断点调试', 'none'],
        ['Python 抓取网页乱码原因分析', 'https://zhuanlan.zhihu.com/p/21057822','编码分析;网页乱码', 'none'],
        ['如何在一台电脑上同时使用 Python 2 和 Python 3', 'https://zhuanlan.zhihu.com/p/20832723', '多版本;python','none'],
        ['如何安装 Python 的第三方模块', 'https://zhuanlan.zhihu.com/p/20760860', 'python;第三方模块','none'],
        ['如何直观地理解程序的运行过程？', 'https://zhuanlan.zhihu.com/p/20721034', 'python;理解程序','none'],
        ['编程初学者如何使用搜索引擎', 'https://zhuanlan.zhihu.com/p/20683456','搜索引擎', 'none']


]


we_r = [

['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166382&idx=3&sn=e6e9f45ae8f95391c621ef13a16db030&scene=0#wechat_redirect', '【我问 Crossin】python程序一闪而过,是我的打开方式不对?', '程序一闪而过;finally;input', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166445&idx=3&sn=9494649f6e16225148932080f3e3108e&scene=0#wechat_redirect', '【我问Crossin】程序猿该如何正确的使用搜索引擎?', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166343&idx=3&sn=b79779da7613bdc5b87f4ed81e7f67e5&scene=0#wechat_redirect', '【我问 Crossin】英语不好能不能学编程?', '换行;IDE文件保存;英语', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166411&idx=3&sn=eec9e79c6321f652dd103052e16b432b&scene=0#wechat_redirect', '【我问Crossin】学会 Python 离成为一名程序员还差多远?', 'invalidsyntax;selenium;python;就业', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166421&idx=3&sn=99d8c4a912a7797335088d0b92986157&scene=0#wechat_redirect', '【我问Crossin】爬虫学习该如何入门?', 'list;exe;爬虫学习', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166396&idx=3&sn=c57adcd8ef18d2d498901741851a9777&scene=0#wechat_redirect', '【我问 Crossin】想转行做后端开发,要多久?', 'sys.argv;re;圆括号指定分组;后端开发', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166065&idx=1&sn=a7e844d663cd17cd4a3b6829910bf879&scene=0#wechat_redirect', '编程教室招收实训生', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166229&idx=1&sn=184ebef46fb29a0e8cf2dc00f2b543f4&scene=0#wechat_redirect', '个人开发者如何申请微信小程序', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166062&idx=1&sn=af4df4f252441594f5aaaca0fafde00d&scene=0#wechat_redirect', '爆款游戏《贪吃蛇大作战》的Python 实现', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166225&idx=1&sn=237d39c0fbb146580e728db85f669922&scene=0#wechat_redirect', '还你系统空间的 Python 小程序', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166235&idx=1&sn=b358785fd8985d21ccfd30d89c628e7c&scene=0#wechat_redirect', '我们的小程序上线啦!', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166411&idx=2&sn=86e4d3e9e18ba2cf1aabe22b11fc2c6a&scene=0#wechat_redirect', '【编程课堂】震惊!小bug 引发大灾难,0.1 + 0.2 的结果竟然是……', '浮点数精度', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=209449188&idx=1&sn=61b4ff775c7bea698a208747a2e40d51&scene=0#wechat_redirect', '获取编程新技能的5个技巧', '提升编程能力;获取新知识', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166246&idx=1&sn=dd634d6c8df1e47463842a491e2bab4e&scene=0#wechat_redirect', '在这个什么都看脸的时代,如何用 GUI 提高 python 程序的颜值?', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=209152876&idx=1&sn=c5c72349b9e7394b6d7aa9ca7c430b9a&scene=0#wechat_redirect', '学习编程的七个阶段', '学习编程', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166414&idx=1&sn=c8d63efa7f0bac98ffb8edcde52331e1&scene=0#wechat_redirect', '喏,你们要的 PyCharm 快速上手指南', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166398&idx=1&sn=60c26ab0f2d43a019217812e0c428f31&scene=0#wechat_redirect', '再也不用担心错过几个亿啦:基于Python的微信消息防撤回工具', '微信;wechat', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166411&idx=1&sn=305bd7ec420104c0b33a686ce154f82c&scene=0#wechat_redirect', '【每周一坑】选择困难的农药召唤师', '每周一坑;王者荣耀', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=210734953&idx=1&sn=09172302f1cc13cae300918072e4f8d1&scene=0#wechat_redirect', '编程学习中的瓶颈', '学习编程', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=208550863&idx=1&sn=582dbe7cecb54d5e07a3701f7e8df557&scene=0#wechat_redirect', '新手学习编程的最佳方式是什么?', '学习编程', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=401601518&idx=1&sn=24a433b15c077118debbd95104eea59e&scene=0#wechat_redirect', '[调查]关于编程学习的几个问题', 'none', 'none'],
['e', '把你开发的网站免费发布到互联网上(1)', 'pythonanywhere;网站部署', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=203858320&idx=1&sn=b806cd211fb345ad4652d574602c1981&scene=0#wechat_redirect', '国外大牛程序员的工作环境', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=206097870&idx=1&sn=2f8c0e8a3c87af6613b75878fc77a99b&scene=0#wechat_redirect', '每一个程序员要遵守的一些优秀编程风格', '学习编程;编程规范', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=204850879&idx=1&sn=ca42a4c133e0dbaadb3d358daa8e2d45&scene=0#wechat_redirect', '帮助孩子学习编程的12种游戏', '学习编程', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166206&idx=1&sn=dc302be69e9007461b70b0f9d4cb7e2b&scene=0#wechat_redirect', '把你开发的网站免费发布到互联网上(2)', 'pythonanywhere;网站部署', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166108&idx=1&sn=de601842552d3432f23206d7fe01934f&scene=0#wechat_redirect', 'python list 排序的两种方法及实例讲解', 'list;排序', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166294&idx=1&sn=d269ebe2c60d3103aa9d9b7764714dfd&scene=0#wechat_redirect', '突破反爬虫的利器:开源IP代理池', 'IP池', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=204255757&idx=1&sn=a571a1abb6e75b847feeb40e2c6e4f23&scene=0#wechat_redirect', '【python课程】编程中的一个实用函数', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166209&idx=1&sn=ca591790a67f95fe3c45c883f7614f91&scene=0#wechat_redirect', '2016,你的小目标完成了吗?', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166153&idx=1&sn=ff100f4e6278709550170d2d97f905bb&scene=0#wechat_redirect', 'ECharts+Python 给你的数据做“美颜”', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=202286091&idx=1&sn=50d0344849e1b324b78d4380ea754b57&scene=0#wechat_redirect', '程序员的成长和代码行数的关系', '学习编程;技术进步', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=400537608&idx=1&sn=a5346c41915583332e72605b19dae672&scene=0#wechat_redirect', '浅谈 Python 2 中的编码问题', '编码', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=402266805&idx=1&sn=cb43d729830eae4667917f7d5f1ca373&scene=0#wechat_redirect', '测试你的红包代码', '红包', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166002&idx=1&sn=d9eb71cf4df8c2aefba86fdc960b8881&scene=0#wechat_redirect', '用Python 实现你的量化交易策略', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=210493369&idx=1&sn=dad8797d985e81e797600aa3522f4678&scene=0#wechat_redirect', '女程序员的成功秘诀', '女程序员', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166264&idx=2&sn=cb1001f5c5358d7f6c9d0c653ae1c69c&scene=0#wechat_redirect', 'Windows 下的包管理器', '包管理', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650165936&idx=1&sn=10dc48e8cb2783e7188786815c9e218b&scene=0#wechat_redirect', 'Python爬虫:一些常用的爬虫技巧总结', '爬虫技巧', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=400022452&idx=1&sn=705a50d47478950d55cb75e0bdaaf3f4&scene=0#wechat_redirect', '编写让别人能读懂的代码', '编程规范', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650165920&idx=1&sn=dc5b2777a5ca813a50f82c84102748e4&scene=0#wechat_redirect', '如何直观地理解程序的运行过程?', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166025&idx=1&sn=50a22c1953f57db0240ca2d1363ba47a&scene=0#wechat_redirect', '用GitHub + Hexo 建立你的第一个博客', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166127&idx=1&sn=111468d2976d0c5e24d7dcd67c943550&scene=0#wechat_redirect', '2016年,上海的互联网企业是否值得加入?', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166045&idx=1&sn=5cd4224789ec34e799d7a765e2c94cf3&scene=0#wechat_redirect', 'Python 与Excel 不得不说的事', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=211255727&idx=1&sn=2068f605e88781ddca2436fd49aac254&scene=0#wechat_redirect', '新手程序员应该知道的7件事', '学习编程;新手问题', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=402682269&idx=1&sn=d708a299ebf9c3571df7a7c87595a39f&scene=0#wechat_redirect', '一些常见的新手问题', '学习编程;新手问题', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650165984&idx=1&sn=0af4ccc46587dba1d6961e9686f70401&scene=0#wechat_redirect', '10个对Web开发者最有用的Python包', 'web开发', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=204451282&idx=1&sn=996770f5912f02578b78fcfacd62c52e&scene=0#wechat_redirect', '成为优秀程序员的10个有效方法', '学习编程;技术进步', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166056&idx=1&sn=5693b76cd7528d76305f420deb2f2598&scene=0#wechat_redirect', 'Hexo(3)-安装自己喜欢的主题', 'hexo;网站部署', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=402183749&idx=1&sn=ddcae87f76233c5286bc947ad9d5552f&scene=0#wechat_redirect', '用Python 实现一个简单的微信红包算法', '微信;红包', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650165933&idx=1&sn=85c170e4bd7080c6bf28be1342058fdb&scene=0#wechat_redirect', '关于“码上行动”的几点说明', '码上行动', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166100&idx=1&sn=312b70a1bd3e74a062a76d4ee185db77&scene=0#wechat_redirect', 'NBA 举办编程马拉松 - 数据分析时代的到来', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650165923&idx=1&sn=a455a2b75eb29c7ab03ca1ded0d03427&scene=0#wechat_redirect', '如何安装 Python 的第三方模块', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=203369586&idx=1&sn=8073abc5a69730708a2957059be28cea&scene=0#wechat_redirect', '验证码的故事 (1)', '验证码', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=211556366&idx=1&sn=127f07d790903a2aff50b9f05f6992a4&scene=0#wechat_redirect', '关于 Git 你不知道的十件事', 'git', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=205604444&idx=1&sn=46b8fe66846a0b250718f98a1eb5cfab&scene=0#wechat_redirect', 'Python 实战(2):简单的数据库', '数据库', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=205848780&idx=1&sn=b17567b2ecb067cf0baa4b2cb733a3fe&scene=0#wechat_redirect', 'Python 实战(3):更多的页面', '页面', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=209587273&idx=1&sn=3ed756b3d07f6ffab883c8d6a2a931af&scene=0#wechat_redirect', '为什麽成为一名工程师这麽难 —— 从程式新手到准工程师的必经之路', '学习编程;新手问题', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10021105&idx=1&sn=c33e44bb6e56bb23ff524a34d292a024&scene=0#wechat_redirect', '【Git 第63课】python 2到3的新手坑', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=400142129&idx=1&sn=d4d13ba952f53ab3fe69a722a1366d0d&scene=0#wechat_redirect', '我前妻的故事(一个初中肄业生的奋斗)', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=200653400&idx=1&sn=b75ec3e38dfd62e2c17e2cb68948eb5f&scene=0#wechat_redirect', '写给新手程序员的一封信', '新手问题', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000146&idx=1&sn=c6814bec2bcd1d26a2c3c68cad21265f&scene=0#wechat_redirect', '【Python 第33课】 处理文件中的数据', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000096&idx=1&sn=9fad5342f695d42f89a797744a70d5da&scene=0#wechat_redirect', '【Python 第21课】 函数的参数',/ 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000173&idx=1&sn=a2701c84fde8da84bf50012cdebacd2e&scene=0#wechat_redirect', '【Python 第42课】 函数的默认参数', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=210665630&idx=1&sn=85097e1be49b842cedf7777c3620ff2e&scene=0#wechat_redirect', '从Side Project到人均产值超越Google,他是如何做到的?', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000220&idx=1&sn=543332b23d372a339884141c557d5ecf&scene=0#wechat_redirect', '【Pygame 第2课】 游戏的本质', 'pygame', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=400291466&idx=2&sn=abd5837459dcf903855b24575ec9dc40&scene=0#wechat_redirect', '技术角度揭秘百万日订单背后的挑战与应对', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=200368047&idx=1&sn=4b183c93cf00160950df5c9d879ba196&scene=0#wechat_redirect', '【Python 第67课】函数的参数传递(1)', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=200398124&idx=1&sn=3c4a153a74e32e3d97a723e0f94de58a&scene=0#wechat_redirect', '【Python 第68课】函数的参数传递(2)', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=200462413&idx=1&sn=97324ec5d341dea053f62f2e0cbfc68a&scene=0#wechat_redirect', '【Python 第69课】函数的参数传递(3)', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000230&idx=1&sn=0c61168090ba27fb1ebe4b9cbe5b3055&scene=0#wechat_redirect', '【Pygame 第3课】 游戏中的事件', 'pygame', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000246&idx=1&sn=d6fcdefb0ebb3cdc8a9315265dd2b872&scene=0#wechat_redirect', '【Pygame 第6课】 面向对象的游戏设计', 'pygame', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000308&idx=1&sn=066b6371a875a31e8f9f7b70b43b4621&scene=0#wechat_redirect', 'python模块的常用安装方式', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000249&idx=1&sn=36c734f9ee44c7f71347c71f1549f922&scene=0#wechat_redirect', '【Pygame 第7课】 多变的宿敌', 'pygame', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000311&idx=1&sn=3f69b87bd4e48215973f629fb5ef534d&scene=0#wechat_redirect', '用python武装你的后院', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000295&idx=1&sn=bcb353417a892a0fe320899a7cad18e7&scene=0#wechat_redirect', '那些年,他们一起用的python', 'python商业应用', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000350&idx=1&sn=eb97c4500eeadb4f5ef52c20cc75b167&scene=0#wechat_redirect', '几道有趣的概率题', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=10000329&idx=2&sn=f6a0cf1927ba6af39c710ddbb5c9a7c7&scene=0#wechat_redirect', '来自Byron同学的解答', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166433&idx=1&sn=5d5c9ace9aa7d19a286af5d1a919d208&scene=0#wechat_redirect', '21天精通编程', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166286&idx=1&sn=4f1c6127522df4f75f94cb6cbdf3c1ed&scene=0#wechat_redirect', '一行代码扫出“敬业福”', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166421&idx=2&sn=699f4e287c9b3db002904b2c039869b6&scene=0#wechat_redirect', '【编程课堂】海龟作图', '编程课堂;海龟作图', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166374&idx=1&sn=8034a349ea77eb8b3bcec546c0261054&scene=0#wechat_redirect', '只学2个月编程能写出什么代码?他们表示:You can you code!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166174&idx=1&sn=52ad0f6479c9e64643a3d24b1dabd33c&scene=0#wechat_redirect', '我在想,究竟是什么让编程“隔行如隔山”', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=401256685&idx=1&sn=056d43f3f798e2755879152a5a7c502f&scene=0#wechat_redirect', '网上看到的一组一秒钟炸醒装睡的人的技能,转需!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=202658868&idx=1&sn=664a3e527cd0778c27c86c8b7b63c7b6&scene=0#wechat_redirect', '一个男人需要挣多少钱才能维系一个家庭?很震惊的数据!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166386&idx=2&sn=86dce4dabeacce4605b16e7a4119f43f&scene=0#wechat_redirect', '第一届“You Can You Code”杯编程小赛评比结果', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166343&idx=2&sn=ca8bbc637c61fe5f2c327572e604d0af&scene=0#wechat_redirect', '【编程课堂】计数器 Counter', '编程课堂;counter', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=203989530&idx=2&sn=df78a8be75a9a149a66d6ae05095831a&scene=0#wechat_redirect', '又一段逆天的视频:在删之前看一看吧!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=400961173&idx=2&sn=c727c95c39de99977b62dbcb132419ca&scene=0#wechat_redirect', '世界上过亿的八辆车,让朋友开眼了!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=208561900&idx=3&sn=2e18408db2776346297d120c03499021&scene=0#wechat_redirect', '最近超火的一组图,其中的含义你看懂了吗?', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=204271971&idx=1&sn=c060f4bf92f453171a486b6a94ffcb83&scene=0#wechat_redirect', '女汉子是怎样上床的?没有比这更屌爆的了!', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166396&idx=2&sn=05efda7315ef02fc725da1e739365d90&scene=0#wechat_redirect', '【编程课堂】词云 wordcloud', '编程课堂;wordcloud', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=207321585&idx=1&sn=baf29d2768bbadac562853862ad6b7c1&scene=0#wechat_redirect', '现在的妹子都是这么饥渴吗?', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=402217581&idx=4&sn=ed84d8fb3bac51485cc6a182d0c37282&scene=0#wechat_redirect', '网上疯转的一道数学题,小伙伴们赶快来战!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=207031872&idx=1&sn=899d4a77a561f4fa23fb12396132816f&scene=0#wechat_redirect', '秘女人的身体艺术,美到极致.', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=205047913&idx=1&sn=c62dde48c27f050d6b1d95612b4623a0&scene=0#wechat_redirect', '夫妻间的恶作剧,未婚情侣慎学~', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=203766666&idx=1&sn=a28c524c1ecf6b85209ed0e330694412&scene=0#wechat_redirect', '据说这是蓝翔的期中考试,期末考试是从上往下~', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166333&idx=1&sn=e640b812fef7fde36d00b63a508a381f&scene=0#wechat_redirect', '如何用100行Python代码做出魔性声控游戏“八分音符酱”', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=202146968&idx=1&sn=eaee1e87c00889cd95688d9e751d2820&scene=0#wechat_redirect', '男人,一生都在寻找的,不是一个妻子,也不是一个情人,而是一个红颜知己!', 'none', 'none'],
# ['http://mp.weixin.qq.com/s?__biz=MzA4MTYxMTAxMw==&mid=204299608&idx=3&sn=823d74eb9722237bd9988b82d1fb87e5&scene=0#wechat_redirect', '开始,我以为她只是个充气的,结果.不科学啊!', 'none', 'none'],
['http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=2650166015&idx=1&sn=9c1b46ffaad707e4967358afb8cc8746&scene=0#wechat_redirect', '在Python 程序中显示进度条', '', 'none'],


]




dt = Resource_dt()

res = dt.extract_item_by_id(83)
print(res)
# for i in we_r:
#     print(i)
#     dt.insert_item(i[1],i[0],i[2],i[3])
#     print('ok')

# for i in we_r:
#     if len(i) != 4:
#         print(i)

# sql =
