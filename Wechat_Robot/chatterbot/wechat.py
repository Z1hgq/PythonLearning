# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import itchat

bot = ChatBot('Terminal',
              storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch'
              ],
              filters=[
                  'chatterbot.filters.RepetitiveResponseFilter'
              ],
              database='chatterbot-database'
              )
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
# 載入(簡體)中文的基本語言庫
bot.train("chatterbot.corpus.chinese")
# 載入(簡體)中文的問候語言庫
bot.train("chatterbot.corpus.chinese.greetings")
# 載入(簡體)中文的對話語言庫
bot.train("chatterbot.corpus.chinese.conversations")



@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return bot.get_response(msg.text)

itchat.auto_login(hotReload=True)
itchat.run()
