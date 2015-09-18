#include "TH1F.h"
#include "photon9.h"
#include "formats10.h"

void Emulstudy()
{
   TFile *f1 =new TFile("tree_testFastSim_TPG_checknow_lastchecktoday.root");
   TTree *treeChain1 = (TTree*)f1->Get("produceNtuple/eIDSimpleTree");
   TFile *f2 =new TFile("tree_testFastSim_TPG_checknow_thesameha_1normal.root");
   TTree *treeChain2 = (TTree*)f2->Get("produceNtuple/eIDSimpleTree");
   compairEmul(treeChain1,treeChain2);
}

//void emuldata(TTree *t1,TH1F *emuladc,int Pflag)
void emuldata(TTree *t1,TH1F *emuladc)
{   
   const int nTow = 4032,nEvent=0;
   int trig_tower_N_emul,trig_tower_ieta_emul[nTow],trig_tower_iphi_emul[nTow],trig_tower_adc_emul[nTow][5],trig_tower_sFGVB_emul[nTow][5];
   t1->SetBranchAddress("nEvent",&nEvent);
   t1->SetBranchAddress("trig_tower_N_emul",&trig_tower_N_emul);
   t1->SetBranchAddress("trig_tower_adc_emul",&trig_tower_adc_emul);
   Long64_t nentries = t1->GetEntries();
   for (Long64_t i=0;i<nentries;i++)
   {
      t1->GetEntry(i);
      for(int towerN=0;towerN<trig_tower_N_emul;towerN++)
      {
         if (trig_tower_adc_emul[towerN][2]>=3)
         {
  //          std::cout<<"trial print out  "<<trig_tower_adc_emul[towerN][2]<<std::endl;
            emuladc->Fill(trig_tower_adc_emul[towerN][2]);
         }
      }


   }
//  emuladc->Draw(); 
}





void compairEmul(TTree *t1,TTree *t2)
{
  char *legname="2012D Emul";
  string legendname[2]={"new Laser correction", "old Laser correction"};
  char *dirctoryname="PLOTS/%s";
  int colors[6] = {1,2,4,5,6,8};
  TH1F *EmulAdcRatioEB;
  EmulAdcRatioEB=new TH1F("emul EB ADC Ratio","Emul EB ADC Ratio",100,0,250);
  TH1F * EmulAdcEB[2];
  EmulAdcEB[0]=new TH1F("emul EB ADC compare1","Emul EB ADC compare1",100,0,250);
  EmulAdcEB[1]=new TH1F("emul EB ADC compare11","Emul EB ADC compare11",100,0,250);
  TH1F * EmulAdcEE[2];
  EmulAdcEE[0]=new TH1F("emul EE ADC compare1","Emul EE ADC compare1",100,0,250);
  EmulAdcEE[1]=new TH1F("emul EE ADC compare11","Emul EE ADC compare11",100,0,250);
  emuldata(t1,EmulAdcEB[0]);
  emuldata(t2,EmulAdcEB[1]);
  RatioHist(EmulAdcEB[0],EmulAdcEB[1],EmulAdcRatioEB);
  EmulAdcRatioEB->Draw();
//  formatHisto(0,legname,legendname,"Emul ADC",0,150,"EmulADC", colors,&EmulAdc[0],2,"EmulADC_new_before.pdf",dirctoryname); 
//  formatHisto(0,legname,legendname,"Emul ADC",0,250,"EmulADC ratio", colors,&EmulAdcRatio,1,"EmulADC_ratio.pdf",dirctoryname); 
}

void RatioHist(TH1F *t1,TH1F *t2,TH1F *t3)
{
   int nb1=0,nb2=0,nb3=0;
   nb1=t1->GetSize()-2; 
   nb2=t2->GetSize()-2; 
   for(int i=1;i<=100;i++)
   {
    if(t2->GetBinContent(i)!=0) 
       t3->SetBinContent(i,(t1->GetBinContent(i))/(t2->GetBinContent(i)));
   }


}
