#! /usr/bin/python3
import src.runsql as runsql

sql = runsql.SQL()

print(sql.run_fromfile("queries\country_with_budgets.sql"))