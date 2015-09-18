MYBATCHDIR=/afs/cern.ch/user/f/fmeng/FANBOWORKINGAREA/CMSSW_6_2_0/src/L1Studies/EGamma/Macros/Efficiency
cp $MYBATCHDIR/configuration/batch_template_LC.sh .


sed -e "s,%runNstart%,$1," \
    -e "s,%runNend%,$2," \
    -i batch_template_LC.sh


mv batch_template_LC.sh batch_$1to$2.sh

#bsub -q cmscaf1nd   batch_$1to$2.sh

#rm batch_$1to$2.sh
