import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute("select distinct dersler from kotu")
ders=imlec.fetchall()
print(ders)

imlec.execute("select count(distinct (dersler)) from kotu")
dersler=imlec.fetchall()
print(dersler)