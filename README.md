# fastText_shortAd_Classification
## 微信广告正负样本分类
参考http://blog.csdn.net/lxg0807/article/details/52960072
## Dependencies
Only test under Unix-based System
 
the dependenceies is saved /usr/local/lib/python3.5/dist-packages/fastText,includeing FastText.py,please pay attention to the Uppercase 'F' 'T' and lowercase letters 'f' 't'.

    $ pip install jieba
    $ pip install fasttext

    # import fastText.FastText as fasttext 

正样本：

* xx,xxx,xxxxxxxxx

负样本：

* 微信公众号 AppSo，回复「钱包」看看微信钱包这 6 个秘密使用技巧
 
* 微信号：wszs1981
 
* 长按二维码关注
 

训练数据集：data/fastText_train.txt

输入数据为分词后带标签数据，数据预处理:

    python3 data/util/jieba_cut.py
    python data/pre_progress.py

测试数据集：data/fastText_text_100

查看运行结果：

    python2 fasttext.py

## result

    __label__ad:	 precision:1.000000	 recall:1.000000	 f:1.000000

