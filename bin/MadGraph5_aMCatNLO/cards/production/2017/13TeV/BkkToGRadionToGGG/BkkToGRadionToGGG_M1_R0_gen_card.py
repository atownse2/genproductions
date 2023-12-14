#! /bin/env python
import os
import sys
from shutil import copyfile

class Cards():
    def __init__(self,Mass_BKK_R):
        self.Mass_BKK_R = Mass_BKK_R
        self.TempleteFolder = "BkkToGRadionToGGG_M1_R0"
        self.BkkToGRadionToGGG_M1_R0_customizecards = "BkkToGRadionToGGG_M1_R0_customizecards.dat"
        self.BkkToGRadionToGGG_M1_R0_extramodels = "BkkToGRadionToGGG_M1_R0_extramodels.dat"
        self.BkkToGRadionToGGG_M1_R0_proc_card = "BkkToGRadionToGGG_M1_R0_proc_card.dat"
        self.BkkToGRadionToGGG_M1_R0_run_card = "BkkToGRadionToGGG_M1_R0_run_card.dat"

    def Cards(self):
        mBKK, mR = self.Mass_BKK_R
        BASEDIR = "BkkToGRadionToGGG_M1-%s_R0-%s"%(str(mBKK),str(mR))
        if not os.path.isdir(BASEDIR):
            os.makedirs(BASEDIR)
        with open("%s/%s"%(self.TempleteFolder,self.BkkToGRadionToGGG_M1_R0_customizecards),"r") as fin, open("%s/%s_customizecards.dat"%(BASEDIR,BASEDIR),"w") as fout:
            fout.write(fin.read().format(BKK_mass = str(mBKK),Radion_mass =(mR)))
        with open("%s/%s"%(self.TempleteFolder,self.BkkToGRadionToGGG_M1_R0_proc_card),"r") as fin, open("%s/%s_proc_card.dat"%(BASEDIR,BASEDIR),"w") as fout:
            fout.write(fin.read().format(BKK_mass = str(mBKK),Radion_mass =(mR)))
        copyfile("%s/%s"%(self.TempleteFolder,self.BkkToGRadionToGGG_M1_R0_run_card),"%s/%s_run_card.dat"%(BASEDIR,BASEDIR))
        copyfile("%s/%s"%(self.TempleteFolder,self.BkkToGRadionToGGG_M1_R0_extramodels),"%s/%s_extramodels.dat"%(BASEDIR,BASEDIR))

m_bkk_r = sys.argv[1], sys.argv[2]

cards = Cards(m_bkk_r)
cards.Cards()
