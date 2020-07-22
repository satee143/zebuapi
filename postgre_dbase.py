import psycopg2

con=psycopg2.connect(database='employees',user='postgres', password='0690252')
cur=con.cursor()
cur.execute(
    "SELECT country,COUNT(employee_id) Strength "
    "FROM employees,regions "
    "WHERE employees.region_id=regions.region_id "
    "GROUP BY country;")

for x in cur:
    print(x)
