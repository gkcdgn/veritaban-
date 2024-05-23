import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=deneme;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute("select *from tablom where yasi<40")
yas=imlec.fetchall()
print(yas)


imlec.execute("select *from tablom where sirketadi between 'a' and 'd'")
adi=imlec.fetchall()
print(adi)


