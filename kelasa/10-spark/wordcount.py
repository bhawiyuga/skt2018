from pyspark import SparkContext

# Inisiasi spark context
sc = SparkContext.getOrCreate()

# Inisiasi rdd dari file text
rdd = sc.textFile("file:///vagrant/ibubudi.txt")

# Transform untuk split line
def split_line(line):
    return line.split(" ")
rddWord = rdd.flatMap(split_line)

# Beri angka 1 sebagai value
def give_number(word):
    return (word.lower(),1)
rddNumber = rddWord.map(give_number)

# Hitung / jumlahkan value dengan key yang sama
def hitung(x,y):
    return x+y
hasil = rddNumber.reduceByKey(hitung)

# Cetak output ke file
hasil.saveAsTextFile("file:///vagrant/hasil_wordcount")


