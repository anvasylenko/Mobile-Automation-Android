﻿def restart():
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

    
def TC_RestartOnRePage():
    Log.AppendFolder("TC_RestartOnRePage") 
    restart()
    oApp = Aliases.Mobile.Device.App
	
     #This functionality does not work as expacted -> bug 
    if oApp.sreenChooseLicenceType.Exists:
        Log.Message("App continues from Registration screen")
    else:
        Log.Warning("App continues from OTHER screen")
	   
    Log.PopLogFolder()

def TakePhoto(whatPage):   # values: "first_page" and "ideftifier_page"
     
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnTakePhotoFirstPage = oApp.Find("ViewID", "btn_take_photo_first" , 20)
    btnTakePhotoFirstImg = oApp.Find("ViewID", "btn_take_photo_first_img" , 20)
    
    btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo" , 20)
    btnTakePhotoImg = oApp.Find("ViewID", "btn_take_photo_img" , 20)
    
    if whatPage == "first_page":
        btnTakePhotoFirstPage.Touch()
        #Take a photo of first page
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(300)
	   
    elif whatPage == "ideftifier_page":
        btnTakePhotoIdentPage.Touch()
        #Take a photo
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(300)
    

     
