EXPERIMENT TYPE=EXP_RAW_DATA
EXPERIMENT NAME=noche
HEADER VERSION=1103
*****Radar Controller Parameters**********
IPP=1000
NTX=150
TXA=40
TXB=50
Pulse selection_TR=A
Code Type=COMPLEMENTARY_CODE_32
Number of Codes=2
Code Width=32
COD(0)=11101101111000101110110100011101
COD(1)=11101101111000100001001011100010
L4_REFERENCE=TXA
L6 Number Of Portions=1
PORTION_BEGIN(0)=200
PORTION_END(0)=210
L6 Portions IPP Periodic=NO
Number of Taus=1
TAU(0)=250
Sampling Windows=1
H0(0)=70
NSA(0)=200
DH(0)=1.25
L7_REFERENCE=TXA
SAMPLING REFERENCE=MIDDLE OF FIRST SUB-BAUD
RELOJ=1.2
TR_BEFORE=12
TR_AFTER=1
WINDOW IN LINE 5&6=NO
******System Parameters*******************
Number of Cards=3
Card(0)=0
Card(1)=1
Card(2)=2
Number of Channels=5
Channel(0)=1
Channel(1)=2
Channel(2)=3
Channel(3)=4
Channel(4)=5
Antennas_Names=5
AntennaName(1)=
AntennaName(2)=
AntennaName(3)=
AntennaName(4)=
AntennaName(5)=
RAW DATA DIRECTORY=C:\Data\WRADAR
CREATE DIRECTORY PER DAY=YES
INCLUDE EXPNAME IN DIRECTORY=NO
******System Parameters*******************
ADC Resolution=8
PCI DIO BusWidth=32
RAW DATA BLOCKS=120
******Process Parameters******************
DATATYPE=SHORT
DATA ARRANGE=CONTIGUOUS_CH
COHERENT INTEGRATION STRIDE=1
------------------------------------------
ACQUIRED PROFILES=300
PROFILES PER BLOCK=300
------------------------------------------
BEGIN ON START=NO
BEGIN_TIME=07:00
END_TIME=18:00
GENERATE ACQUISITION LINK=YES
VIEW RAW DATA=YES
REFRESH RATE=1
------------------------------------------
SEND STATUS TO FTP=NO
SAVE STATUS AND BLOCK=YES
FTP INTERVAL=60
GENERATE RTI=NO
SEND RTI AND BLOCK=NO
------------------------------------------
COMPORT CONFIG=Com2 CBR_9600 TWOSTOPBITS NOPARITY
JAM CONFIGURE FILE=dmasg_pprofiles_pch_64_pdigi_6clk.jam
ACQUISITION SYSTEM=JARS
************JARS CONFIGURATION PARAMETERS************
JARS_FILTER=F:\Experiments\JASMET\2018_12_60MHz\F120KHZ.jars
MARK WIDTH=2
GENERATE OWN SAMPLING WINDOW=NO
SAVE DATA=YES
****************RC SEQUENCES******************
RC_SEQ1=255,96
RC_STOP_SEQUENCE=255,0
RC_START_SEQUENCE=255,32
