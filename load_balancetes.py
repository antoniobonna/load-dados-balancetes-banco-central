import os
import csv
import credentials
import psycopg2
from subprocess import call
from companies import norm_banks
from zipfile import ZipFile
from itertools import islice

### Definicao das variaveis
indir = '/home/ubuntu/dump/dados_balancete_banco_central/'
outdir = '/home/ubuntu/scripts/load-dados-balancetes-banco-central/parsed/'
new_file = 'balancete.csv'
files = [f for f in os.listdir(indir) if f.endswith('zip')]
tablename = 'balancetes_banco_central.balancete_geral_stg'

DATABASE, HOST, USER, PASSWORD = credentials.setDatabaseLogin()

### funcao que cria data no formato banco de dados
def parse_date(date):
    newdate = date[:4] + '-' + date[4:] + '-01'
    return newdate

### extrai arquivos zip
def extract_file(file):
    zip = ZipFile(indir+file)
    zip.extractall(indir)
    os.remove(indir+file)

for file in files:
    extract_file(file)

csvfiles = [f for f in os.listdir(indir) if f.endswith('CSV')]

### Iteracao sobre os arquivos e parser dos CSVs

with open(outdir+new_file,'w', newline="\n", encoding="utf-8") as ofile:
    writer = csv.writer(ofile, delimiter=';')
    for file in csvfiles:
        with open(indir+file, 'r', encoding='iso-8859-1') as ifile:
            reader = csv.reader(ifile,delimiter=';')
            count = 0
            for row in reader:
                if count < 4:
                    count += 1
                    continue ### pula as 4 primeiras linhas do arquivo
                try:
                    row[0] = parse_date(row[0])
                    ### ajusta data para o formato do banco de dados
                    row[4] = norm_banks(row[4])
                    row[10] = row[10].replace(',','.')
                    if len(row) < 13:
                        for i in range(0,13-len(row)):
                            row.append('')
                    row[11] = row[11].replace(',','.')
                    row[12] = row[12].replace(',','.')
                    writer.writerow(row)
                except:
                    print('Error in line:\n{}\n'.format(row))
                    pass
        os.remove(indir+file)

### conecta no banco de dados
db_conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(DATABASE, USER, HOST, PASSWORD))
cursor = db_conn.cursor()
print('Connected to the database')
### copy
with open(outdir+new_file, 'r') as ifile:
    SQL_STATEMENT = "COPY %s FROM STDIN WITH CSV DELIMITER AS ';' NULL AS ''"
    print("Executing Copy in "+tablename)
    cursor.copy_expert(sql=SQL_STATEMENT % tablename, file=ifile)
    db_conn.commit()
os.remove(outdir+new_file)
cursor.close()
db_conn.close()

### VACUUM ANALYZE
call('psql -d torkcapital -c "VACUUM VERBOSE ANALYZE '+tablename+'";',shell=True)