mkdir /tmp/fmeng/data%num2%
tmpdir=/tmp/fmeng/data%num2%
MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
output_dir=/eos/cms/store/user/fmeng/Crab3/makepairselection
output_root_dir=root://eoscms/${output_dir}
for i in {%num1%..%num2%}
do
    xrdcp -f -r  ${output_root_dir}/elepairs${i}.root  $tmpdir
done

cd $tmpdir
 
hadd elepairs%num1%to%num2%.root elepairs*
#selectPair
xrdcp -r -f elepairs%num1%to%num2%.root root://eoscms//eos/cms/store/user/fmeng/Crab3/selectPair/ 

cp ${MYBATCHDIR}/configuration/selectPairs.C ${tmpdir}/.
cp $MYBATCHDIR/baseFuncNad.1.8.h . 
cp $MYBATCHDIR/readJSONFile.cc  .
cp $MYBATCHDIR/readJSONFile.h  .
root -l -q 'selectPairs.C++'


