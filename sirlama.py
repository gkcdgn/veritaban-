import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute("select dersler from kotu order by dersler desc")
ders=imlec.fetchall()
print(ders)