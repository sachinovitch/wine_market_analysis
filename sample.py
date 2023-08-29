#! /usr/bin/python3
import src.runsql as runsql

sql = runsql.SQL()

print(sql.run_fromfile("queries/highlights10_approach1.sql"))
