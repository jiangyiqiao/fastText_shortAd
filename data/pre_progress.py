#coding=utf-8
import os

filenames=["ad","not_ad"]
output=open("fasttext_train.txt","w")

for filename in filenames:
    f = open(filename)             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法
    while line:
        line = f.readline()
        output.write(line.replace("\n"," ")+"\t__label__"+filename+"\n")
    f.close()

output.flush()
output.close()




