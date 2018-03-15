import codecs
import jieba
import text_regularization as tr

def savefile(savepath, content):
    fp = codecs.open(savepath, 'a', 'UTF-8')
    # with open(savepath, "a") as fp:
    try:
        fp.write(content+"\n")
    except Exception as e:
        print(content)


if __name__ == "__main__":
    input_files = ['not_ad.txt','ad.txt']
    output_files = ['not_ad','ad']
    for i,input_file in enumerate(input_files):
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                text = tr.extractWords(line)
                word_list = " ".join(jieba.cut(text))
                savefile(output_files[i], word_list)




