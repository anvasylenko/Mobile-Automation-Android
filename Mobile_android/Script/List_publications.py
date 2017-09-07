from Read_Test_Data_From_Excel import *
from General_function import *


def ListPublicutoionsAllTestCases():
    ListPublicutoions(1)
    ListPublicutoions(2)
    ListPublicutoions(3)
    ListPublicutoions(4)

     
    
def ListPublicutoions(TestCaseNumber):
     
    Log.AppendFolder("ListPublicutoions")
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    btnListPublications = oApp.Find("ViewID", "dashboard_item_list_publications" , 10)
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("List_Publicutoions", TestCaseNumber)
    
    if btnListPublications.Exists:
        btnListPublications.Touch()
    
    btnContinue = oApp.Find("ViewID", "btn_continue", 20)
    txtSearch = oApp.Find("ViewID", "txt_search", 20)
    
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
    searchResult = oApp.Find("ViewID", "txt_identifier", 20)
    counter = oApp.Find("ViewID", "txt_totals", 20)
    
    if searchResult.getText().toString() == newMap['search']:
       Log.Message ("Title/ISBN/ISSN is correct")
    else:
       Log.Warning("Title/ISBN/ISSN is not correct")
	  
#    if counter.getText().toString() == newMap['counter']:         
#       Log.Message ("Counter is correct")
#    else:
#       Log.Warning("Counter is not correct")
    
    Log.Message(counter.getText().toString())

	  
    if int(newMap['save_and_continue']) == 1:
        btnSaveContinue.Touch()
        Delay(1000)
        txtSearch = oApp.Find("ViewID", "txt_search", 20)
        if txtSearch.Exists:
            Log.Message("PASS. Save and continue works")
        else:
            Log.Warning("Save and continue does not work")
           
		  
		  
    if int(newMap['finish_and_send_yes']) == 1:
        btnFinishSend.Touch()
        Delay(200)
        btnYes = oApp.Find("ViewID", "yes_button" , 20)
        btnYes.Touch()
        Delay(200)
        txtMessage = oApp.Find("ViewID", "lbl_results_uploaded" , 20)
        if txtMessage.Exists:
            Log.Message("PASS. Finish and send works")
            btnBack = oApp.Find("ViewID", "btn_finish_button" , 20)
            btnBack.Touch()
           
        else:
            Log.Warning("Finish and send does not work")
            
		  
    if int(newMap['finish_and_send_no']) == 1:
        btnFinishSend.Touch()
        Delay(200)
        btnNo = oApp.Find("ViewID", "no_button" , 20)
        btnNo.Touch()
        Delay(200)
        if searchResult.Exists:
            Log.Message("PASS. Finish and send No works")
            oDevice.PressBack()
            
        else:
            Log.Warning("Finish and send No does not work")
            

    Log.PopLogFolder()
    
