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
    oApp.btnSkipContinue.Touch()
    Log.PopLogFolder()
    

def checkBarCode():
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    btnBarcode = oApp.Find("ViewID", "btn_scan", 10)
    Delay(200)
    btnBarcode.Touch()
    Delay(200)
    Picture = Mobile.Device().Desktop.Picture()
    Log.Picture(Picture, "Device screenshot")
    Log.Checkpoint("PASS. Barcode button works")
    oDevice.PressBack()
    
    
    
def InstallAgent():
  AgentApkPath = "<TestComplete 11>\\Bin\\Extensions\\Android\\AndroidAgent.apk";
  Agent = Mobile.Device().PackageManager.GetPackageFromAPK(AgentApkPath);
  Mobile.Device().PackageManager.InstallPackage(Agent);