# coding=gbk
import random

def load_dict_from_open(data):
    dict={}
    try:
        with open(data,'r') as dict_data:
            for line in dict_data:
                (Cname,Ename)=line.strip().split(':')
                dict[Cname.decode('utf-8')]=Ename
    except IOError as ioerr:
        print "file %s is not exist"%(data)
    return dict


def select_one_from_dict(dict):
    dict_key=random.choice(dict.keys())
    print dict_key
    # print chardet.detect(dict_one)
    return dict_key

def print_to_user_then_input(dict_one):
    print dict_one
    userinput=raw_input("enter the name in English:")
    print userinput
    return userinput
def compare_userinput_and_default(dict_key,dict,userinput):
    dict_one_value = dict.get(dict_key)
    print dict_one_value

    if dict_one_value == userinput:
        print "correct"
        return True
    else:
        print "wrong"
        return False
if __name__=='__main__':
    # �����ļ������ֵ���������
    dict = load_dict_from_open('data.txt')
    # ѡ��һ������
    dict_one = select_one_from_dict(dict)
    # �� key ��ӡ���û�����ȡ����
    userinput = print_to_user_then_input(dict_one)
    # �Ƚ�
    compare_userinput_and_default(dict_one,dict,userinput)
