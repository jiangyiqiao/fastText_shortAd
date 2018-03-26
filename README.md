# fastText_shortAd_Classification
## 微信广告正负样本分类
参考http://blog.csdn.net/lxg0807/article/details/52960072
## Dependencies
run success : python3

the dependenceies is saved /usr/local/lib/python3.5/dist-packages/fastText,includeing FastText.py,please pay attention to the Uppercase 'F' 'T' and lowercase letters 'f' 't'.

    $ pip install jieba
    $ pip install fasttext 

    # import fastText.FastText as fasttext 
    # also don't need to pip , directly import fastText
正样本：

* xx,xxx,xxxxxxxxx

负样本：

* 微信公众号 AppSo，回复「钱包」看看微信钱包这 6 个秘密使用技巧
 
* 微信号：wszs1981
 
* 长按二维码关注
 
其中，训练集正负样本各1W+，测试集样本各5K+

训练数据集： data/train/fastText_train.txt 
测试数据集： data/test/fastText_test.txt

输入数据为分词后带标签数据，数据预处理:

    python data/train/pre_processing.py
    python data/test/pre_progressing.py

测试数据集：data/test/fastText_text.txt 

训练模型：
   
    python train_model.py

测试模型：
   
    python test_model.py

## result

    __label__not_ad:	 precision:0.879189	 recall:0.992830	 f:0.932560
    __label__ad:	 precision:0.989747	 recall:0.835337	 f:0.906010


