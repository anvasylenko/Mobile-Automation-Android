def restart():
    Mobile.SetCurrent("emulator-5554")
#    TestedApps.CLA.Run()
    Delay(500)
    oApp = Aliases.Mobile.Device.App
    oApp.Restart()
    
def viewTutorial():
    Log.AppendFolder("viewTutorial")
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    Delay(2000)
#    oApp.Touch()
    
    Mobile.Device().Drag(50, 70, 30, 150, 500)
    Delay(500)
#    oDevice.Drag(262, 378, -274, 9)
#    oDevice.Drag(84, 365, 243, 16)
#    oDevice.Drag(84, 365, 243, 16)
   
    Delay(500)
#    oApp.btnSkipContinue.Touch()
    Log.PopLogFolder()