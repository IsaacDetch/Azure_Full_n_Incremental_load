# Fabric notebook source

# METADATA ********************

# META {
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8cfd7126-f032-40f5-90cf-5bf2f6493b15",
# META       "default_lakehouse_name": "WorldWideImporters",
# META       "default_lakehouse_workspace_id": "7d1c7242-49fd-4610-8ad9-5e6d4b72e5bd"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.sql("SELECT * FROM WorldWideImporters.fact_sale LIMIT 1000")
display(df)

# CELL ********************

df.count()

# CELL ********************

table_name = 'wwi_sales'

# CELL ********************

## df.write.mode("oveerwrite").format("delta").save("Table/" + table_name)

# CELL ********************

df.createOrReplaceTempView("fact")

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SELECT * FROM fact_sale

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SELECT SalespersonKey, SUM(UnitPrice) FROM fact_sale GROUP BY SalespersonKey;

