# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: promptReco -s RAW2DIGI,L1Reco,RECO,DQM --data --magField AutoFromDBCurrent --scenario pp --datatier RECO --eventcontent RECO --conditions GR_P_V25::All --customise Configuration/DataProcessing/RecoTLR.customisePrompt --no_exec --python_filename=promptReco_Collision.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('file:promptReco_DIGI2RAW.root')
    fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/data/Run2011B/L1EGHPF/RAW/v1/000/178/208/001221F3-71F3-E011-A77D-001D09F2545B.root')
    #fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/data/Run2011B/L1EGHPF/RAW/v1/000/178/208/026F8764-68F3-E011-A087-485B39897227.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('promptReco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition
#process.RECOoutput = cms.OutputModule("PoolOutputModule",
#    splitLevel = cms.untracked.int32(0),
#    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    outputCommands = process.RECOEventContent.outputCommands,
#    fileName = cms.untracked.string('promptReco_RAW2DIGI_L1Reco_RECO_DQM.root'),
#    dataset = cms.untracked.PSet(
#        filterName = cms.untracked.string(''),
#        dataTier = cms.untracked.string('RECO')
#    )
#)

# Additional output definition
process.SpecialEventContent = cms.PSet(
           outputCommands = cms.untracked.vstring('drop *'),
                     splitLevel = cms.untracked.int32(0)
                  )
process.SpecialBranchContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_SimRctDigis_*_*',
                                           'keep *_SimGctDigis_*_*',
                                           'keep *_SimGtDigis_*_*',
                                           'keep *_l1extraParticlesOnline_*_*',
                                           'keep *_simEcalTriggerPrimitiveDigis_*_*'
                                           ),
    splitLevel = cms.untracked.int32(0)
    )

process.SpecialEventContent.outputCommands.extend(process.RECOEventContent.outputCommands)
process.SpecialEventContent.outputCommands.extend(process.L1TriggerFEVTDEBUG.outputCommands)
process.SpecialEventContent.outputCommands.append('keep *_l1extraParticlesOnline_*_*')
process.SpecialEventContent.outputCommands.append('keep *_zeroedEcalTrigPrimDigis_*_*')
process.SpecialEventContent.outputCommands.append('keep *_ecalDigis_*_*')
process.SpecialEventContent.outputCommands.append('keep *_hcalDigis_*_*') #modif-new
process.SpecialEventContent.outputCommands.append('keep *_simEcalTriggerPrimitiveDigis_*_*')
process.SpecialEventContent.outputCommands.append('keep *_SimGtDigis_*_*') #modif

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
                                              splitLevel = cms.untracked.int32(0),
                                              outputCommands = process.SpecialEventContent.outputCommands,
                                              fileName = cms.untracked.string('l1EmulatorFromRaw_RAW2DIGI_L1_pRECO.root'),
                                              dataset = cms.untracked.PSet(
    filterName = cms.untracked.string(''),
    dataTier = cms.untracked.string('DIGI-RECO')
    )
                                              )
process.output_step = cms.EndPath(process.FEVTDEBUGHLToutput)


# Other statements
#process.GlobalTag.globaltag = 'FT_R_44_V11::All'
process.GlobalTag.globaltag = 'GR_R_44_V14::All'

#modif#
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalTPGLinearizationConstRcd"),
             tag = cms.string("EcalTPGLinearizationConst_weekly_hlt"),
             connect =cms.untracked.string('frontier://FrontierPrep/CMS_COND_ECAL')
             )
    )

# process
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.Path(process.endOfProcess)

# HLT Filter
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.MyHLTSelection = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
    HLTPaths = [ 'HLT_L1SingleEG*' ,
                 'HLT_Activity_Ecal_*_*'
                 ],
    #andOr = True,
    throw = False)

def customise(process):
    
    #
    # (re-)run the  L1 emulator starting from a RAW file
    #
    from L1Trigger.Configuration.L1Trigger_custom import customiseL1EmulatorFromRaw
    process=customiseL1EmulatorFromRaw(process)
    
    #
    # special configuration cases (change to desired configuration in customize_l1TriggerConfiguration)
    #
    from L1Trigger.Configuration.customise_l1TriggerConfiguration import customiseL1TriggerConfiguration
    process=customiseL1TriggerConfiguration(process)
    
    #
    # customization of output commands
    #
    from L1Trigger.Configuration.L1Trigger_custom import customiseOutputCommands
    process=customiseOutputCommands(process)
    
    return (process)

# Customise the process as-is
process = customise(process)

# Digis
import EventFilter.EcalRawToDigi.EcalUnpackerData_cfi
process.ecalDigis = EventFilter.EcalRawToDigi.EcalUnpackerData_cfi.ecalEBunpacker.clone()
process.ecalDigis.DoRegional = False
process.ecalDigis.InputLabel = 'source'

#process.load('SimCalorimetry.EcalTrigPrimProducers.ecalTrigPrimESProducer_cff')
#process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_beamv5_trans_160208_160728.txt'
#process.EcalTrigPrimESProducer.WriteInFile = False

# TP generation
process.load('SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cff')
process.simEcalTriggerPrimitiveDigis.Label = 'ecalDigis'
process.simEcalTriggerPrimitiveDigis.InstanceEB = 'ebDigis'
process.simEcalTriggerPrimitiveDigis.InstanceEE = 'eeDigis'
process.simEcalTriggerPrimitiveDigis.BarrelOnly = False


# TCC zeroing emulation
process.zeroedEcalTrigPrimDigis = cms.EDProducer('TCCZeroing',
                                                 ZeroingThreshold = cms.double(16.0), # In TP Compressed ET scale
                                                 #ZeroingThreshold = cms.double(4.0), # In TP Compressed ET scale
                                                 Digis = cms.InputTag("ecalDigis", "EcalTriggerPrimitives")
                                                 )

process.analysis = cms.EDAnalyzer('Validate',
                                  OnlineTPs = cms.InputTag("ecalDigis", "EcalTriggerPrimitives"),
                                  #OfflineTPs = cms.InputTag("zeroedEcalTrigPrimDigis"),
                                  OfflineTPs = cms.InputTag("simEcalTriggerPrimitiveDigis"),
                                  OnlineSRFlag = cms.InputTag("ecalDigis"),
                                  hcalDigisLabel = cms.InputTag("hcalDigis"),
                                  GTRecordCollection = cms.string('gtDigis'),
                                  GTRecordCollectionM = cms.string('simGtDigis'),
                                  HLTTag = cms.InputTag("TriggerResults","","HLT")
                                  )

# Set the digi inputs required
#process.simRctDigis.ecalDigis = cms.VInputTag(cms.InputTag("zeroedEcalTrigPrimDigis"))
process.simRctDigis.ecalDigis = cms.VInputTag(cms.InputTag("simEcalTriggerPrimitiveDigis"))
process.simRctDigis.hcalDigis = cms.VInputTag(cms.InputTag("hcalDigis"))
process.simGctDigis.inputLabel = cms.InputTag("simRctDigis")

# L1 extra for the re-simulated candidates
process.l1extraParticles = cms.EDProducer("L1ExtraParticlesProd",
                                          muonSource = cms.InputTag("gtDigis"),
                                          etTotalSource = cms.InputTag("simGctDigis"),
                                          nonIsolatedEmSource = cms.InputTag("simGctDigis","nonIsoEm"),
                                          etMissSource = cms.InputTag("simGctDigis"),
                                          htMissSource = cms.InputTag("simGctDigis"),
                                          produceMuonParticles = cms.bool(False),
                                          forwardJetSource = cms.InputTag("simGctDigis","forJets"),
                                          centralJetSource = cms.InputTag("simGctDigis","cenJets"),
                                          produceCaloParticles = cms.bool(True),
                                          tauJetSource = cms.InputTag("simGctDigis","tauJets"),
                                          isolatedEmSource = cms.InputTag("simGctDigis","isoEm"),
                                          etHadSource = cms.InputTag("simGctDigis"),
                                          hfRingEtSumsSource = cms.InputTag("simGctDigis"),
                                          hfRingBitCountsSource = cms.InputTag("simGctDigis"),
                                          centralBxOnly = cms.bool(True),
                                          ignoreHtMiss = cms.bool(False)
                                          )

# L1 extra for the online candidates
process.l1extraParticlesOnline = cms.EDProducer("L1ExtraParticlesProd",
                                                muonSource = cms.InputTag("gtDigis"),
                                                etTotalSource = cms.InputTag("gctDigis"),
                                                nonIsolatedEmSource = cms.InputTag("gctDigis","nonIsoEm"),
                                                etMissSource = cms.InputTag("gctDigis"),
                                                htMissSource = cms.InputTag("gctDigis"),
                                                produceMuonParticles = cms.bool(False),
                                                forwardJetSource = cms.InputTag("gctDigis","forJets"),
                                                centralJetSource = cms.InputTag("gctDigis","cenJets"),
                                                produceCaloParticles = cms.bool(True),
                                                tauJetSource = cms.InputTag("gctDigis","tauJets"),
                                                isolatedEmSource = cms.InputTag("gctDigis","isoEm"),
                                                etHadSource = cms.InputTag("gctDigis"),
                                                hfRingEtSumsSource = cms.InputTag("gctDigis"),
                                                hfRingBitCountsSource = cms.InputTag("gctDigis"),
                                                centralBxOnly = cms.bool(True),
                                                ignoreHtMiss = cms.bool(False)
                                                )


# Tie it all together
process.everything = cms.Path(
    #process.MyHLTSelection +
    process.RawToDigi +
    process.simEcalTriggerPrimitiveDigis +
    process.simRctDigis +
    process.simGctDigis +
    process.simGtDigis +
    process.l1extraParticles +
    process.l1extraParticlesOnline
    #process.reconstruction +
    #process.analysis
    )


# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.dqmoffline_step,process.endjob_step,process.RECOoutput_step)

process.schedule = cms.Schedule(process.everything,process.output_step)

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
#from Configuration.DataProcessing.RecoTLR import customisePrompt 

#call to customisation function customisePrompt imported from Configuration.DataProcessing.RecoTLR
#process = customisePrompt(process)

# End of customisation functions
