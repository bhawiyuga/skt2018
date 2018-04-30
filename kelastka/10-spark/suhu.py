# Import sparkcontext
from pyspark import SparkContext

# Inisiasi spark context
sc = SparkContext.getOrCreate()

# Import data suhu
rdd = sc.textFile("file:///vagrant/dataset/suhu.txt")

def kaliDua(x):
    return int(x)*2

# Transform dikalikan dua (Transform)
rddKaliDua = rdd.map(kaliDua)

# Cari sum (Action)
sum = rddKaliDua.sum()

#print("Hasil sum adalah "+str(sum))
# Cetak ke file
rddHasil = sc.parallelize([sum])
rddHasil.saveAsTextFile("file:///vagrant/dataset/hasil.txt")