from General_function import *

def LogCopyingMusic():
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnLogCopyingMusic = oApp.Find("ViewID", "dashboard_item_log_copying_printed_music" , 20)
    btnLogCopyingMusic.Touch()
    
    btnTakePhotoFirst = oApp.Find("ViewID", "btn_take_photo_first" , 20)
    btnTakePhotoFirstImg = oApp.Find("ViewID", "btn_take_photo_first_img" , 20)
    btnTakePhoto = oApp.Find("ViewID", "btn_take_photo" , 20)
    btnTakePhotoImg = oApp.Find("ViewID", "btn_take_photo_img" , 20)
    btnScan = oApp.Find("btn_scan", "" , 20)
    btnScanImg = oApp.Find("ViewID", "btn_scan_img" , 20)
    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
    
    btnTakePhotoFirst.Touch()
    #Take a photo of first page
    ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
    ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
    Delay(200)
  
    btnTakePhoto.Touch()
    #Take a photo
    ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
    ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
    Delay(200)
    
    
    
    
    oApp.ScreenWhatToDo.txtSearch.Keys("the best music")
    btnContinue.Touch()
    
    LogCopyingPubl()
    
#    oDevice.PressBack()