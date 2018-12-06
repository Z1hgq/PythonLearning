import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return meg.text

itchat.auto_login(hotReload=True)
itchat.run()