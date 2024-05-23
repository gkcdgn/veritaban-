import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=deneme;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()
imlec.execute('select*from tablom')

def getir():
    imlec.execute("select*from tablom")
    liste=imlec.fetchall()
    for i in liste:
        print(i)
getir()

def getir1():
    imlec.execute("select kullanici_adi,sirketadi from tablom")
    liste=imlec.fetchall()
    print(liste)

getir1()

def getir2():
    imlec.execute("select *from tablom where sirketadi='boktan'")
    liste=imlec.fetchall()
    print(liste)
getir2()