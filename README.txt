Nella cartella sono presenti:

index.db = Esempio del file SQLITE contenente la tabella e i dati che dobbiamo trasferire
Laser_Trasferimento.py = Sorgente del programma Python che si occupa del trasferimento
Laser_Trasferimento_compile.bat = Sorgente del bat per la compilazione del programma Python (di fatto un comando)
Laser_Trasferimento.spec = Viene creato da "Laser_Trasferimento_compile.bat" durante la compilazione...ma può essere eliminato ogni volta
BYSTRONICPARTS.sql = Struttura della tabella lato Oracle dove vengono scritte le informazioni
dist = Cartella contenente l'eseguibile (non è detto che sia presente :-) )
__python = cache di Python che si può cancellare

Per l'esecuzione del programma è necessario aver installato:

- Python 3.6 o superiore
- Libreria cx_Oracle (da installare tramite comando: pip install cx_oracle)
- Libreria pyinstaller per la compilazione del programma (da installare tramite comando: pip install pyinstaller)

Alcune note per l'esecuzione in ICOM
Ho fatto quanto segue:
In "F:\appl\icom\" rinominata la cartella TLaser in TLaser_originale
Fatta una copia di TLaser
Nella cartella TLaser rinominati i file OCI.dll in _OCI.dll e MSVCR71.dll in _MSVCR71.dll
Scaricato instant client 19.8 in versione 32bit (qui penso che anche uno più vecchio poteva andare bene)
Estratto tutti i file del client nella cartella TLaser
Copiato tnsnames.ora nella cartella TLaser
Nella cartella TLaser creato il file TLaser.bat con seguente contenuto:
SET TNS_ADMIN=F:\APPL\Icom\TLaser
SET NLS_LANG=AMERICAN_AMERICA.UTF8
F:\APPL\Icom\TLaser\TLaser.exe "R:\SmiMec\Macchine\Rep_Lamiera\Laser BystarFiber8kW\BystronicData\Bysoft7\Parts\index.db" icom_815
Ora da ICOM eseguo TLaser.bat e tutto funziona.