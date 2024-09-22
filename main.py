import pandas as pd
from googletrans import Translator

translator = Translator()

text='나는 한국인이다.'
cn_result= translator.translate(text, dest='zh-cn')

#번역한 중국어를 다시 한국어로 바꿔보기
ko_result = translator.translate(cn_result.text, dest='ko')
print(cn_result.text) #我是韩国人。
print(ko_result.text) #나는 한국인이다.6