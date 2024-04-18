#! /bin/env python
import os
import sys
from shutil import copyfile

cards_dir = os.path.dirname(os.path.abspath(__file__))

class Cards():
    def __init__(self,Mass_BKK_R):
        self.Mass_BKK_R = Mass_BKK_R
        self.TempleteFolder = os.path.join(cards_dir, "BkkToGRadionToGGG_M1_R0")
        self.BkkToGRadionToGGG_M1_R0_customizecards = "BkkToGRadionToGGG_M1_R0_customizecards.dat"
        self.BkkToGRadionToGGG_M1_R0_extramodels = "BkkToGRadionToGGG_M1_R0_extramodels.dat"
        self.BkkToGRadionToGGG_M1_R0_proc_card = "BkkToGRadionToGGG_M1_R0_proc_card.dat"
        self.BkkToGRadionToGGG_M1_R0_run_card = "BkkToGRadionToGGG_M1_R0_run_card.dat"

    def Cards(self):
        mBKK, mR = self.Mass_BKK_R
        fragment = "BkkToGRadionToGGG_M1-%s_R0-%s"%(str(mBKK),str(mR))
        BASEDIR = os.path.join(cards_dir, fragment)
        if not os.path.isdir(BASEDIR):
            os.makedirs(BASEDIR)

        _customize = os.path.join(self.TempleteFolder, self.BkkToGRadionToGGG_M1_R0_customizecards)
        customize = os.path.join(BASEDIR, fragment+"_customizecards.dat")
        with open(_customize,"r") as fin, open(customize,"w") as fout:
            fout.write(fin.read().format(BKK_mass = str(mBKK),Radion_mass =(mR)))
        
        _proc = os.path.join(self.TempleteFolder, self.BkkToGRadionToGGG_M1_R0_proc_card)
        proc = os.path.join(BASEDIR, fragment+"_proc_card.dat")
        with open(_proc,"r") as fin, open(proc,"w") as fout:
            fout.write(fin.read().format(BKK_mass = str(mBKK),Radion_mass =(mR)))

        copyfile(
            os.path.join(self.TempleteFolder, self.BkkToGRadionToGGG_M1_R0_run_card),
            os.path.join(BASEDIR, fragment+"_run_card.dat")
            )
        
        copyfile(
            os.path.join(self.TempleteFolder, self.BkkToGRadionToGGG_M1_R0_extramodels),
            os.path.join(BASEDIR, fragment+"_extramodels.dat")
            )
    
m_bkk_r = sys.argv[1], sys.argv[2]

cards = Cards(m_bkk_r)
cards.Cards()
