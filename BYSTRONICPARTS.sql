-- TABELLA DI DESTINAZIONE DATI LATO ORACLE
CREATE TABLE BYSTRONICPARTS (
  NAME       VARCHAR2(100)  NULL,
  SPESSORE   NUMBER(17,6)   NULL,
  X          NUMBER(17,6)   NULL,
  Y          NUMBER(17,6)   NULL,
  AREA       NUMBER(17,6)   NULL,
  CREATEDAT  TIMESTAMP(6)   NULL
)

--TRUNCATE TABLE BYSTRONICPARTS
--SELECT * FROM BYSTRONICPARTS