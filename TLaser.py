# -*- coding: utf-8 -*-

"""
  Programma creato per trasferire il contenuto di una tabella sqlite che contiene i dati delle macchine taglio laser, all'interno di una tabella oracle   
"""

#Librerie di database
import cx_Oracle
import sqlite3 

#Libreria di sistema per leggere i parametri scritti in riga di comando
import sys

try:
    #Controllo che siano stati passati i parametri
    if sys.argv[1] == '' or sys.argv[2] == '':
        pass
except:    
    print('+--------------------------------------------------+')
    print('|             Utilizzo del programma               |')
    print('| parametro1=Percorso sqlite file (es. c:/index.db)|')
    print('| parametro2=Nome server oracle   (es. ICOM_815)   |')
    print('+--------------------------------------------------+')
    sys.exit()    
   
#Collegamento a Oracle
v_oracle_db = cx_Oracle.connect(user='SMILE', password='SMILE', dsn=sys.argv[2])        
v_oracle_cursor = v_oracle_db.cursor()    
                                     
#Collegamento a SQLite
v_sqlite_conn = sqlite3.connect(database=sys.argv[1])
v_sqlite_cur = v_sqlite_conn.cursor()

#Ricerco ultima data inserimento in tabella ORACLE
v_oracle_cursor.execute("SELECT Max(CREATEDAT) FROM bystronicparts")                                
v_data_exe_precedente = v_oracle_cursor.fetchone()[0]
print('Max data in tabella oracle...' + str(v_data_exe_precedente))
        
#Select dati laser da sqlite (attenzione al fatto che è duplicata a seconda se data presente)
if v_data_exe_precedente == None:
    v_sqlite_cur.execute("SELECT Name, Properties, CreatedAt FROM ObjectInfo")                                
else:        
    v_sqlite_cur.execute("SELECT Name, Properties, CreatedAt FROM ObjectInfo WHERE CreatedAt > datetime( '" + str(v_data_exe_precedente) + "')")                                

#Scorro le righe....
print('Trasferimento in corso...')
v_righe = 0
for row in v_sqlite_cur:
    #Conto le righe
    v_righe += 1    
    #Splitto il campo proprietà che contiene lo spessore, x, y e l'area
    v_split = str(row[1]).split('|')
    #Scrivo la riga
    v_insert = "INSERT INTO bystronicparts(NAME, SPESSORE, X, Y, AREA, CREATEDAT) VALUES('"
    v_insert += row[0] 
    v_insert += "'," + v_split[2] 
    v_insert +=  "," + v_split[3]
    v_insert +=  "," + v_split[4]
    v_insert +=  "," + v_split[7]
    v_insert +=  ",TO_TIMESTAMP('" + str(row[2]) + "','RRRR-MM-DD HH24:MI:SS,FF9'))"
    v_oracle_cursor.execute( v_insert )        
    
#Chiudo tutto
v_oracle_cursor.execute('COMMIT')
v_oracle_db.close()
v_sqlite_conn.close()

#Stampo risultato
print('..trasferite ' + str(v_righe) + ' righe.')