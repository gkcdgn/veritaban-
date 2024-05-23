import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

imlec.execute("select ogrenci_cinsiyeti,count(*) from kotu GROUP BY ogrenci_cinsiyeti")
sayi=imlec.fetchall()
print(sayi)

imlec.execute("select dersler,count(*) from kotu GROUP BY dersler")
ders=imlec.fetchall()
print(ders)
