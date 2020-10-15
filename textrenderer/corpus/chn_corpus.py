import random
import numpy as np

from textrenderer.corpus.corpus import Corpus


class ChnCorpus(Corpus):
    def load(self):
        """
        Load one corpus file as one line , and get random {self.length} words as result
        """
        self.load_corpus_path()   ##產生self.corpus_path，corpus_dir路徑下所以txt文件的路徑

        for i, p in enumerate(self.corpus_path):
            print_end = '\n' if i == len(self.corpus_path) - 1 else '\r'
            print("Loading chn corpus: {}/{}".format(i + 1, len(self.corpus_path)), end=print_end)
            with open(p, 'r', encoding='utf-8') as f:
                data = f.readlines()

            lines = []
            for line in data:
                #line_striped = line.strip()
                line_striped = line.strip('\n').strip('\r\n').strip('  ')
                line_striped = line_striped.replace('\u3000', '')  ##'\u3000是中文文章的空格'
                line_striped = line_striped.replace('&nbsp', '')  ##&nbsp表示html中的空格
                line_striped = line_striped.replace('&emsp', '')
                line_striped = line_striped.replace(' ', '')
                line_striped = line_striped.replace('   ', '')
                line_striped = line_striped.replace("\00", "")    ##"\00"是python中的一種空格

                ##add by own
                #line_striped = line.strip('\n').strip('  ')

                if line_striped != u'' and len(line.strip()) > 1:
                    lines.append(line_striped)
            #print('lines:',lines)
            # 所有行合并成一行
            #split_chars = [',', '，', '：', '-', ' ', ';', '。']
            split_chars = [',', '，', '：', '-', ';', '。', ' ']
            percent_chars = [0.12]*6 + [0.28]
            #splitchar = random.choice(split_chars)
            splitchar = np.random.choice(split_chars,p=percent_chars)
            whole_line = splitchar.join(lines)
            #whole_line = ''.join(lines)

            # 在 crnn/libs/label_converter 中 encode 时还会进行过滤
            ##過濾出whole_lines在self.charsets的語料
            whole_line = ''.join(filter(lambda x: x in self.charsets, whole_line))
            #unsuportted_line = ''.join(filter(lambda x: x not in self.charsets, whole_line))
            #print('upsuport line:',unsuportted_line)
            #print('whole_line:',whole_line)

            if len(whole_line) > self.length:
                self.corpus.append(whole_line)

    def get_sample(self, img_index):
        # 每次 gen_word，随机选一个語料文件，随机获得长度为 word_length 的字符
        line = random.choice(self.corpus)

        min_length = 4
        max_length = 36
        length = np.random.randint(min_length, max_length)
        start = np.random.randint(0, len(line) - length)
        word = line[start:start + length]

        #start = np.random.randint(0, len(line) - self.length)

        #word = line[start:start + self.length]
        return word
