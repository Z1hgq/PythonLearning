
# coding:utf-8
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(unicode('Sally sells seashells by the seashore.'))
# engine.say(unicode('The quick brown fox jumped over the lazy dog.'))
# engine.runAndWait()

# import pyttsx3
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx
engine = pyttsx.init()
engine.say('你好啊')
engine.runAndWait()
# 朗读一次
engine.endLoop()


