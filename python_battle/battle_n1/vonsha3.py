#coding:gbk
'''
作者：lynn
行业：学生
学习时间：2周
介绍项目：类似橙光游戏那种的文字冒险游戏-。-
感受：这种活动挺好的，起码把循环写熟了，希望以后多搞~助教很认真，谢谢！
'''
# from __future__ import unicode_literals
from sys import exit
from random import randint


def death_xuan():
	print"结局：选秀落选"
	exit(1)
def death_yin():
	print"结局：饮鸩自尽"
	exit(1)
def death_bei():
	print"结局：被害而死"
	exit(1)
def death_da():
	print"结局：打入冷宫"
	exit(1)
def death_lao():
	print"结局：老死深宫"
	exit(1)
def death_han():
	print"结局：含冤而死"
	exit(1)
def win():
	print"结局：晋升成功！你赢了"
	exit(1)

def home_dad():
	print"林大人：浅殇，马上就要开始选秀了，爹爹想问问你的意思。"
	print"林浅殇：爹爹，就算我不同意就真的可以不去了吗？从我一出生您不是一直在等待着今日吗？"
	print"林大人：家族日渐败落。这可是我林家唯一翻身的机会，你既然姓林，就要为我林家夺得一片天下。"
	print"林浅殇：我从出生就知道我是巩固家族利益的工具，这点不用爹爹再提。"
	print"（望着这诺大的宫殿）鱼与熊掌向来不可兼得，而我林浅殇却皆要。"
	print"李嬷嬷：这里便是储秀宫，各位主子们这些日子便在这里居住，大家都是千挑万选进来的，相比都是懂些规矩的。选秀大典为三日后开选，希望各位主子们能尽展才能。"
	action = raw_input("1.给银子 2给簪子")
	if action == "1":
		print"1.你给李嬷嬷银子的时候，嬷嬷下意识的一推，正巧被路过的宁妃看到了，她便将你的名字从花名册里打掉了。"
		return"death_xuan"
	elif action == "2":
		print"林浅殇：（将发簪插进嬷嬷发间）嬷嬷的发簪掉了。"
		print"李嬷嬷：倒也是个有心的，不妨告诉你，陛下喜欢有才气的女子。"
		print"林浅殇：多谢嬷嬷提点。"
		return "xuanfangjian"
	else:
		print"超出范围，请重输"
		return"home_dad"

def xuanfangjian():
	print"宫女：房间是两人制的，一间房间两个人。"
	action = raw_input("1.住左边的 2.住右边的")
	if action == "1":
		print"宋秀女：（伸手拦住了你）这里已经有人住了，你住其他的地方吧。"
		action1 = raw_input("1.与其争吵 2.换个住所")
		if action1 == "1":
			print"马上就要选秀了，你却闹出这样的乌龙事件，皇后知道了，便将你们逐出皇宫。"
			return"death_xuan"
		elif action1 == "2":
			print"李秀女：咱们俩住一个房间啊，我叫李青青，你呢？"
			print"林浅殇：我叫林浅殇。"
			print"李秀女：嗯，以后我们就是好朋友了。"
			print"林浅殇：（好朋友。。。在我眼里只有权利）"
			return"shuzhuang_kanshu"
		else:
			print"超出范围，请重输"
			return"xuanfangjian"
	elif action == "2":
		print"安秀女：在哪都能碰见你，真实冤家路窄。"
		print"林浅殇：冤家其实也并不多，只是路不窄。"
		print"李秀女：咱们俩住一个房间啊，我叫李青青，你呢？"
		print"林浅殇：我叫林浅殇。"
		print"李秀女：嗯，以后我们就是好朋友了。"
		print"林浅殇：（好朋友。。。在我眼里只有权利）"
		return"shuzhuang_kanshu"
	else:
		print"超出范围，请重输"
		return"xuanfangjian"

def shuzhuang_kanshu():
	action = raw_input("1.梳妆 2.看书")
	if action == "1":
		print"（梳了一个美美的发型但是却没任何作用）"
		print"陛下喜欢有才气的女子"
		return"death_xuan"
	if action == "2":
		print"明月几时有，把酒问青天。不知天上宫阙，今夕是何年。"
		print"李秀女：听说陛下喜欢吃芙蓉糕。"
		print"林浅殇：你从哪里听来的。"
		print"李秀女：听宫女们说的啊"
		return"jiantaihou"
	else:
		print"超出范围，请重输"
		return"shuzhuang_kanshu"

def jiantaihou():
	print"太后：大家可曾读过什么书？"
	action = raw_input("1.四书五经 2.女戒 3.金瓶梅")
	if action == "1":
		print"林浅殇：臣女一直很喜欢四书五经。"
		print"皇帝有意无意看了你一眼（宠爱+5）"
		return"rugong"
	elif action =="2":
		print"林浅殇：臣女在家经常熟读的就是女戒。"
		print"太后：嗯，是个懂规矩的（心机+2）"
		return"rugong"
	elif action == "3":
		print"金瓶梅是禁读的，太后一怒之下赐你毒酒一杯。"
		return"death_yin"
	else:
		print"超出范围，请重输"
		return"jiantaihou"

def rugong():
	print"林大人：明天就要入宫了，收拾收拾吧。"
	print"林浅殇：爹爹放心，我林浅殇想要的谁也抢不走。"
	print"李嬷嬷：见过锦美人。"
	print"林浅殇：嬷嬷有礼了。"
	print"李嬷嬷：美人您的住所就在前面，同您一起进宫的有，安美人、李良人。"
	print"李嬷嬷：这里就是美人您的住所，奴婢就送您到这里吧，以后的路就由美人自己走了。"
	action = raw_input("1.给银两 2.给首饰")
	if action == "1":
		print"林浅殇：这些都是本宫的一些心意，还望姑姑收下。"
		print"李嬷嬷：没人真是客气了（人心+5）"
		return"mojuyuan"
	elif  action == "2":
		print"林浅殇：这是由玛瑙制成的簪子送与嬷嬷。"
		print"李嬷嬷：这么贵重的首饰奴婢不能要。（属性无任何变化）"
		return"mojuyuan"
	else:
		print"超出范围，请重输"
		return"rugong"
def mojuyuan():
	print"莲晴：主子，墨菊院已经打扫干净了，奴婢是您的一等丫鬟，院子里还有三等丫鬟两名，太监两名。"
	action = raw_input("1.打赏全部人 2. 树立威严")
	if action == "1":
		print"林浅殇：你去那些银两给大家分分吧，这么大的院子打扫起来可不容易呢。"
		print"莲晴：是主子（人心+2）"
		print"林浅殇：今日也折腾一天了，你们都退下吧。"
		print"一夜无梦"
		return"chujian_ning"
	elif action == "2":
		print"林浅殇：既然是跟着我了，以后我们都是一根线上的人了，该做什么不该做什么想必你自己心里也很清楚。"
		print"莲晴：奴婢明白（心机+2）"
		print"林浅殇：今日也折腾一天了，你们都退下吧。"
		print"一夜无梦"
		return"chujian_ning"
	else:
		print"超出范围，请重输"
		return"mojuyuan"

def chujian_ning():
	print"宁妃：瞧着今日进宫的各位妹妹，倒是让本宫想起，本宫刚进宫的场景了。"
	print"婉嫔：所以那一届进宫的人，竟没有一个人比得上姐姐啊。"
	action = raw_input("1.帮宁妃 2.帮婉嫔 3.默不作声")
	if action == "1":
		print"婉嫔本就不喜欢出风头的人，本就记恨宁妃，她为了不让宁妃势力庞大，所以对你下了手。"
		return"death_bei"
	elif action == "2":
		print"宁妃本就不喜欢出风头的人，本就记恨婉嫔，她为了不让婉嫔势力庞大，所以对你下了手。"
		return"death_bei"
	elif action == "3":
		print"宁妃：婉嫔妹妹，这张嘴真是不饶人啊。"
		print"婉嫔：妹妹是在给姐姐树立威信啊，姐姐可不能冤枉妹妹啊。"
		print"皇后：好了，时候也不早了，你们便退下吧。"
		print"婉嫔：在这宫里不是考心理战取胜的，而是要靠行动。"
		print"林浅殇：姐姐在说什么，妹妹听不懂。"
		print"婉嫔：懂不懂又有何关系，妹妹心里明白就好。"
		print"林浅殇：莲晴，你看我手中的花开得多好啊。"
		print"莲晴：这花能被主子折下，是它的福分。"
		print"林浅殇：你说命都没了，哪来的福分？"
		print"一夜好梦"
		return"huangshangjiadao"

	else:
		print"超出范围，请重输"
		return"chujian_ning"

def huangshangjiadao():
	print"皇帝驾到"
	action = raw_input("1.行礼 2.不行礼")
	if action == "1":
		print"林浅殇：见过陛下。"
		print"皇帝：你这是再煮些什么，这么清香。"
		print"林浅殇：回陛下，这是清晨摘的荷花，臣妾把他们清洗干净，暴晒几日，然后再煮成花茶。"
		print"皇帝：这种香气倒是能让人安神。"
		print"莲晴：主子好事，陛下今晚要来咱们这里。"
		action1 = raw_input("1.做些小菜 2.欲擒故纵")
		if action1 == "1":
			print"林浅殇：你去吩咐厨房去做一些菜。"
			print"莲晴：是，主子。"
			action2 = raw_input("1.为皇帝布菜  2.给皇帝夹菜")
			if action2 == "1":
				print"皇帝：爱妃辛苦了（宠爱+2）"
				print"一夜好梦"
				return"jinmeiren"
			elif action2 == "2":
				print"林浅殇：陛下，尝尝这个，这个御膳房一直做得不错。"
				print"皇帝:（给你夹了一块肉）多吃点（宠爱+5）"
				print"一夜好梦"
				return"jinmeiren"
			else:
				print"超出范围，请重输"
				return"huangshangjiadao"
		elif action1 == "2":
			print"你的欲擒故纵失败了，毕竟皇帝第一次来你这里，你不出来迎接，还把皇帝关在门外。"
			return"death_da"
		else:
			print"超出范围，请重输"
			return"huangshangjiadao"
	elif action == "2":
		print"你的宠爱度并没有达到可任性的程度"
		return"death_da"
	else:
		print

def jinmeiren():
	print"李公公：锦美人，淑慎性成，勤勉柔顺，率礼不越，性行温良，克娴内则，晋为锦贵人。"
	print"林浅殇：有老公公跑一趟了，这些都是本宫的一些心意，还望公公收下。"
	print"李公公：娘娘客气了，娘娘现在荣宠一身，以后还望娘娘多多提点着奴才呢。"
	print"婉嫔：妹妹好啊，妹妹进宫这么久，也不曾来向本宫请安，本宫只好亲自来跑一趟了。"
	action = raw_input("1.行礼 2.不行礼")
	if action == "1":
		print"林浅殇：臣妾给婉嫔姐姐请安。"
		print"婉嫔：本宫都来了这么久，妹妹就不请本攻进去喝杯茶吗。"
		print"林浅殇：姐姐身份尊贵，妹妹怕自己的茶入不了姐姐的口。"
		print"婉嫔：你知道吗，你现在叫以下犯上。"
		print"林浅殇：那妹妹想姐姐请罪，实在是寒舍简陋，不能屈尊姐姐贵体啊。"
		print"婉嫔：你。（甩袖而去）"
		return"jian_li"
	elif action == "2":
		print"你不行礼，婉嫔倒是没说什么，倒是被那些有心之人拿来大做文章。"
		return"death_lao"
	else:
		print"超出范围，请重输"
		return"jinmeiren"

def jian_li():
	print"莲晴：主子，李良人来了。"
	action = raw_input("1.不见 2.见")
	if action == "1":
		print"林浅殇：突然有些乏了，你让她先回去吧。"
		return"jianhuangshang"
	elif action == "2":
		print"林浅殇：让她进来吧。"
		print"李良人：听说姐姐晋升了，妹妹特地来恭喜姐姐，这是一点薄礼还望姐姐收下（人心+5）"
		print"林浅殇：（看着她手上的礼物，这可能是她能拿出来最好的礼物了）小厨房做了些点心，一会妹妹带回去些。"
		print"李良人：本来就是我为姐姐来贺喜，还要来拿姐姐东西。"
		print"林浅殇：（拉起她的手）我也不喜欢吃这些东西，你拿回去尝尝。"
		return"jianhuangshang"
	else:
		print"超出范围，请重输"
		return"jian_li"

def jianhuangshang():
	print"皇帝：（揉了揉太阳穴）"
	action = raw_input("1.给皇帝捶背 2.询问皇帝是不是有什么不舒服")
	if action == "1":
		print"林浅殇（走至皇帝身后，亲亲的为皇帝捶着背）"
		print"皇帝：（轻握住你的手）捶了这么久，可累了。（宠爱+5）"
		print"一夜好梦"
		return"anmeiren"
	elif action == "2":
		print"林浅殇：陛下，今日怎么看着您的心情不是怎么好，出什么事情了。"
		print"皇帝：没什么，咱们早些睡吧。"
		print"一夜无梦"
		return"anmeiren"
	else:
		print"超出范围，请重输"
		return"jianhuangshang"

def anmeiren():
	print"安美人：姐姐如今荣宠在身，都不怎么搭理妹妹了，妹妹的心真是。。。"
	print"林浅殇：表妹啊，从小你就是安家的掌上明珠，不知道安伯母知道你见我都得行礼是什么感受。"
	print"安美人:你。。。"
	print"林浅殇：太后娘娘，如今是越来越年轻了。"
	print"宁妃：（看向你）林妹妹这张嘴真是会说话啊。"
	print"太后：锦贵人说的就是不错，哀家也觉得现在是越来越年轻了。"
	print"宁妃：太后。。。"
	print"宁妃：林妹妹这张嘴可真是会说话，哄得太后娘娘真是，一套一套的。"
	print"林浅殇：妹妹再怎么说，也不敌姐姐的心思缜密，观察入微。"
	print"宁妃：你要知道，越是自作聪明的人越是活不了太久。"
	print"林浅殇：妹妹只知道，人不为己天诛地灭。"
	print"莲晴：娘娘怎么了。"
	print"林浅殇：这几日头一直在疼。"
	print"莲晴：奴婢去请太医给您看看吧。"
	action = raw_input("1.请太医 2.不请太医")
	if action == "1":
		print"太医：恭喜锦主子怀有身孕，不过您最近是不是一直都有些头痛。最近还是不要吃一些凉性的东西，头痛是最近可能主子休息的不太好了。"
		print"林浅殇：（温柔地看着自己的肚子）多谢太医。"
		return"jinguiren"
	elif action == "2":
		print"你已经中了毒，却还是没有请太医，便疯了。"
		return"death_lao"
	else:
		print"超出范围，请重输"
		return"anmeiren"

def jinguiren():
	print"李公公：锦贵人，聪慧敏捷，端庄淑睿，封为凝嫔。"
	print"林浅殇：五皇万岁万岁万万岁。"
	print"李公公：咱家在此恭喜娘娘了，双喜临门。"
	action = raw_input("1.赏金叶子 2.赏银子")
	if action == "1":
		print"林浅殇：这代金叶子还请公公笑纳。"
		print"李公公：娘娘，真是客气了（人心+5）"
		return"xiyangong"
	elif action == "2":
		print"林浅殇：这些银票还望公公收下。"
		print"李公公：那奴才也就收下了（人心+2）"
	else:
		print"超出范围，请重输"
		return"jinguiren"

def xiyangong():
	print"莲晴：娘娘，这夕颜宫真好。"
	print"林浅殇：只要孩子没什么事情，其他的事情应该都不重要了。"
	print"莲晴：娘娘，这夕颜宫可是大修了一番呢，听说宫殿的名字都是宁妃娘娘起的呢。"
	print"林浅殇：你可知道有一种花，名叫夕颜。"
	print"莲晴：夕颜，奴婢觉得这个名字挺好听的。"
	print"林浅殇：那你可知道，夕颜早上花开，日落时凋零。"
	print"莲晴：奴婢。。。奴婢。。。请娘娘恕罪。"
	print"林浅殇：罢了既然你不知道其深意本宫也不会怪你。"
	print"皇帝：爱妃觉得朕把这宫殿布置的可好"
	action = raw_input("1.恩很好。 2.只是这宫殿的名字")
	if action == "1":
		print"林浅殇：臣妾觉得很好（心机+2）"
		return"huaiyun"
	if action == "2":
		print"林浅殇：只是这宫殿的名字。。。"
		print"皇帝：爱妃不喜欢，这宫殿的名字是由宁妃想出的，最后由母后敲定的。"
		print"林浅殇：宁姐姐当真是博学多闻呢。"
		print"皇帝：（有点生气）这宫殿可是朕亲自督工，也不见你只言片语里提起朕。"
		action1 = raw_input("1.恭维皇上 2.开玩笑的说")
		if action1 == "1":
			print"林浅殇：陛下眼光最好了，臣妾很喜欢。"
			print"皇帝：是吗？"
			print"一夜好梦"
			return"huaiyun"
		elif action1 == "2":
			print"林浅殇：是是是，陛下的功劳最大。"
			print"皇帝：嗯。（宠爱+5）"
			print"一夜好梦"
			return"huaiyun"
		else:
			print"超出范围，请重输"
			return"xiyangong"
	else:
		print"超出范围，请重输"
		return"xiyangong"

def huaiyun():
	print"皇后：凝嫔如今怀有身孕，可要好好安胎啊。"
	print"林浅殇：臣妾知道。"
	print"宁妃：在这宫里不是一向是母凭子贵嘛，这况且是。。。"
	print"婉嫔：（掩嘴笑）宁妃姐姐您自己都没有孩子，怎么好意思说别人呢。"
	print"宁妃：我还是劝某些人，不要太得意了，小心报应来得太快。"
	print"林浅殇：（突然肚子疼的蹲下去）啊。"
	print"莲晴：娘娘，您怎么了，快来人啊。"
	print"皇后：凝嫔你醒了。"
	action = raw_input("1.问孩子 2.装睡")
	if action == "1":
		print"林浅殇：孩子，孩子？"
		print"皇帝：孩子，咱们还会有的。"
		print"李公公：不好了，陛下，不好了，婉嫔娘娘没了。"
		print"皇后：陛下，臣妾觉得这绝对不是一次简单的事情，先是凝嫔落胎，后是婉嫔自尽。"
		print"林浅殇：陛下，您要为臣妾和臣妾的孩子做主啊。"
		print"李公公：陛下，奴才今个在皇后娘娘的宫殿里的茶杯中发现了夹竹桃，又在婉嫔娘娘的宫中发现许多夹竹桃粉末。"
		action1 = raw_input("1.出言 2.不语")
		if action1 == "1":
			print"干嘛如此的心急呢，皇帝都没有发话"
			return"death_bei"
		elif action1 == "2":
			print"陛下，想必是婉嫔害了人，自己却承受不了心里的压力，所以。。。"
			print"皇帝：（沉默）\n(突然睁开眼睛）来人。婉嫔残害皇嗣，罪无可恕，而今废弃封号，其他的事情就由皇后处理吧。"
			print"皇后：是，陛下。"
			print"皇帝：（对你说）早些休息吧。"
			print"林浅殇：（突然的笑了）"
			print"莲晴：娘娘，您怎么了，要不要请太医。"
			print"林浅殇：莲晴你真的以为是婉嫔害了本宫的孩子吗，婉嫔有真的是自杀吗。"
			print"莲晴：娘娘。"
			print"林浅殇：宁妃，真是好手段一石二鸟。"
			return"qingan"
		else:
			print"超出范围，请重输"
			return"huaiyun"
	elif action == "2":
		print"这么个情况，你还在装睡。"
		return"death_bei"
	else:
		print"超出范围，请重输"
		return"huaiyun"

def qingan():
	print"宁妃：凝嫔妹妹刚没了孩子，还这么准时的来给皇后姐姐请安，本宫甚是佩服。"
	print"林浅殇：（在宁妃耳边说道）那也不及姐姐的好手段，一石二鸟还没自己什么事。"
	print"宁妃：（眼镜紧紧盯着你）所有人都可能知道是本宫干的，但他们没证据，谁又敢拿本宫怎么样呢。\n自然也比不过妹妹，刚失了孩子，还跟一个没事人的一样。"
	print"林浅殇：妹妹只知道，光痛苦是没什么用的，不是吗宁妃姐姐"
	print"皇后宫里没有人先开口说话，你要不要说？"
	action = raw_input("1.说 2.不说")
	if action == "1":
		print"林浅殇：姐姐宫里的茶，又换新样式了呢（心机+5）"
		print"皇后：妹妹既然喜欢，一会就带走些。\n前些日子喝一小口小产了，再多喝的话人没了怎么办。瞧我真不会说话，妹妹不要往心里去。\n林浅殇：姐姐无心的，妹妹知道。"
		return"xunwen"
	elif action == "2":
		print"皇后：妹妹们怎么都不说话呢，倒显得本宫这宫里冷冷清清的。\n安美人：皇后姐姐，今日茶叶瞧这很不错呢。\n宁妃：前些日子，凝嫔喝了一口就小产了，你还要天天喝。瞧我真不会说话，妹妹不要往心里去。\n林浅殇：姐姐无心的，妹妹知道。"
		return"xunwen"
	else:
		print"超出范围，请重输"
		return"qingan"

def xunwen():
	action = raw_input("1.询问皇帝去哪了 2.询问宁妃家世")
	if action == "1":
		print"林浅殇：陛下，现在在哪？\n莲晴：陛下，去了娘妃娘娘那里。"
		print"林浅殇：是吗，宁妃的家世如何？\n莲晴：宁妃娘娘的母家是当朝宰相，父家是礼部尚书。\n林浅殇：怪不得呢"
		return"bi_kaixin"
	elif action == "2":
		print"林浅殇：宁妃的家世如何？\n莲晴：宁妃娘娘的母家是当朝宰相，父家是礼部尚书。\n林浅殇：怪不得呢（心机+2）"
		return"bi_kaixin"
	else:
		print"超出范围，请重输"
		return"xunwen"

def bi_kaixin():
	print"林浅殇：陛下，今日看起来心情似乎是很好呢。\n皇帝：今日我国出站藩国大胜，朕今日当然开心。\n林浅殇：陛下开心，臣妾开心。\n皇帝：（突然握住你的手，好似想到了你前些日子的失子）朕一直都会在的。（宠爱+5）\n林浅殇：又是一年春天了。\n莲晴：是啊，娘娘今年的迎春花开得格外的好。"
	action = raw_input("1.与安美人聊天 2.与李良人聊天")
	if action == "1":
		print"林浅殇：又是一年呢。\n安美人：表姐荣宠在身自然什么不用自己操心。"
		return"chushi"
	elif action == "2":
		print"林浅殇：又是一年呢。\n李良人：嗯"
		return"chushi"
	else:
		print"超出范围，请重输"
		return"bi_kaixin"
def chushi():
	print"皇后：今年春节妹妹们都可以管好自己宫里的人，别出了什么事情。\n宁妃：有皇后姐姐不会出什么事情的不是吗。\n皇后：借妹妹吉言了。"
	print"林浅殇：（捂住胸口）最近总感觉会出什么事情，我着胸口这几日总是突突的跳。\n莲晴：娘娘，不好了，安美人她。。。没了。"
	action = raw_input("1.去皇后宫 2.询问怎么回事")
	if action == "1":
		print"宁妃：凝嫔你还不认罪，安贵人出事的池塘边为何有了你的手帕。"
		action1 =raw_input("1.辩解 2.认罪")
		if action1 == "1":
			print"林浅殇：陛下，臣妾今日一上午都未出过门，何来害安妹妹之说呢。\n宁妃：证据都摆在眼前了，妹妹为何还要一再辩解，心虚还是心里有愧。陛下还请明断，还安妹妹一个公道（开始抹眼泪）\n皇帝一怒之下将你抓入大牢。\n大牢中。\n李良人：姐姐，我在安美人院中发现一个机关盒子，或许里边有什么线索，我解不出，还望姐姐帮忙。一共可以试10次，我已试过5次，还剩5次机会。"
			print"提示：机关密码2位数"
			code = randint(1,100)
			print code
			guesses = 0
			while True:
				guess = input("请输入一个数：")
				if guess > code:
					print guess, "太大了"
					guesses += 1
					if guesses > 4:
						print"你没能解出机关"
						return"taopao"
						break
				elif guess < code:
					print guess, "太小了"
					guesses += 1
					if guesses > 4:
						print"你没能解出机关"
						return"taopao"
						break
				else:
					if guesses > 4:
						print"你没能解出机关"
						return"taopao"
						break
					print"你解出了机关\n原来安美人发现了婉嫔自尽的秘密，被皇后和宁妃联手害死。你发现后呈递皇上，皇上将皇后、宁妃抓入大牢。你获皇上独宠."
					return"win"
					break
		elif action1 == "2":
			return"death_han"
		else:
			print"超出范围，请重输"
			return"chushi"
	elif action == "2":
		print"你听到谣言，做出错误判断。"
		return"death_han"
	else:
		print"超出范围，请重输"
		return"chushi"



def taopao():
	print"你没能解出机关。\n深夜你趁守卫不备打算逃出大牢。\n你看到了5扇门，只有一扇门可以逃出去，其他的门都是死路。"
	action = raw_input("你选择哪扇门?（1/2/3/4/5）")
	if int(action) == randint(1,5):
		print"你选择了%d号门，你逃出了大牢"% int(action)
	else:
		print"你选择了%d号门，逃跑失败" %int(action)
		return"death_han"



ROOMS = {
	"death_xuan":death_xuan,
	"death_yin":death_yin,
	"death_bei":death_bei,
	"death_da":death_da,
	"death_lao":death_lao,
	"death_han":death_han,
	"win":win,
	"home_dad":home_dad,
	"xuanfangjian":xuanfangjian,
	"shuzhuang_kanshu":shuzhuang_kanshu,
	"jiantaihou":jiantaihou,
	"rugong":rugong,
	"mojuyuan":mojuyuan,
	"chujian_ning":chujian_ning,
	"huangshangjiadao":huangshangjiadao,
	"jinmeiren":jinmeiren,
	"jian_li":jian_li,
	"jianhuangshang":jianhuangshang,
	"anmeiren":anmeiren,
	"jinguiren":jinguiren,
	"xiyangong":xiyangong,
	"huaiyun":huaiyun,
	"qingan":qingan,
	"xunwen":xunwen,
	"bi_kaixin":bi_kaixin,
	"chushi":chushi,
	"taopao":taopao
}

def runner(map,start):
	next = start
	while True:
		room = map[next]
		print"\n-------------------"
		next = room()
runner(ROOMS,"home_dad")
