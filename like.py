import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute("select * from kotu where dersler='tarih'")
ders=imlec.fetchall()
#print(ders)


imlec.execute("select * from kotu where dersler like'a%'")
dersi=imlec.fetchall()
#print(dersi)

imlec.execute("select * from kotu where dersler not like'%a%'")
dersi=imlec.fetchall()
print(dersi)