MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
cp $MYBATCHDIR/configuration/batch_select_LC.sh .


sed -e "s,%num1%,$1," \
    -e "s,%num2%,$2," \
    -i batch_select_LC.sh 


mv batch_select_LC.sh   batch_select_LC_$1to$2.sh

bsub -q cmscaf1nd  batch_select_LC_$1to$2.sh 

#rm batch_$1to$2.sh
