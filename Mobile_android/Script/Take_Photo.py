﻿def TakePhoto(whatPage):   # values: "first_page" and "ideftifier_page"
     
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnTakePhotoFirstPage = oApp.Find("ViewID", "btn_take_photo_first" , 20)
    btnTakePhotoFirstImg = oApp.Find("ViewID", "btn_take_photo_first_img" , 20)
    
    btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo" , 20)
    btnTakePhotoImg = oApp.Find("ViewID", "btn_take_photo_img" , 20)
    
    if whatPage == "first_page":
        btnTakePhotoFirstPage.Touch()
       # Take a photo of first page
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(1000)
	   
    elif whatPage == "ideftifier_page":
        btnTakePhotoIdentPage.Touch()
        #Take a photo
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(1000)