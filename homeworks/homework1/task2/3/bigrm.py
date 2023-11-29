
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from nltk.corpus import stopwords

class BigramCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper_get_bigrams,
                   reducer=self.reducer_count_bigrams),
            MRStep(reducer=self.reducer_find_top_bigrams)
        ]

    def mapper_init(self):
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')

    def mapper_get_bigrams(self, _, line):
        text = line.lower().split('"')[-2]
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        words = word_tokenize(text)
        words = [word for word in words if word not in stopwords.words('english')]
        for bigram in bigrams(words):
            yield bigram, 1

    def reducer_count_bigrams(self, bigram, counts):
        yield None, (sum(counts), bigram)

    def reducer_find_top_bigrams(self, _, bigram_counts):
        sorted_bigrams = sorted(bigram_counts, reverse=True)[:20]
        for count, bigram in sorted_bigrams:
            yield bigram, count

if __name__ == '__main__':
    BigramCount.run()
