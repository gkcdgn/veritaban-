import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=pythontablo;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute('create table dersler(derid tinyint,dersad varchar(20))')
db.commit()

def veriekle(id,ders):
    imlec.execute("insert into dersler values(?,?)",(id,ders))
    imlec.commit()

id=int(input("ders idsi giriniz"))
ders=input("ders adı giriniz")

veriekle(id,ders)
db.close()