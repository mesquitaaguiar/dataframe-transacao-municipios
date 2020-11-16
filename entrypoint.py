import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import Row

Transacao = Row('id_transacao','nm_municipio','nm_estado','dt_atualizacao','ordem_transacao')
sparkContext = pyspark.SparkContext('local[*]')
sqlContext = SQLContext(sparkContext)

def main():
    rows = sparkContext.textFile('file:////tmp//*.txt').map(lambda line: line.split(";")).cache()
    transacao = rows.map(lambda r: Transacao(*r))
    df2 = sqlContext.createDataFrame(transacao)
    df2.createOrReplaceTempView("transacao")
    
    print(sqlContext.sql("SELECT * FROM transacao order by nm_municipio").show())


if __name__=="__main__":
    main()