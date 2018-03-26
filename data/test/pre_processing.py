#encoding:UTF-8
import codecs
import jieba
import text_regularization as tr


filenames=["ad.txt","not_ad.txt"]
output=open("fastText_test.txt","a")

for filename in filenames:
    with open(filename, 'r') as f:
        for line in f:        
            text = tr.extractWords(line)
            word_list = " ".join(jieba.cut(text))
            output.write(word_list.replace("\n"," ")+"\t__label__"+filename[:-4]+"\n")
    f.close()

output.flush()
output.close()





