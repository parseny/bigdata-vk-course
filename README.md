# Homework Description
There are three blocks in the task:

- Local cluster deployment and launching a Spark application
- Working with data in Spark
- Implementation of ML model prediction over text data using UDF
## Data description
A very popular set of movielens datasets is used as [data](https://grouplens.org/datasets/movielens/), which consists of:
- ratings (ratings.csv)
- tags (tags.csv)
- links (links.csv)
- films with genres (movies.csv)

In the hw, we will work with the first two datasets.

## Task 1. Spark application
#### Setting up Hadoop Cluster and Jupyter in Docker Environment

1. Deploy a Hadoop cluster with the following configuration:
   - 1 Namenode
   - 1 Datanode
   - 1 Resourcemanager
   - 1 Nodemanager

2. Also, deploy Jupyter in a container (all mentioned services are already available in [docker-compose](https://github.com/smalyshevv/bigdata-docker-pyspark)) (30 points)

3. Start a Spark session (SparkSession) with YARN master, 2 executors, and an application name ```{surname}_spark```. Before that, make sure to exit savemode in HDFS (```hdfs dfsadmin -safemode leave```).

4. Attach a [screenshot](notebooks/screenshots/yarn.png) of the YARN application where the application is running and a screenshot of the Spark application UI (30 points)

5. Read the tables ratings and tags from the [ml-latest-small](notebooks/ml-latest-small) directory; display the number of rows in both datasets. (Don't forget to transfer your data from the Jupyter container to HDFS:

## Task 2. Working with Data

1. Count the number of unique movies and unique users in the "ratings" table.

2. Count the number of ratings that are >= 4.0.

3. Display the top 100 movies with the highest rating.

4. Calculate the difference in time in seconds between the tagging time of a user for a given movie and the time when the user rated the movie. Output the average time delta.

5. Calculate the average rating from each user, and output the average of all the average ratings of all users.

Results should be in the same [notebook](notebooks/hw_spark.ipynb) as the previous task and written using PySpark methods without using `toPandas`.

## Task 3. Predicting Ratings Using Tags with TfidfVectorizer and SGDRegressor
1. Train a TfidfVectorizer on the "tag" column:
   - Convert the "tags" and "ratings" datasets to pandas using `.toPandas()`.
   - Train the TfidfVectorizer on the "tag" column.
   - Transform the "tag" column using the TfidfVectorizer to obtain numerical features.

2. Train an SGDRegressor:
   - Use the numerical features obtained from TfidfVectorizer as input.
   - Use the "rating" column as the label.
   - Train the SGDRegressor on these features and labels.

3. Write a UDF for predicting the rating based on the "tag" column:
   - Apply the TfidfVectorizer transform to the "tag" column.
   - Use the SGDRegressor to predict ratings from the numerical features obtained.
    
4. Apply the UDF to the Spark DataFrame and verify its functionality:
   - Apply the UDF to the Spark DataFrame containing the "tag" column.
   - Call an action (e.g., `show(50)`) to ensure the UDF works.
   - Attach a screenshot of the DAG for this job from the Spark UI. (15 points)

5. Calculate RMSE between predicted and true ratings:
   - Compute the root mean squared error (RMSE) between the predicted and actual ratings using PySpark.
   - Report the number of stages and tasks executed during this job. (10 points)

Results should be included in the same [notebook](notebooks/hw_spark.ipynb) from the first task.