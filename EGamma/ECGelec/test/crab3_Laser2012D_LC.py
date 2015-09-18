from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ECAL_LASER_CORRECTION_D_LC'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'eleTreeProd_testFastSim_TPG_antr_06_09_LC.py'

config.Data.inputDataset = '/DoubleElectron/Run2012D-ZElectron-22Jan2013-v1/RAW-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob =200 
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON.txt'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#config.Data.runRange = '193093-193999' # '193093-194075'
#config.Data.runRange = '203777-208686' # '193093-194075'
config.Data.runRange = '203777-208686' # all for D data 203777-208686
#config.Data.runRange = '190456-190705' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/fmeng/Crab3'
config.Data.publication = False 
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_Data_analysis'
#config.section_('User')
#config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
