from Read_Test_Data_From_Excel import *
from General_functions import *
from Log_copying import *
from Take_Photo import *
    
    
def LogCopyingMusic(TestCaseNumber):

    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Log_Copying_Music", TestCaseNumber)
    
    Log.AppendFolder(VarToString(TestCaseNumber) + " - Log_Copying_Music: " + (newMap['tc_name']))

    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    
    # All this code goes to the "Log copying of music" screen under diffirent conditions
    
    screenTitle = oApp.Find("ViewID", "txt_title", 20) 
    if screenTitle.getText().toString() == "Log copying of music":
       oDevice.PressBack()
       Delay(500)

    btnLogCopyingMusic = oApp.Find("ViewID", "dashboard_item_log_copying_printed_music", 20)
    if btnLogCopyingMusic.Exists:
        btnLogCopyingMusic.Touch()
	   
		 
    screenTitle = oApp.Find("ViewID", "txt_title", 20) 
    if screenTitle.getText().toString() != "Log copying of music":
       oDevice.PressBack()
       Delay(500)
	
    btnLogCopyingMusic = oApp.Find("ViewID", "dashboard_item_log_copying_printed_music", 20)
    if btnLogCopyingMusic.Exists:
        btnLogCopyingMusic.Touch()
	   
    
    btnTakePhotoFirst = oApp.Find("ViewID", "btn_take_photo_first", 20)
    btnTakePhotoFirstImg = oApp.Find("ViewID", "btn_take_photo_first_img", 20)
    btnTakePhoto = oApp.Find("ViewID", "btn_take_photo", 20)
    btnTakePhotoImg = oApp.Find("ViewID", "btn_take_photo_img", 20)
    btnScan = oApp.Find("btn_scan", "", 20)
    btnScanImg = oApp.Find("ViewID", "btn_scan_img", 20)
    btnContinue = oApp.Find("ViewID", "btn_continue", 10)
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    btnScanBarCode = oApp.Find("ViewID", "btn_scan", 20)
    
    
    # Barcode button checking
    if int(newMap['barcode_check']) == 1:
        checkBarCode()
        Log.PopLogFolder()
        return None
    
    # Take a photo of first page
    if int(newMap['take_photo_first_page']) == 1:
        TakePhoto("first_page")
    
    # Take a photo of identifier page
    if int(newMap['take_photo_identifier_page']) == 1:
        TakePhoto("identifier_page")
	
		 
    if int(newMap['first_page_cancel_photo']) == 1:
        btnRemove = oApp.Find("ViewID", "remove_first_page_image" , 10)
        if btnRemove.Exists:
            btnRemove.Touch()
            delay(200)
            btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo_first" , 20)
            if btnTakePhotoIdentPage.Exists:
                Log.Message("Photo was removed successful")
            else:
                Log.Warning("Photo was not removed") 
        else:
            Log.Warning("Remove button does not exists")

		  
    if int(newMap['ideftifier_page_cancel_photo']) == 1:
        btnRemove = oApp.Find("ViewID", "remove_identifier_image" , 20)
        if btnRemove.Exists:
            btnRemove.Touch()
            delay(200)
            btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo" , 20)
            if btnTakePhotoIdentPage.Exists:
                Log.Message("Photo was removed successful")
            else:
                Log.Warning("Photo was not removed") 
        else:
            Log.Warning("Remove button does not exists")
    

#    if int(newMap['search']) == 1:
    
    btnContinue.Touch()
    Delay(500)
    
    if int(newMap['tc_fail_search']) == 1:
        btnScanBarCode = oApp.Find("ViewID", "btn_scan" , 20)
        if btnScanBarCode.Exists:
            Log.Checkpoint("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None

    LogCopying("Log_Copying_Music", TestCaseNumber)
    
    Log.PopLogFolder()
    
    
    

        