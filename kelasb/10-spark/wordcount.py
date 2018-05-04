# Import library
from pyspark import SparkContext

# Inisiasi spark context
sc = SparkContext.getOrCreate()

# Inisiasi RDD dari sebuah file
rddA = sc.textFile("file:///vagrant/ibubudi.txt")

# Lakukan pengolahan
# 1. Transform flatMap split
# 2. Beri angka 1 sebagai value
# 3. ReduceByKey
rddHasil = rddA.flatMap(lambda line:line.split(" ")).map(lambda word:(word.lower(),1)).reduceByKey(lambda x,y:x+y)

# Hasil akhir
rddHasil.saveAsTextFile("file:///vagrant/hasil_akhir")