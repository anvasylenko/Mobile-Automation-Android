﻿from Read_Test_Data_From_Excel import *

def LogCopying(nameSheet, TestCaseNumber):
     
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
     
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel(nameSheet, TestCaseNumber)

    oISBN = oApp.Find("ViewID", "txt_isbn_title", 10)
    oUsage = oApp.Find("ViewID", "spinner_usage", 10)
    oNumCopies = oApp.Find("ViewID", "txt_copies_made", 10)
    oFrom1 = oApp.Find("ViewID", "txt_from", 20)
    oTo1 = oApp.Find("ViewID", "txt_to", 20)
    btnAddpageRange = oApp.Find("ViewID", "btn_add_page_range", 10)
    oPageRange = oApp.Find("ViewID", "container_page_range", 10)
    ISBN = oApp.Find("ViewID", "txt_isbn_title", 10)


    # Set data
    Delay(500)   
    oUsage.TouchItem(newMap['usage'])
    oNumCopies.Keys(newMap['copies_made'])
    oFrom1.Keys(newMap['from'])
    oTo1.Keys(newMap['to'])
    
    
    if int(newMap['add_page_range']) == 1:
        
        btnAddpageRange.Touch()
        oSecondPageRange = oPageRange.Layout("NO_ID", 2).Layout("NO_ID").Layout("NO_ID")
        oFrom2 = oSecondPageRange.Find("ViewID", "txt_from", 10)
        oFrom2.Keys("21")
        oPageRange = oApp.Find("ViewID", "container_page_range" , 20)
        oSecondPageRange = oPageRange.Layout("NO_ID", 2).Layout("NO_ID").Layout("NO_ID", 2)
        oTo2 = oSecondPageRange.EditText("txt_to")
        oTo2.Keys("22")
	   
	   
        btnAddpageRange.Touch()
        oThirdPageRange = oPageRange.Layout("NO_ID", 3).Layout("NO_ID").Layout("NO_ID")
        oFrom3 = oThirdPageRange.Find("ViewID", "txt_from" , 10)
        oPageRange = oApp.Find("ViewID", "container_page_range" , 20)
        oThirdPageRange = oPageRange.Layout("NO_ID", 3).Layout("NO_ID").Layout("NO_ID", 2)
        oTo3 = oThirdPageRange.EditText("txt_to")
        oFrom3.Keys("31")
        oTo3.Keys("32")
	   
	   
        btnAddpageRange.Touch()
        oFourthPageRange = oPageRange.Layout("NO_ID", 4).Layout("NO_ID").Layout("NO_ID")
        oFrom4 = oFourthPageRange.EditText("txt_from")
        oPageRange = oApp.Find("ViewID", "container_page_range" , 20)
        oFourthPageRange = oPageRange.Layout("NO_ID", 4).Layout("NO_ID").Layout("NO_ID", 2)
        oTo4 = oFourthPageRange.EditText("txt_to")
        oFrom4.Keys("41")
        oTo4.Keys("42")
    
	   
        btnAddpageRange.Touch()
        oFifthPageRange = oPageRange.Layout("NO_ID", 5).Layout("NO_ID").Layout("NO_ID")
        oFrom5 = oFifthPageRange.EditText("txt_from")
        oPageRange = oApp.Find("ViewID", "container_page_range", 20)
        oFifthPageRange = oPageRange.Layout("NO_ID", 5).Layout("NO_ID").Layout("NO_ID", 2)
        oTo5 = oFifthPageRange.EditText("txt_to")
        oFrom5.Keys("51")
        oTo5.Keys("52")
	   
        if btnAddpageRange.Visible:
            Log.Warning("Fail. Add Page Range button exists")
        else:
            Log.Checkpoint("PASS. Add Page Range button does not exist")
        

    btnContinue = oApp.Find("ViewID", "btn_continue", 10)
    btnContinue.Touch()
    Delay(3000)
    
    if int(newMap['tc_fail_log']) == 1:
        oUsage = oApp.Find("ViewID", "spinner_usage", 10)
        if oUsage.Exists:
            Log.Checkpoint("PASS. Test failed as expected")
            Delay(500)
            oDevice.PressBack()
            oDevice.PressBack()
            txtSearch = oApp.Find("ViewID", "txt_search", 20)
            if txtSearch.Exists:
                oDevice.PressBack()
        else:
            Log.Warning("Log Test did not failed as expected")
    else:
        oApp = Aliases.Mobile.Device.App
        oMessageScreen = oApp.Find("ViewID", "data_submitted", 20)
        if oMessageScreen.Exists:
            Log.Checkpoint(oMessageScreen.getText().toString())
            btnLogAnotherTitle = oApp.Find("ViewID", "btn_finish_button", 20)
            btnLogAnotherTitle.Touch()	   
            Delay(4000)
        else:
            Log.Warning("Successful Message does not appaered")
		  


    
      