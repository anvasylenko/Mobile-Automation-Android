﻿from Read_Test_Data_From_Excel import *
from General_function import *

def LogCopyingPublish():
    Log.AppendFolder("LogCopyingPublish")
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications" , 10)

    if btnLogCopying.Exists:
        btnLogCopying.Touch()
	   
    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
	   
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Log_copying_publications", 2)
    
    if int(newMap['take_photo']) == 1:
        TakePhoto("ideftifier_page")
 
    btnContinue.Touch()
    
    oISBN = oApp.Find("ViewID", "txt_isbn_title" , 10)
    oUsage = oApp.Find("ViewID", "spinner_usage" , 10)
    oNumCopies = oApp.Find("ViewID", "txt_copies_made" , 10)
    oFrom1 = oApp.Find("ViewID", "txt_from" , 20)
    oTo1 = oApp.Find("ViewID", "txt_to" , 20)
    btnAddpageRange = oApp.Find("ViewID", "btn_add_page_range" , 10)
    oPageRange = oApp.Find("ViewID", "container_page_range" , 10)
    ISBN = oApp.Find("ViewID", "txt_isbn_title" , 10)

    

#    #Check ISBN
#    if ISBN.getText().toString() == newMap['isbn']:
#        Log.Message ("ISBN is correct")
#    else:
#        Log.Message("ISBN is NOT correct")
#	   
	# Set data
    Delay(500)   
    oUsage.TouchItem(newMap['usage'])
    oNumCopies.Keys(newMap['copies_made'])
    oFrom1.Keys(newMap['from'])
    oTo1.Keys(newMap['to'])
    
#    if int(newMap['add_page_range']) == 1:
#        btnAddpageRange.Touch()
#	   
#        oSecondPageRange = oPageRange.Layout("NO_ID", 2).Layout("NO_ID").Layout("NO_ID")
#        oThirdPageRange = oPageRange.Layout("NO_ID", 3).Layout("NO_ID").Layout("NO_ID")
#        oFourthPageRange = oPageRange.Layout("NO_ID", 4).Layout("NO_ID").Layout("NO_ID")
#        oFifthPageRange = oPageRange.Layout("NO_ID", 5).Layout("NO_ID").Layout("NO_ID")
#     
#    
#        oFrom2 = oSecondPageRange.EditText("txt_from")
#        oTo2 = oSecondPageRange.EditText("txt_to")
    #    oFrom2.Keys("11")
    #    oto2.Keys("12")
#    
#        oFrom3 = oThirdPageRange.EditText("txt_from")
#        oTo3 = oThirdPageRange.EditText("txt_to")
#    
#        oFrom4 = oFourthPageRange.EditText("txt_from")
#        oTo4 = oFourthPageRange.EditText("txt_to")
#    
#        oFrom5 = oFifthPageRange.EditText("txt_from")
#        oTo5 = oFifthPageRange.EditText("txt_to")

    btnContinue = oApp.Find("ViewID", "btn_continue" , 10)
    btnContinue.Touch()
    
    # Chech message and Log.Message("Data was loogged") 
    oMessageScreen = oApp.Find("ViewID", "log_finished_view", 20)
    oMessage = oMessageScreen.Layout("NO_ID").Layout("relativeLayout").TextView("NO_ID").getText().toString()
    
    if oMessage == "Your data has been submitted.":
        Log.Message(oMessage)
    else:
        Log.Warning("Successful Message does not appared")

    btnLogAnoterTitle = oApp.Find("ViewID", "btn_finish_button", 10)
    btnLogAnoterTitle.Touch()	   

    
#    Delay(200)
#    obtBack = oApp.ScreenWhatToDo.btnLogCopying.ScreenLogCopyingFinish.btnBack
#    obtnClose = oApp.ScreenWhatToDo.btnLogCopying.ScreenLogCopyingFinish.btnClose
#    
#    obtBack.Touch()
#    
#    oSingleResult = oApp.ScreenWhatToDo.btnLogCopying.allSearchResults.SingleResult
#    
#    if oSingleResult.Exists:
#        Log.Message("back works")

#    oDevice.PressBack()

    Log.PopLogFolder()