from Read_Test_Data_From_Excel import *
from General_function import *

def LogCopyingPublishAllTestCases():
    LogCopyingPublish(1)
    LogCopyingPublish(2)
    LogCopyingPublish(3)
    LogCopyingPublish(3)
    LogCopyingPublish(4)
    LogCopyingPublish(5)
    
def LogCopyingPublish(TestCaseNumber):
    Log.AppendFolder(VarToString(TestCaseNumber) + " TC - LogCopyingPublish")
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications" , 20)
    if btnLogCopying.Exists:
           btnLogCopying.Touch()
		 
    screenTitle = oApp.Find("ViewID", "txt_title" , 20) 
    Log.Message(screenTitle.getText().toString())
    if screenTitle.getText().toString() != "Log copying":
       oDevice.PressBack()
       Delay(500)
	  
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications", 20)
    if btnLogCopying.Exists:
        btnLogCopying.Touch()
	   
    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
    txtSearch = oApp.Find("ViewID", "txt_search" , 20)
	   
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Log_copying_publications", TestCaseNumber)
    
    Log.Message((newMap['tc_name']))
    
    if int(newMap['take_photo']) == 1:
        TakePhoto("ideftifier_page")

	   
    if int(newMap['photo_cancel']) == 1:
        btnRemove = oApp.Find("ViewID", "remove_image" , 10)
        if not btnRemove.Exists:
            Log.Warning("Remove button does not exists")
        else:
            btnRemove.Touch()
            delay(500)
            btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo" , 20)
            if btnTakePhotoIdentPage.Exists: 
                Log.Message("Photo was removed successful")
            else:
                Log.Warning("Photo was not removed")
 
    btnContinue.Touch()
    delay(1000)
    
    if int(newMap['tc_fail_search']) == 1:
        txtSearch = oApp.Find("ViewID", "txt_search" , 20)
        if txtSearch.Exists:
            Log.Message("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None
		  
    LogCopying("Log_copying_publications", TestCaseNumber)
    
    Log.PopLogFolder()
    
    
