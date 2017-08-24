outpath='/nfs/dust/cms/user/mwassmer/ntuples/data_final/' # path of output of analyzer
scriptpath='data_final' # folder containing shell scripts that will have to be run on cluster
samplelist='data_samples_used.csv' # samples list
dataset_column='boosted_dataset' # run on the column with dataset or boosted_dataset?
cmsswcfgpath='/nfs/dust/cms/user/mwassmer/CMSSW_8_0_26_patch2/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Spring17_cfg.py'
cmsswpath='/nfs/dust/cms/user/mwassmer/CMSSW_8_0_26_patch2/'
dbs="prod/phys03" # dbs instance: boosted miniaod is in prod/phys03, standard miniaod in prod/global
min_events_per_job=50000 # min number of events per job 
isBoostedMiniAOD=False # do the inputs contain fat jets?
systematicVariations='systematicVariations_none.txt'
nSystematicVariationsPerJob=6