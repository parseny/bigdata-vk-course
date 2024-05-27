# Homework Description
There are two blocks in the task:

- Local cluster deployment 
- Writing map reduce in Python

## Part 1. Local cluster deployment

1. Deploy a local cluster in a configuration of: 
   - 1 NameNode
   - 1-3 DataNodes (depending on the available laptop capacity)
   - 1-2 NodeManagers
   - 1 ResourceManager

    You can do this either using [docker-compose](docker-compose.yaml), or by [instructions](https://youtu.be/ny2w5zImqvA).

2. - Examine the settings and status of NodeManager and ResourceManager in the web interface. 
   - Take screenshots of NameNode and ResourceManager. [Screenshots](homeworks/homework1/task1/screenshots). 
3. Run Jupiter. Create a notebook. 
4. Using python code (pyarrow), or using the ```hadoop fs``` commands, upload any data file to hdfs. 
5. Execute the command in separate cells
   ```!hadoop fs -ls (file path)```
   ```!hadoop fs -cat```
6. Run the command ```!hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 15 1800```
7. Add a [notebook](homeworks/homework1/task1/task1.ipynb) with the results, as well as [screenshots](homeworks/homework1/task1/screenshots) of ResourceManager launches.


## Part 2. Map Reduce Tasks

### [Task 1](homeworks/homework1/task2/1)
Find the top most talkative characters - count the number of replicas for each, and choose the 20 with the highest value.
Sort the results by the number of replicas (in descending order).
Provide the results for each episode, and separately for all three.

The results from hdfs should be read in a laptop and displayed on a [diagram](homeworks/homework1/task2/1/screenshots/rm_character_phrase_count.png).

### [Task 2](homeworks/homework1/task2/2)
#### Find the longest phrase of each character. 
The result must contain pairs (character name: his longest phrase), and must also be sorted back by phrase length.

Provide the results for each episode, and separately for all three.

### [Task 3](homeworks/homework1/task2/3)
#### Conduct a statistical analysis of the text of the episodes.

Each sentence in the text must be pre-cleaned: be reduced to a lowercase,
be cleaned of grammar and punctuation.

After clearing, the sentence should be split into bigram-s.

The answer should contain the 20 most frequent bigrams.

Cleaning should be done in the mapper code, ready-made bigram-s should be sent
to the reducer. 

The result of this part may differ depending on the quality of pre-cleaning,
this is the norm. 

The results of each run can be read and displayed on the chart in any convenient way.

Remember that we are in a distributed system. You need to install nltk dependency
not only in Jupiter, but also on NodeManager!

On the mapper side, you may need to perform additional initialization of the library:

```python
def mapper_init(self):
    nltk.download('punkt')
    nltk.download('stopwords')
```


It is mandatory to use the nltk library for text processing.

Provide the results for each episode, and separately for all three.