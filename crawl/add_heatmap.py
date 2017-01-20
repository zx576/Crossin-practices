
import re
import json
# 集合所有data
'''
def collectdata():
    all_data = set()
    for i in range(1,9):
        with open('E:/GIT/practice/Crossin-practices/crwal/uid_f_re/uid_%r.txt'%i,'r')as f:
            data = f.read()
        rule = re.compile('(\d{10})')
        res = re.findall(rule,data)
        res_set = set(res)
        all_data.update(res_set)
        print(len(res))
    alldata_list = list(all_data)
    # dic = {}
    # dic['alldata'] = alldata_list
    # with open('total_id.txt','w')as f:
    #     f.write(str(dic))
    # print(len(alldata_list))

    with open('repostdata.txt','r')as f2:
        re_d = f2.read()
    re_data = json.loads(re_d)
    re_data_list = re_data['repost_data']
    print(len(re_data_list))
    for i in re_data:
        if i in alldata_list:
            alldata_list.remove(i)
    print(len(alldata_list))
    dic = {}
    dic['alldata'] = alldata_list
    # print()
    with open('total_data_new.txt','w')as f3:
        f3.write(str(dic))

'''
#--------------------------------------------------------------------------
# 排除已经抓的id
# with open('total_id.txt','r') as f1:
#     total_d = f1.read()
#     # print(total_d)
# total_data = json.loads(total_d)
# print(type(total_data))
# total_data_list = total_data['alldata']
# print(len(total_data_list))
# with open('repostdata.txt','r')as f2:
#     re_d = f2.read()
# re_data = json.loads(re_d)
# re_data_list = re_data['repost_data']
# print(len(re_data_list))
# for i in re_data:
#     if i in total_data_list:
#         total_data_list.remove(i)
# print(len(total_data_list))
# dic = {}
# dic['alldata'] = total_data_list
# # print()
# with open('total_data_new.txt','w')as f3:
#     f3.write(dic)
# collectdata()

# with open('total_data_new.txt','r')as f:
#     data = f.read()
#
# data=re.sub('\'','\"',data)
# data1 = json.loads(data)
# print(type(data1))
