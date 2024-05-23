import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=pythontablo;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

def sil():
    imlec.execute("delete from dersler")
    imlec.commit()


def sil1():
    imlec.execute("delete from dersler where ögrenci_adi='songül'")
    imlec.commit()

sil1()