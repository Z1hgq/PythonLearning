import itchat

itchat.auto_login()

arr = ['1','2','3','4','5','6','7','8','9','10']
for item in arr:
	itchat.send(item, toUserName='filehelper')