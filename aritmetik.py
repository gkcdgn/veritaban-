import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=pythontablo;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

#imlec.execute("update table_1 set toplam=(sinav1+sinav2+sinav3)")
imlec.execute("update table_1 set ortalama=(sinav1+sinav2+sinav3)/3 ")
imlec.commit()