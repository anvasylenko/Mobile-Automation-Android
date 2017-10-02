from Read_Test_Data_From_Excel import *
from Log_copying import *
from Take_Photo import *
from General_functions import *

    
def LogCopyingPublications(TestCaseNumber):
         
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Log_copying_publications", TestCaseNumber)
 
    Log.AppendFolder(VarToString(TestCaseNumber) + " - Log_copying_publications: " + (newMap['tc_name']))
    
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    
    # All this code goes to the "Log copying" screen under diffirent condotions
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications" , 20)
    if btnLogCopying.Exists:
           btnLogCopying.Touch()
		 
    screenTitle = oApp.Find("ViewID", "txt_title" , 20) 
    if screenTitle.getText().toString() != "Log copying":
       oDevice.PressBack()
       Delay(500)
	  
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications", 20)
    if btnLogCopying.Exists:
        btnLogCopying.Touch()
	   
    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
    txtSearch = oApp.Find("ViewID", "txt_search" , 20)

    
    # Barcode button checking
    if int(newMap['barcode_check']) == 1:
        checkBarCode()
        Log.PopLogFolder()
        return None
	   
	   
    if int(newMap['take_photo']) == 1:
        TakePhoto("identifier_page")

	   
    if int(newMap['photo_cancel']) == 1:
        btnRemove = oApp.Find("ViewID", "remove_image", 10)
        if not btnRemove.Exists:
            Log.Warning("Remove button does not exists")
        else:
            btnRemove.Touch()
            delay(500)
            btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo", 20)
            if btnTakePhotoIdentPage.Exists: 
                Log.Message("Photo was removed successful")
            else:
                Log.Warning("Photo was not removed")
  
    btnContinue.Touch()
    delay(1000)
    
    
    if int(newMap['tc_fail_search']) == 1:
        txtSearch = oApp.Find("ViewID", "txt_search" , 20)
        if txtSearch.Exists:
            Log.Checkpoint("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None
		  
    LogCopying("Log_copying_publications", TestCaseNumber)
    
    Log.PopLogFolder()
    
    

def test(): 
    LogCopyingPublications(1)

    
    
