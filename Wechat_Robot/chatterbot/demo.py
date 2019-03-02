# -*- coding: utf-8 -*-

from chatterbot import ChatBot

import logging

from chatterbot.trainers import ChatterBotCorpusTrainer

# Uncomment the following line to enable verbose logging

# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance

bot = ChatBot('Terminal',
              storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  "chatterbot.logic.MathematicalEvaluation",
                #   "chatterbot.logic.TimeLogicAdapter"
              ],
              filters=[
                  'chatterbot.filters.RepetitiveResponseFilter'
              ],
              input_adapter='chatterbot.input.TerminalAdapter',
              output_adapter='chatterbot.output.TerminalAdapter',
              database='chatterbot-xiaohuangji'
              )
bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('QingYun')
# bot.train("chatterbot.corpus.english")
# # 載入(簡體)中文的基本語言庫
# bot.train("chatterbot.corpus.chinese")
# # 載入(簡體)中文的問候語言庫
# bot.train("chatterbot.corpus.chinese.greetings")
# # 載入(簡體)中文的對話語言庫
# bot.train("chatterbot.corpus.chinese.conversations")
print('Type something to begin...')
while True:
    try:
        bot_input = bot.get_response(None)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
