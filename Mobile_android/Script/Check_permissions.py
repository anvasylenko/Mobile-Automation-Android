from Log_copying_publications import *
from Read_Test_Data_From_Excel import *

    
def checkPermissionTest(TestCaseNumber):
    Log.AppendFolder("checkPermissionTest")
    oApp = Aliases.Mobile.Device.App
    oDevice = Aliases.Mobile.Device
    
    btnLogCopying = oApp.ScreenWhatToDo.btnLogCopying
    btnLogCopying.Touch()
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Check_Permissions", TestCaseNumber)
    
    Log.Message(newMap['tc_name'])
    
    # Set search data
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    txtSearch.Keys(newMap['search'])
#    oApp.ScreenWhatToDo.txtSearch.Keys(newMap['search'])
    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
    btnContinue.Touch()
    Delay(3000)
    
    
    if int(newMap['tc_fail']) == 1:
        if txtSearch.Exists:
            Log.Message("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None
    
    
    # if searched results more than 1
    if int(newMap['results_count']) != 1:
        oForSearch = oApp.Find("ViewID", "layout_multiple_results" , 40)
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

    # Check data
    oTitle = oApp.Find("ViewID", "txt_book_title" , 20)
    oISBN = oApp.Find("ViewID", "txt_isbn_issn" , 20)
    oType = oApp.Find("ViewID", "txt_type" , 20)
    oForm = oApp.Find("ViewID", "txt_form" , 20)
    oCountry = oApp.Find("ViewID", "txt_country" , 30)
    oPublisher = oApp.Find("ViewID", "txt_publisher" , 30)
    oLicence = oApp.Find("ViewID", "txt_licence" , 30)
      
    if oTitle.getText().toString() == newMap['title']:
        Log.Message ("Title is correct")
    else:
        Log.Warning("Title is not correct")
	    
    Delay(200)	    
    if newMap['type'] == "Web Domain":
        if oISBN.getText().toString() == newMap['url']:
             Log.Message ("url is correct")
        else:
             Log.Message("url is not correct")
    else:
        if oISBN.getText().toString() == newMap['isbn']:
            Log.Message ("oISBN is correct")
        else:
            Log.Message("oISBN is not correct")
    
    Delay(200)	    
    if oType.getText().toString() == newMap['type']:
        Log.Message ("oType is correct")
    else:
        Log.Message("oType is not correct")
	
    Delay(200)	   
    if oForm.getText().toString() == newMap['form']:
        Log.Message ("oForm is correct")
    else:
        Log.Message("oForm is not correct")
    
    Delay(200)	    	   
    if oCountry.getText().toString() ==  newMap['country']:
        Log.Message (oCountry.getText().toString())
        Log.Message ("oCountry is correct")
    else:
        Log.Message("oCountry is not correct")
    
    Delay(200)	   	   
    if oPublisher.getText().toString() == newMap['publisher']:
        Log.Message ("oPublisher is correct")
        Log.Message ("oPublisher is correct")
    else:
        Log.Message(oPublisher.getText().toString())
    
    # Check licence
    Delay(200)	
    btnMenu = oApp.Find("ViewID", "drawer_button", 10)
    btnMenu.Touch()
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite", 10).getText().toString()     
    oDevice.PressBack()
    if oLicence.getText().toString() == txtLicence:
        Log.Message ("oLicence is correct")
    else:
        Log.Message("oLicence is not correct")
	
    #Check Licence Usage
    if oForm.getText().toString() == "print":
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
    elif oForm.getText().toString() == "digital":
        oDigital = oApp.Find("ViewID", "help_icon", 20)
        oDigital.Touch()
        oApp.btnScreenClose.Touch()
        Log.Message("Digital screen is shown")
    else:
        Log.Message("oForm is not correct")
    
    #Go to Log Copying or Check another permission
    Delay(200)	
    btnCheckAnotherPermission = oApp.Find("ViewID", "btn_check_another", 40)
    obtnLogCopying = oApp.Find("ViewID", "btn_log", 20)
    
    if int(newMap['log_copying']) == 0:
        btnCheckAnotherPermission.Touch()
        if oApp.ScreenWhatToDo.txtSearch.Exists:
            Log.Message("Check permissions is shown. CheckAnotherPermission button works")
        else:
            Log.Message("Check permissions is NOT shown. CheckAnotherPermission button does not work")
    else:     
        obtnLogCopying.Touch()
        LogCopyingPublish(5)

    Log.PopLogFolder()
    



