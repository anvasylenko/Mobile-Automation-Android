from General_function import *

def before():
    Mobile.SetCurrent("emulator-5554")
    TestedApps.CLA.Run()
    Delay(500)
    
    TC_SkipRegisrtration()
   