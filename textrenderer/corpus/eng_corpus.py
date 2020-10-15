from textrenderer.corpus.corpus import Corpus
import numpy as np


class EngCorpus(Corpus):
    """
    Load English corpus by words, and get random {self.length} words as result
    """

    def load(self):
        self.load_corpus_path()

        for i, p in enumerate(self.corpus_path):
            print("Load {} th eng corpus {}".format(i,p))
            with open(p, encoding='utf-8') as f:
                data = f.read()

            lines = data.split('\n')
            for line in lines:
                for word in line.split(' '):
                    word = word.strip()
                    #print(word,word in self.charsets)
                    word = ''.join(filter(lambda x: x in self.charsets, word))
                    

                    if word != u'':
                        self.corpus.append(word)
            print("Word count {}".format(len(self.corpus)))
            #print(self.corpus[:4000])

    def get_sample(self, img_index):

        # start = np.random.randint(0, len(self.corpus) - self.length + 1)
        # #print('self.length:',self.length)
        # words = self.corpus[start:start + self.length]

        english_word_num = np.random.randint(0,5)
        start = np.random.randint(0, len(self.corpus) - english_word_num + 1)
        #print('self.length:',self.length)
        words = self.corpus[start:start + english_word_num]
        word = ' '.join(words)
        if len(word)>36:
            word = word[:36]
        return word
