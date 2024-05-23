import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

imlec.execute("select dersler,count(*) from kotu GROUP BY dersler having count(*)=2")
sayi=imlec.fetchall()
print(sayi)

imlec.execute("select dersler,count(*) from kotu GROUP BY dersler having dersler='tarih'")
say=imlec.fetchall()
print(say)