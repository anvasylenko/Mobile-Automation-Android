﻿from Read_Test_Data_From_Excel import *
from Take_Photo import *

     
def ListPublications(TestCaseNumber):
     
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("List_Publications", TestCaseNumber)
    
    Log.AppendFolder(VarToString(TestCaseNumber) + " - List_Publications: " + (newMap['tc_name']))
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    
    # All this code goes to the "Log copying" screen under diffirent conditions
    btnListPublications = oApp.Find("ViewID", "dashboard_item_list_publications", 10)
    if btnListPublications.Exists:
        btnListPublications.Touch()
	   
    screenTitle = oApp.Find("ViewID", "txt_title", 20)
    if screenTitle.getText().toString() != "List Publications":
       oDevice.PressBack()
       Delay(500)
	
    btnListPublications = oApp.Find("ViewID", "dashboard_item_list_publications", 10)  
    if btnListPublications.Exists:
        btnListPublications.Touch()
	   
	
    # Set search data and press Continue button
    btnContinue = oApp.Find("ViewID", "btn_continue", 20)
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    txtSearch.Keys("^a")
    txtSearch.Keys("[BS]")
    txtSearch.Keys(newMap['search'])
    btnContinue.Touch()
    Delay(1000)
    
    
    if int(newMap['tc_fail']) == 1:
        if txtSearch.Exists:
            Log.Message("PASS. Test failed as expected")
            Log.PopLogFolder()
            return None
        else:
            Log.Warning("Test is not failed as expected")
            Log.PopLogFolder()
            return None
    
    btnSaveContinue = oApp.Find("ViewID", "btn_save_continue", 20)
    btnFinishSend = oApp.Find("ViewID", "btn_finish_send", 30)
    searchResultTitleIsbnIssn = oApp.Find("ViewID", "txt_identifier", 20)
    counter = oApp.Find("ViewID", "txt_totals", 20)
    
    if searchResultTitleIsbnIssn.getText().toString() == newMap['search']:
       Log.Checkpoint ("Title/ISBN/ISSN is correct")
    else:
       Log.Warning("Title/ISBN/ISSN is not correct")
	  
	  
	# code will be implemeted in the future
#        txtMessage = oApp.Find("ViewID", "data_submitted", 20)
#        txtMessage = txtMessage.split()  
#    if counter.getText().toString() == newMap['counter']:         
#       Log.Message ("Counter is correct")
#    else:
#       Log.Warning("Counter is not correct")
#    Log.Message(counter.getText().toString())

	  
    if int(newMap['save_and_continue']) == 1:
        btnSaveContinue.Touch()
        Delay(1000)
        txtSearch = oApp.Find("ViewID", "txt_search", 20)
        if txtSearch.Exists:
            Log.Checkpoint("PASS. Save and continue works")
        else:
            Log.Warning("Save and continue does not work")
           
		  
    if int(newMap['finish_and_send_yes']) == 1:
        btnFinishSend.Touch()
        Delay(200)
        btnYes = oApp.Find("ViewID", "yes_button", 20)
        btnYes.Touch()
        Delay(1000)
        txtMessage = oApp.Find("ViewID", "data_submitted", 20)
        Log.Message(txtMessage.getText().toString())
        if txtMessage.Exists:
            Log.Checkpoint("PASS. Finish and send works")
            btnBack = oApp.Find("ViewID", "btn_finish_button", 20)
            btnBack.Touch()
        else:
            Log.Warning("Finish and send does not work")
            
		  
    if int(newMap['finish_and_send_no']) == 1:
        btnFinishSend.Touch()
        Delay(200)
        btnNo = oApp.Find("ViewID", "no_button", 20)
        btnNo.Touch()
        Delay(200)
        if btnFinishSend.Exists:
            Log.Checkpoint("PASS. Finish and send No works")
            btnSaveContinue.Touch()
        else:
            Log.Warning("Finish and send No does not work")
            

    Log.PopLogFolder()
    


     
