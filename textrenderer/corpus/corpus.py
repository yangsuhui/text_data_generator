from abc import abstractmethod
import glob
import numpy as np

from libs.utils import load_chars


class Corpus(object):
    def __init__(self, chars_file, corpus_dir=None, length=None):
        self.corpus_dir = corpus_dir
        ##修改成变长的文字个数
        self.length = length

        self.corpus = []

        self.chars_file = chars_file
        ##self.charsets是字符串，是chars_file文件中所以字符組成
        self.charsets = load_chars(chars_file)
        #print('charsets:',self.charsets)

        self.load()

    @abstractmethod
    def load(self):
        """
        Read corpus from disk to memory
        """
        pass

    @abstractmethod
    def get_sample(self, img_index):
        """
        Get word line from corpus in memory
        :return: string
        """
        pass

    def load_corpus_path(self):
        """
        Load txt file path in corpus_dir
        """
        print("Loading corpus from: " + self.corpus_dir)
        self.corpus_path = glob.glob(self.corpus_dir + '/**/*.txt', recursive=True)
        if len(self.corpus_path) == 0:
            print("Corpus not found.")
            exit(-1)

