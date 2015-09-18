### CERN ############################
# 8nm, 1nh, 8nh, 1nd, 2nd, 1nw, 2nw #
# use with bsub -q 8nh batch.sh     #
#!/bin/zsh                          #
#####################################
cd $TMPDIR
runNstart=%runNstart%
runNend=%runNend%
rm -r ele_${runNstart}to${runNend} 
mkdir  ele_${runNstart}to${runNend}
cd ele_${runNstart}to${runNend}
export MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
export WORKDIR=`pwd`
output_dir=/eos/cms/store/user/fmeng/Crab3/makepairselection_LC
output_root_dir=root://eoscms//${output_dir}
echo " use default output dir" $output_dir

cd $WORKDIR
. /afs/cern.ch/sw/lcg/external/gcc/4.6/x86_64-slc6/setup.sh
. /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.09/x86_64-slc6-gcc46-opt/root/bin/thisroot.sh
cp $MYBATCHDIR/baseFuncNad.1.8.h . 
cp $MYBATCHDIR/readJSONFile.cc  .
cp $MYBATCHDIR/readJSONFile.h  .
cp $MYBATCHDIR/configuration/makePairs_test_new2_LC.C   .

#cd $MYBATCHDIR
echo "in the middle"
#echo $1
#echo $2

#cd $WORKDIR
echo "how are  you"
sed -e "s,%startN%,$runNstart," \
    -e "s,%endN%,$runNend,"\
    -i makePairs_test_new2_LC.C  
#direcotry1="${outputplace}"
root -l -q 'makePairs_test_new2_LC.C++'
#g++ test.cpp -g -o test `root-config --cflags --glibs` && ./test
#rfcp *.txt  $MYBATCHDIR/.
cd $TMPDIR
xrdcp -f -R ele_${runNstart}to${runNend}  ${output_root_dir}
#$eos chmod 775 ${output_dir}/*.root
#Save the batch.sh file and send it to the lxplus farm queue with:
#bsub -q 8nm batch.sh
