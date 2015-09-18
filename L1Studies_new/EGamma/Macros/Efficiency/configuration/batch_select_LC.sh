mkdir /tmp/fmeng/data%num1%to%num2%
tmpdir=/tmp/fmeng/data%num1%to%num2%
MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
output_dir=/eos/cms/store/user/fmeng/Crab3/makepairselection_LC
output_root_dir=root://eoscms/${output_dir}
for i in {%num1%..%num2%}
do
    xrdcp -f -r  ${output_root_dir}/elepairs_${i}.root  $tmpdir/.
done

cd $tmpdir
mkdir result%num1%to%num2%
runNstart=%num1%
runNend=%num2% 
hadd elepairs%num1%to%num2%.root elepairs*
#selectPair
xrdcp -r -f elepairs%num1%to%num2%.root root://eoscms//eos/cms/store/user/fmeng/Crab3/selectPair_LC/ 

cp ${MYBATCHDIR}/configuration/selectPairs_LC.C ${tmpdir}/.
cp $MYBATCHDIR/baseFuncNad.1.8.h . 
cp $MYBATCHDIR/readJSONFile.cc  .
cp $MYBATCHDIR/readJSONFile.h  .
#root -l -q 'selectPairs.C++'
sed -e "s,|num1|,$runNstart," \
    -e "s,|num2|,$runNend,"\
    -i selectPairs_LC.C
root -l -q 'selectPairs_LC.C++'
xrdcp -r -f result%num1%to%num2%/\
tree_effi_TagProbe%num1%to%num2%.root \
root://eoscms//eos/cms/store/user/fmeng/Crab3/selectPair_LC/result


