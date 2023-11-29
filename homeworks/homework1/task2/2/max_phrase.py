
from mrjob.job import MRJob, MRStep

class MaxPhrasePerPerson(MRJob):
    def mapper(self, _, line):
        character = line.split('"')[3]
        words = line.split('"')[-2]
        yield (character, (words, len(words)))
               
    def reducer(self, character, phrase_len_pair):
        max_len_phrase, len = max(phrase_len_pair, key=lambda x: x[1])
        yield None, (character, max_len_phrase, len)

    def reducer_sort_phrases(self, _, character_phrase_len):
        character_phrase_len = list(character_phrase_len)
        character_phrase_len.sort(key=lambda x: x[2], reverse=True)
        for character, phrase, len in character_phrase_len:
            yield character, phrase

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_sort_phrases)
        ]


if __name__ == '__main__':
    MaxPhrasePerPerson.run()
