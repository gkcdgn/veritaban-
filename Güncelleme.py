
import pypyodbc

db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=deneme;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()

def guncelleme():
    imlec.execute("update tablom set kullanici_adi='gökçe' where kullanici_adi='jeee'")
    imlec.commit()

guncelleme()