from Read_Test_Data_From_Excel import *
from General_function import *


def LogCopyingMusicAllTestCases():
    LogCopyingMusic(1)
    LogCopyingMusic(2)
    LogCopyingMusic(3)
    LogCopyingMusic(4)
    LogCopyingMusic(5)
    LogCopyingMusic(6)
    LogCopyingMusic(7)
    LogCopyingMusic(8)
    LogCopyingMusic(9)
    LogCopyingMusic(10)
    LogCopyingMusic(11)
    LogCopyingMusic(12)
    LogCopyingMusic(13)
    LogCopyingMusic(14)
    
    
    
    
def LogCopyingMusic(TestCaseNumber):
 
    Log.AppendFolder(VarToString(TestCaseNumber) + " TC - LogCopyingMusic")
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    screenTitle = oApp.Find("ViewID", "txt_title" , 20) 
    Log.Message(screenTitle.getText().toString())
    if screenTitle.getText().toString() == "Log copying of music":
       oDevice.PressBack()
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Log_Copying_Music", TestCaseNumber)
    
    Log.Message(newMap['tc_name'])

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
    
    # Take a photo of first page
    if int(newMap['take_photo_first_page']) == 1:
        TakePhoto("first_page")
    
    # Take a photo of ideftifier page
    if int(newMap['take_photo_ideftifier_page']) == 1:
        TakePhoto("ideftifier_page")
	
		 
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
    
#    oDevice.PressBack()
    Log.PopLogFolder()
    
    
    

        