##########################################################################################
#-----------------AQUI NACE EL ORIGEN-------------

#   En lines generales la clase main.cpp  tiene:

int main()

ArgProcessor ArgProcess(MyParameters,&pAcquisitionManager); ###################ENFOQUE 1
#---------------------------------------------------------------------------------
#---------------------------- NUMBER 1--------------------------------------------
#---------------------------------------------------------------------------------
ArgProcess.jro_arguments(argc,argv);                        ################## ENFOQUE 2

        ##ingresa parametros y memoria a process manager (RdpToolsBeta)
		MyProcess.GetExtParameters(&MyParameters,&MyMemManager
        ##crea todos los buffers necesarios para iniciar la adquisicion
		if(!MyMemManager.AllocateMemory(&MyParameters))

        #inicializa buffers y parametros de procesamiento
		if(!MyProcess.initProcessing())

        ##ingresa los parametros para crear las cabeceras del formato Jicamarca
		MyHeader.GetExpParameters(&MyParameters);

		##ingresa parametros al dispositivo seleccionado para adquirir
		pAcquisitionManager->jro_MatchParameters(&MyParameters);

		##ingresa buffers y funcion que se ejecutara cuando se tenga un buffer lleno
		pAcquisitionManager->jro_AssignMemory(&MyMemManager,&MyCallbackFunction);

        if(!pAcquisitionManager->jro_InitAcquisition())
        ### si se apreta la tecla q
        pAcquisitionManager->jro_StopAcquisition();

void MyCallbackFunction(flag)
                        -------------->MyProcess.ProcessData
                        -------------->MyParameters.SaveData
                        -------------->MyHeader.SaveData(&MyMemManager)
                        -------------->MyHeader.SendData(&MyMemManager);



void Process_Finish()   -------------->pAcquisitionManager->jro_StopAcquisition();
#######################################################################################
######################ENFOQUE 1
#-----------------------------------------------------------------------------------
#----------------------------   NUMBER 2 -------------------------------------------
#-----------------------------------------------------------------------------------
int ArgProcessor::jro_arguments(int argc,char* argv[])

                MyParameters.ReadRACPFileParameters(argv[++i]) ##DESTINADO AL ARCHIVO RACP profile
                else if(arg.compare("--cbsim")==0)
                    			MyParameters.EnableCooperSimulation = true;
			                    MyParameters.currentDataFormat = HPCh_;
                            	}else if(MyParameters.EnableCooperSimulation)
	                             ##establece al sistema de simulacion cooperball como AcquisitionManager
		                                  (*MyAcqMan) = &cooperball

#########################copperball#################################

copperball    AcquisitionManager
                public
                    ---> void jro_MatchParameters # recibe datos de ExperimentParameters
                         ----------->  jro_MatchParameters(ExpParameters* ExpParam)
                         #---------------------------------------------------------------
                         #------------------- NUMBER 3
                         #-------------------  ExpParameters::ReadRACPFileParameters
                         #---------------------------------------------------------------
                         ExpParameters::ReadRACPFileParameters
                    #------------------------------------------------------------------------------
                    #--------------------------  NUMBER 4
                    #-------------------------------------------------------------------------------
                    ---> void jro_AssignMemory    #  asignacion de buffers y cunciones donde la data es transferida
                            #-------------Enfocate en el MyMemManager
                            #m_SizeofBuffer ->m_miSizeAcqBuffer[0];
                            #m_AcqBuffer->m_mAcqBuffer[0]
                    #------------------------------------------------------------------------------
                    #--------------------------  NUMBER 5
                    #-------------------------------------------------------------------------------
                    ---> bool jro_InitAcquisition #  inicia adquicion. si algo esta mal pon falso.
                    ---> bool jro_StopAcquisition #  detener adquisicion.
                    ---> DWORD WINAPI RunSimulation(LPVOID p) #thread que se encarga de la simulacion
                    ---> void init_pulse
                   private:
                            -timeperblock
                            jro_GenerateBlockOfData #  genera data de copperball
                            signal
                            fAngle
                            DC_level
                            stdev
                            RandomNum
                            RandomMAX
                            SignalMax
                            SingalMin
                            m_nReference
                            readcode
                            CopperSignal
                            BaudWidth
                            prof_gen
                            InBuffer
                            Imbuff
                            Rebuff
                            Noise
                            pulses
                            pulse_size
                            num_codes



copperball     #####COMO FUNCIONA
                ---> void jro_MatchParameters # recibe datos de ExperimentParameters
                    #------------------------------------------------
                    #---------------- NUMBER 6
                        ExpParameters::ReadRACPFileParameters
                    #------------------------------------------------
                ---> void jro_AssignMemory
                        MemoryManager::MemoryManager()
                ---> jro_InitAcquisition
                    #------------------------------------------------
                    #---------------- NUMBER 7
                    #------------------------------------------------
                    ---> init_pulses()
                    ---> RunSimulation---> jro_GenerateBlockOfData

###################################################
#################  COPPERBALL  ####################
###################################################

ExperimentParameters
