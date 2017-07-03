 def send_msg(self,text):
        dict_user = slef.dict_user
        input_name = input('请输入微信联系人昵称,非本人备注:')
        # 注销这一句
        # txts = slef.txts
        friendList = itchat.get_friends(update=True)[1:]
        for friend in friendList:
            nice=friend['DisplayName'] or friend['NickName']
            User=friend['UserName']
            temp_user={nice:User}
            dict_user.update(temp_user.items())
        try :
            send_user=(dict_user.get(input_name))
            print(send_user)
            # 修改这一句
            # result=itchat.send(txts,send_user)
            result=itchat.send(text,send_user)
            print(result)
        except Exception as e :
            raise
