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
   
    Mobile.Device().Drag(50, 70, 30, 150, 500)
    Delay(500)
#    oDevice.Drag(262, 378, -274, 9)
#    oDevice.Drag(84, 365, 243, 16)
#    oDevice.Drag(84, 365, 243, 16)
   
    Delay(500)
    oApp.btnSkipContinue.Touch()
    Log.PopLogFolder()
    
def InstallAgent():
  AgentApkPath = "<TestComplete 11>\\Bin\\Extensions\\Android\\AndroidAgent.apk";
  Agent = Mobile.Device().PackageManager.GetPackageFromAPK(AgentApkPath);
  Mobile.Device().PackageManager.InstallPackage(Agent);