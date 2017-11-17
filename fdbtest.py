import fdb as firebird
from datetime import datetime, timedelta
from validate_email import validate_email

banco = '10.1.15.116:/opt/savi/data/atc/sistemas/dados/NFE.FDB'

dt_ini = datetime.now() - timedelta(days=2)
print(dt_ini)

con = firebird.connect(dsn=banco, user='sysdba', password='rp@inf01')
cur = con.cursor()
query="select n.codigonf, n.dtemissao, d.emaildestinatario from nf n,destinatarionf d where n.codigonf = d.nf and n.emailenviado = 'E' and n.dtemissao >= ?"
cur.execute(query,(dt_ini,))
for (nota,data,email) in cur:
    print('Nota %s data: %s email: %s' % (nota, str(data), email))
con.commit()
cur.close()