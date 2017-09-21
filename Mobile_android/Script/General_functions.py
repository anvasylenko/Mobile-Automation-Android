def restart():
    Mobile.SetCurrent("emulator-5554")
#    TestedApps.CLA.Run()
    Delay(500)
    oApp = Aliases.Mobile.Device.App
    oApp.Restart()
    
def TC_SkipRegisrtration():
    Log.AppendFolder("TC_SkipRegisrtration")
    oApp = Aliases.Mobile.Device.App
#    oApp.sreenChooseLicenceType.Drag(5,5, 0, 500)
#    oApp.sreenChooseLicenceType.Drag(5,5, 0, 500)
#    oApp.sreenChooseLicenceType.Drag(67, 304, 224, 1)
#    oApp.sreenChooseLicenceType.Drag(67, 304, 224, 1)
   
    Delay(500)
    oApp.btnSkipContinue.Touch()
    Log.PopLogFolder()
