mkdir /tmp/fmeng/data
tmpdir=/tmp/fmeng/data
MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
output_dir=/eos/cms/store/user/fmeng/Crab3/makepairselection1
output_root_dir=root://eoscms//${output_dir}
xrdcp -f -R  ${output_root_dir} /tmp/fmeng/data/.
cd /tmp/fmeng/data/
hadd elepairs0f.root elepairs_*0.root
hadd elepairs1f.root elepairs_*1.root
hadd elepairs2f.root elepairs_*2.root
hadd elepairs3f.root elepairs_*3.root
hadd elepairs4f.root elepairs_*4.root
hadd elepairs5f.root elepairs_*5.root
hadd elepairs6f.root elepairs_*6.root
hadd elepairs7f.root elepairs_*7.root
hadd elepairs8f.root elepairs_*8.root
hadd elepairs9f.root elepairs_*9.root
hadd elepairs.root elepairs*f.root
cp ${MYBATCHDIR}/configuration/selectPairs.C ${tmpdir}/.
cp $MYBATCHDIR/baseFuncNad.1.8.h . 
cp $MYBATCHDIR/readJSONFile.cc  .
cp $MYBATCHDIR/readJSONFile.h  .
root -l -q 'selectPairs.C++'


