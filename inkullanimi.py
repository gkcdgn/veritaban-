import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=insert;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute("select *from kotu where dersler in('matematik','tarih')")
ders=imlec.fetchall()
print(ders)