# Databricks notebook source
# MAGIC %md ## Markdown content
# MAGIC Adding lists
# MAGIC - item 1
# MAGIC - item 2
# MAGIC - item 3
# MAGIC 
# MAGIC Links
# MAGIC [Queens Solus Website](http://my.queensu.ca)

# COMMAND ----------

# create a simple list of integers
data = xrange(1, 10001)

# COMMAND ----------

#check the length of that list
len(data)

# COMMAND ----------

# use SparkContext to create 8 cluster partitions and spread a dataset across them
ds = sc.parallelize(data, 8)

# COMMAND ----------

# show what the dataset like by collecting everything in the spark context
print ds.collect()
