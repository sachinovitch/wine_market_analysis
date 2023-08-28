#! /usr/bin/python3
import src.runsql as runsql

sql = runsql.SQL()

print(sql.run_fromfile("queries/sample.sql"))
print(sql.run_fromtext("SELECT name FROM wineries ORDER BY name LIMIT 5"))

sql.cnn_close()
