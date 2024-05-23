import pypyodbc


db=pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=GÖKÇE\SQLEXPRESS;'
    'Database=pythontablo;'
    'Trusted_Connection=True;'
)

imlec=db.cursor()