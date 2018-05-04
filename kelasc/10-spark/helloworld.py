# Import sparkcontext
from pyspark import SparkContext

# Inisiasi spark context
sc = SparkContext.getOrCreate()

rdd = sc.textFile("file:///vagrant/ibubudi.txt")

# Transform untuk split line
def split_text(line):
    return line.lower().split(" ")
rddBaru = rdd.flatMap(split_text)

# Transform untuk kasih angka 1
def give_number(word):
    return (word,1)
rddBaru = rddBaru.map(give_number)
#rddBaru.saveAsTextFile("file:///vagrant/hasil1.txt")

# Action untuk reduce by key
def hitung_angka(x,y):
    return x+y
hasil = rddBaru.reduceByKey(hitung_angka)
hasil.saveAsTextFile("file:///vagrant/hasil_akhir")


