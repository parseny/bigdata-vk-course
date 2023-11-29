
from mrjob.job import MRJob, MRStep

class PhrasesPerPerson(MRJob):
    def mapper(self, _, line):
        character = line.lower().split('"')[3]
        words = line.lower().split('"')[-2]
        yield (character, 1)

    def combiner(self, character, counts):
        yield (character, sum(counts))

    def reducer(self, character, counts):
        yield None, (character, sum(counts))

    def reducer_top20_characters(self, _, character_count_pairs):
        character_count_pairs = list(character_count_pairs)
        character_count_pairs.sort(key=lambda x: x[1], reverse=True)
        for character, count in character_count_pairs[:20]:
            yield (character, count)

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_top20_characters)
        ]


if __name__ == '__main__':
    PhrasesPerPerson.run()
