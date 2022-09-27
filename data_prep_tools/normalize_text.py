import os, sys
import codecs
import re

input_text = sys.argv[1]

output_name = '{}_clean'.format(input_text)
w = codecs.open(output_name, 'w', encoding='utf-8')

for line in codecs.open(input_text, 'r', encoding='utf-8').readlines():
    text = line.strip()
    text = text.replace("(","  ")
    text = text.replace(")","  ")
    text = text.replace("{","  ")
    text = text.replace("}","  ")
    text = text.replace("[","  ")
    text = text.replace("]","  ")
    #text = re.sub("[a-z]","  ", text)
    #text = re.sub("[A-Z]","  ", text)
    text = text.replace(".","  ")
    text = text.replace("_","  ")
    text = text.replace("·","  ")
    text = text.replace(",","  ")
    text = text.replace("?","  ")
    text = text.replace("!","  ")
    text = text.replace("~","  ")
    text = text.replace("\\","  ")
    text = text.replace("/","  ")
    text = text.replace("'","  ")
    text = text.replace('"',"  ")
    text = text.replace(":","  ")
    text = text.replace(";","  ")
    text = text.replace("…","  ")
    text = text.replace("*","  ")
    text = text.replace("`","  ")
    text = text.replace("<","  ")
    text = text.replace(">","  ")
    text = text.replace("‘","  ")
    text = text.replace("’","  ")
    text = text.replace("“","  ")
    text = text.replace("”","  ")
    text = text.replace("=","  ")
    text = text.replace("`","  ")
    text = text.replace("-","  ")
    #text = text.replace("ㅋ","  ")
    #text = text.replace("ㅂ","  ")
    #text = text.replace("ㄷ","  ")
    #text = text.replace("ㅍ","  ")
    #text = text.replace("ㅠ","  ")
    #text = text.replace("<9e>","  ")
    #text = text.replace("<200b>","")
    text = text.replace("100","백 ")
    text = re.sub("^ ","", text)
    text = re.sub(" $","", text)
    text = text.replace(".","  ")
    new_line = ' '.join(text.split())
    #new_line = line.split()[0] + "\t" + text
    #new_line = " ".join(new_line.split())
    w.write(new_line + '\n')

w.close()