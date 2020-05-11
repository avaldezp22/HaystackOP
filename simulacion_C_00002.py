###################################################
#################  COPPERBALL  ####################
###################################################
ExperimentParameters

bool ExpParameters::ReadRACPFileParameters(const char* RACPFileName)
##aqui debo abrir el archivo .RACP
# READ .RACP
"EXPERIMENT TYPE="
if  EXP_PROCESS_SPECTRA:
	MyGPParam.FixPP.m_nExperimentType = EXP_SPECTRA;
	MyGPParam.FixPP.m_nProcessFlags|=FLAG_SPECTRA_CALC;
	pass
elif EXP_RAW_DATA;
	pass

"EXPERIMENT NAME="
			strcpy_s(MyGPParam.m_sExpName,FindValue(StrPtr));
			MyGRCParam.FixRCP.m_nEspType=(unsigned int)atoi(FindValue(StrPtr));
"NUMBER OF EXPERIMENTS="
			MyGRCParam.FixRCP.m_nEspType=(unsigned int)atoi(FindValue(StrPtr));

"NUMBER OF CARDS="
			MyGPParam.m_nCards=(unsigned int)atoi(FindValue(StrPtr))
			if(MyGPParam.m_nCards>0 && MyGPParam.m_nCards < 10):
				  MyGPParam.Dyn_nCardSequence= new unsigned char[MyGPParam.m_nCards]
				  #Read and put the code string in valstr
				  fgets(StrTemp,100,MyRacpFile);
				  MyGPParam.Dyn_nCardSequence[q]=(unsigned char)atoi(FindValue(StrPtr))
			elif(MyGPParam.m_nCards>=10):
					printf("SysParamScanFile")

"NUMBER OF CHANNELS="
			MySystemParam.m_nChannels = (unsigned int)atoi(FindValue(StrPtr))
			MyAcqParam.nAcqChannels = MySystemParam.m_nChannels

"RAW DATA DIRECTORY="

			MyGPParam.m_sBaseDirectory
"PROCESS DATA DIRECTORY="
			MyGPParam.m_sBaseDirectory

"CREATE DIRECTORY PER DAY="
			if((StrPtr=strstr(StrTemp,"YES"))!=NULL):
				MyGPParam.bCreateDayDir=true
			else:
				MyGPParam.bCreateDayDir=false

"INCLUDE EXPNAME IN DIRECTORY="
			if((StrPtr=strstr(StrTemp,"YES"))!=NULL):
				MyGPParam.bNameInDirectory=true;
			else:
				MyGPParam.bNameInDirectory=false;

"SAVE DATA="
			if((StrPtr=strstr(StrTemp,"YES"))!=NULL)
				SaveData=true;
			else
				SaveData=false;

ReadRCParameters(MyRacpFile,StrTemp);
	"IPP="
	FixRCP.m_fIPP
	"NTX="
	FixRCP.m_nNTX
	"TXA="
	FixRCP.m_fTXA
	"TXB="
	FixRCP.m_fTXB
	"CODE TYPE="
		if (strstr(valstr, "USERDEFINE") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_USERDEFINE;
		else if (strstr(valstr, "BARKER2") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER2;
		else if (strstr(valstr, "BARKER3") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER3;
		else if (strstr(valstr, "BARKER4") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER4;
		else if (strstr(valstr, "BARKER5") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER5;
		else if (strstr(valstr, "BARKER7") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER7;
		else if (strstr(valstr, "BARKER11") != NULL)	MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER11;
		else if (strstr(valstr, "BARKER13") != NULL)	MyGRCParam.FixRCP.m_nCodeType=CODE_BARKER13;
		else if (strstr(valstr, "AC128") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_AC128;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_2") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE2;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_4") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE4;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_8") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE8;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_16") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE16;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_32") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE32;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_64") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE64;
		else if (strstr(valstr, "COMPLEMENTARY_CODE_128") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_COMPLEMENTARYCODE128;
		else if (strstr(valstr, "BINARY_CODE_28") != NULL)		MyGRCParam.FixRCP.m_nCodeType=CODE_BINARY28;

	"NUMBER OF CODES="
	m_nNum_Codes=(unsigned int)atoi(FindValue(StrPtr))
	"CODE WIDTH="
	m_nBauds = (unsigned int)atoi(FindValue(StrPtr))
	code_binaries=  new char*[MyGRCParam.m_nNum_Codes]
	if sum == 0:
		IsFliped =True
	"L4_REFERENCE="
		if	"TXA"
				baud_with  =FixRCP.m_fTXA/MyGRCParam.m_nBauds
		elif "TXB"
				baud_with  =FixRCP.m_fTXB/MyGRCParam.m_nBauds
	"PULSE SELECTION_TXA="
		FixRCP.m_sRango_TXA
	"PULSE SELECTION_TXB="
		FixRCP.m_sRango_TXB
	"PULSE SELECTION_TR="
		FixRCP.m_sRango_IPP
	"SAMPLING WINDOWS (LINE 4)="

	"SAMPLING WINDOWS (LINE 5)="
		FixRCP.m_nL5_NumWindows
		MyGRCParam.Dyn_sfL5_AcqH0 =
		MyGRCParam.Dyn_snL5_AcqNSA =
		MyGRCParam.Dyn_sfL5_AcqDH =

	"SAMPLING WINDOWS (LINE 6)="
		FixRCP.m_nL5_NumWindows
		MyGRCParam.Dyn_sfL6_AcqH0 =
		MyGRCParam.Dyn_snL6_AcqNSA =
		MyGRCParam.Dyn_sfL6_AcqDH =
	"NUMBER OF TAUS="
		FixRCP.m_nNum_Taus
		Dyn_sfTau
	"SAMPLING WINDOWS="
		FixRCP.m_nNum_Windows
		MyGRCParam.Dyn_sfAcqH0  =
		MyGRCParam.Dyn_snAcqNSA =
		MyGRCParam.Dyn_sfAcqDH  =
	"RELOJ="
		FixRCP.m_fCLOCK

		ReadSysParameters(MyRacpFile,StrTemp);
		"ADC RESOLUTION="
		MySystemParam.m_nADCResolution=(unsigned int)atoi(FindValue(StrPtr));

		"PCI DIO BUSWIDTH="

		MySystemParam.m_nPCIDIOBusWidth=(unsigned int)atoi(FindValue(StrPtr));
		"RAW DATA BLOCKS="
		MyGPParam.FixPP.m_nDataBlocksperFile=(unsigned int)atoi(FindValue(StrPtr));
		"PROCESS DATA BLOCKS="
		MyGPParam.FixPP.m_nDataBlocksperFile=(unsigned int)atoi(FindValue(StrPtr));

		"SEND STATUS TO FTP="
		MyFtpParam.m_bsend2ftp=Yes
		"FTP SERVER="
		MyFtpParam.m_sftp_server

		"FTP USER="
		strcpy_s(MyFtpParam.m_sftp_user

		"FTP PASSWD="
		MyFtpParam.m_sftp_passwd,FindValue(StrPtr));

		"FTP DIR="
		MyFtpParam.m_sftp_dir
		"FTP FILE="
		MyFtpParam.m_sftp_file
		"FTP INTERVAL="
		MyFtpParam.m_nftp_interval

		"SAVE STATUS AND BLOCK="
		MyFtpParam.m_bSave_StatusBlock=Yes

		ReadProcessParameters(MyRacpFile,StrTemp);

			if("DATATYPE=")
				if("FLOAT"))
					MyGPParam.FixPP.m_nProcessFlags&=~FLAG_DATATYPE_SHORT;
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_DATATYPE_FLOAT;
				else
					MyGPParam.FixPP.m_nProcessFlags&=~FLAG_DATATYPE_FLOAT;
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_DATATYPE_SHORT;

			if("DATA ARRANGE=")
				//clean the corresponding bits (INVERT MASK)
				MyGPParam.FixPP.m_nProcessFlags&=(~(FLAG_DATAARRANGE_CONTIGUOUS_H
								|FLAG_DATAARRANGE_CONTIGUOUS_CH|FLAG_DATAARRANGE_CONTIGUOUS_P));

				if((StrPtr=strstr(StrTemp,"CONTIGUOUS_H"))!=NULL)
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_DATAARRANGE_CONTIGUOUS_H;
				elseif((StrPtr=strstr(StrTemp,"CONTIGUOUS_CH"))!=NULL)
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_DATAARRANGE_CONTIGUOUS_CH;
				elseif((StrPtr=strstr(StrTemp,"CONTIGUOUS_P"))!=NULL)
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_DATAARRANGE_CONTIGUOUS_P;

			if("COHERENT INTEGRATIONS=")
				MyGPParam.FixPP.m_nCoherentIntegrations=(unsigned int)atoi(FindValue(StrPtr));
				if(MyGPParam.FixPP.m_nCoherentIntegrations>1)
					MyGPParam.FixPP.m_nProcessFlags|=FLAG_COHERENT_INTEGRATION;

			if("COHERENT INTEGRATION STRIDE=")

				MyGPParam.m_nCohIntStride=(unsigned int)atoi(FindValue(StrPtr));
				goto fin_PROP;

			if("ACQUIRED PROFILES=")

				MySystemParam.m_nProfiles=(unsigned int)atoi(FindValue(StrPtr));
				MyAcqParam.nAcqProfiles = MySystemParam.m_nProfiles;//DEBUG1
				goto fin_PROP;

			if("PROFILES PER BLOCK=")
				MyGPParam.m_nProfilesperBlock = (unsigned int)atoi(FindValue(StrPtr));
				MyGPParam.FixPP.m_nFFTorProfilesperBlock = MyGPParam.m_nProfilesperBlock;

			if("BEGIN ON START=")

				if((StrPtr=strstr(StrTemp,"YES"))!=NULL)
					MyGPParam.m_bBeginOnStart = true;

			if("BEGIN_TIME=")
				sscanf(FindValue(StrPtr),"%2d:%2d",&(MyGPParam.FixPP.m_BeginTime.tm_hour),&(MyGPParam.FixPP.m_BeginTime.tm_min));
				goto fin_PROP;

			if("END_TIME=")
				sscanf(FindValue(StrPtr),"%2d:%2d",&(MyGPParam.FixPP.m_EndTime.tm_hour),&(MyGPParam.FixPP.m_EndTime.tm_min)


		ReadEchotekParameters(MyRacpFile,StrTemp);
		ReadJARSParameters(MyRacpFile,StrTemp); /*Agregado x Marcos 20 mayo 2010*/
