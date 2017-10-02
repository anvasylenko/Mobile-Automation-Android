﻿from Log_copying_publications import *
from General_functions import *
from Read_Test_Data_From_Excel import *
from Log_copying import *

    
def checkPermissionTest(TestCaseNumber):
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Check_Permissions", TestCaseNumber)

    Log.AppendFolder(VarToString(TestCaseNumber) + " - Check_Permissions: " + (newMap['tc_name']))
    
    oApp = Aliases.Mobile.Device.App
    oDevice = Aliases.Mobile.Device
    
    btnLogCopying = oApp.ScreenWhatToDo.btnLogCopying
    btnLogCopying.Touch()
    
    
    # Barcode button checking
    if int(newMap['barcode_check']) == 1:
        checkBarCode()
        Log.PopLogFolder()
        return None
    
    
    # Set search data
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    txtSearch.Keys("^a")
    txtSearch.Keys("[BS]")
    txtSearch.Keys(newMap['search'])
    btnContinue = oApp.Find("ViewID", "btn_continue", 10)
    btnContinue.Touch()
    Delay(5000)
    
    
    if int(newMap['tc_fail']) == 1:
        if txtSearch.Exists:
            Log.Checkpoint("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None
    else:
         Delay(4000)

    
    oApp = Aliases.Mobile.Device.App
    noResultsMessage = oApp.Find("ViewID", "txt_results", 40)
    
    if not noResultsMessage.exists:
        Log.Checkpoint("Data was found")
    else:
        noResultsMessage = noResultsMessage.getText().toString()
        if noResultsMessage == "Found no results for:":
            Log.Warning("Found no results for: " + newMap['search'])
            Log.PopLogFolder()   
            oDevice.PressBack()  
            Log.PopLogFolder()       
            return None
        
	
	   
    # if searched results more than 1
    if int(newMap['results_count']) != 1:
        oForSearch = oApp.Find("ViewID", "layout_multiple_results", 40)
        oResult = oForSearch.ListView("list_results").Layout("NO_ID", 2).Layout("root_view").TextView("txt_book_title")
        Log.Message("Searching showns more than one results")
        oResult.Touch()
    else:
        oResult = oApp.Find("ViewID", "layout_single_results", 40)
        oSingleResult = oResult.ScrollView("NO_ID")
        if oSingleResult.Exists:
            Log.Message("Single result is shown")
        else:
            Log.Warning("Single result is not shown")
            Log.PopLogFolder()
            return None
    
    
		  
    # Check data
    oTitle = oApp.Find("ViewID", "txt_book_title" , 20)
    oISBN = oApp.Find("ViewID", "txt_isbn_issn" , 20)
    oType = oApp.Find("ViewID", "txt_type" , 20)
    oForm = oApp.Find("ViewID", "txt_form" , 20)
    oCountry = oApp.Find("ViewID", "txt_country" , 30)
    oPublisher = oApp.Find("ViewID", "txt_publisher" , 30)
    oLicence = oApp.Find("ViewID", "txt_licence" , 30)
    checkData = True
    
    if oTitle.getText().toString() == newMap['title']:
        Log.Message ("Title is correct")
    else:
        Log.Warning("Title is not correct")
        checkData = False
	    
    Delay(200)	    
    if newMap['type'] == "Web Domain":
        if oISBN.getText().toString() == newMap['url']:
             Log.Message ("url is correct")
        else:
             Log.Message("url is not correct")
             checkData = False
    else:
        if oISBN.getText().toString() == newMap['isbn']:
            Log.Message ("oISBN is correct")
        else:
            Log.Message("oISBN is not correct")
            checkData = False
    
    Delay(200)	    
    if oType.getText().toString() == newMap['type']:
        Log.Message ("oType is correct")
    else:
        Log.Message("oType is not correct")
        checkData = False
	
    Delay(200)	   
    if oForm.getText().toString() == newMap['form']:
        Log.Message ("oForm is correct")
    else:
        Log.Message("oForm is not correct")
        checkData = False
    
    Delay(200)	    	   
    if oCountry.getText().toString() ==  newMap['country']:
        Log.Message ("oCountry is correct")
    else:
#        Log.Message (oCountry.getText().toString())
        Log.Message("oCountry is not correct")
        checkData = False
    
    Delay(200)	   	   
    if oPublisher.getText().toString() == newMap['publisher']:
        Log.Message ("oPublisher is correct")
    else:
        Log.Message(oPublisher.getText().toString())
        Log.Warning ("oPublisher is not correct")
        checkData = False
    
    # Check licence
    Delay(200)	
    btnMenu = oApp.Find("ViewID", "drawer_button", 10)
    btnMenu.Touch()
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite", 10).getText().toString()     
    oDevice.PressBack()
    if oLicence.getText().toString() == txtLicence:
        Log.Message ("oLicence is correct")
    else:
        Log.Warning("oLicence is not correct")
	
    # Check Licence Usage
    if oForm.getText().toString() == "Print":
        oPerm = oApp.Find("ViewID", "permissions_container", 20)
        oPhotocopying = oPerm.Layout("NO_ID").Layout("root_view").TextView("txt_name")
        oPhotocopying.Touch()
        oApp.btnScreenClose.Touch()
        Log.Message("Photocopying screen is shown")
       
	   ####### -> need to add draging
	   
#        oScaning = oApp.Layout("NO_ID", 2).Layout("root_view").TextView("txt_name")
#        oScaning.Touch()
#        oApp.btnScreenClose.Touch()
#        Log.Message("Scaning screen is shown")
    elif oForm.getText().toString() == "Digital":
        oDigital = oApp.Find("ViewID", "help_icon", 20)
        oDigital.Touch()
        oApp.btnScreenClose.Touch()
        Log.Message("Digital screen is shown")
    elif oForm.getText().toString() == "Print & Digital":
        oDigital = oApp.Find("ViewID", "help_icon", 20)
        oDigital.Touch()
        oApp.btnScreenClose.Touch()
        Log.Message("Digital screen is shown")
    else:
        Log.Warning("oForm is not correct")
      
	
   
    if checkData == True:
        Log.Checkpoint("PASS. All data are macthed")
    else:
        Log.Warning("Fail. Not all data are macthed")
    
	   
    # Go to Log Copying or Check another permission
    Delay(200)	
    btnCheckAnotherPermission = oApp.Find("ViewID", "btn_check_another", 40)
    obtnLogCopying = oApp.Find("ViewID", "btn_log", 20)
    
    if int(newMap['log_copying']) == 0:
        btnCheckAnotherPermission.Touch()
        if oApp.ScreenWhatToDo.txtSearch.Exists:
            Log.Message("Check permissions is shown. CheckAnotherPermission button works")
        else:
            Log.Warning("Check permissions is NOT shown. CheckAnotherPermission button does not work")
    else:     
        obtnLogCopying.Touch()
        LogCopying("Check_Permissions", TestCaseNumber)

    Log.PopLogFolder()
    
    
def test():
    checkPermissionTest(3)
#    LogCopyingPublications(9)
