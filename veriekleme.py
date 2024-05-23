import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=deneme;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute('select*from tablom')

def veriekle():
    imlec.execute("insert into tablom values('10','selin','avru','40')")
    imlec.commit()

veriekle()
kullanicilar=imlec.fetchall()
for i in kullanicilar:
    print(i)




db.close()