import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=pythontablo;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

imlec.execute("select count(*) from table_1")
sayi=imlec.fetchall()
print(sayi)

imlec.execute("select sum(sinav1) from table_1")
toplam=imlec.fetchall()
print(toplam)

imlec.execute("select Avg(sinav1) from table_1")
ortalama=imlec.fetchall()
print(ortalama)