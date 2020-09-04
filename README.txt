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