# Import sparkcontext
from pyspark import SparkContext
import json

# Inisiasi spark context
sc = SparkContext.getOrCreate()

# Import
rdd = sc.textFile("file:///vagrant/dataset/iot_devices.json")

def parseJson(line):
    data = json.loads(line)
    return data["temp"]

rddSuhu = rdd.map(parseJson)

hasil = rddSuhu.mean()

#print("Rata- adalah "+str(hasil))
rddHasil = sc.parallelize([hasil])
rddHasil.saveAsTextFile("file:///vagrant/dataset/hasiliot")