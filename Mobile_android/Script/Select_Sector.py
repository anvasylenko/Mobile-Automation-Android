﻿def SelectSector(changeSector, sector):
    Log.AppendFolder("SelectSector")
    oApp = Aliases.Mobile.Device.App
    
    if changeSector == 1:
        btnMenu = oApp.Find("ViewID", "drawer_button" , 10)
        btnMenu.Touch()
	   
        btnChangeSector = oApp.Find("ViewID", "btn_change" , 10)
        btnChangeSector.Touch()
    
    if sector == "Schools":
        oApp.sreenChooseLicenceType.spinnerLicenceType.Touch()
        spinnerChooseLicenceType = Mobile.Device("emulator-5554").Process("com.eman.clatitlesearchs").RootLayout("", 2).Layout("content").Layout("parentPanel").Layout("NO_ID").ListView("list_items")
        spinnerChooseLicenceType.Child(1).touch()
	   
        oApp.sreenChooseLicenceType.spinnerSector.Touch()
        spinnerSector = Mobile.Device("emulator-5554").Process("com.eman.clatitlesearchs").RootLayout("", 2).Layout("content").Layout("parentPanel").Layout("NO_ID").ListView("list_items")
        spinnerSector.Child(0).touch()
        Log.Message("schools was choosen successfully")
    
    else:
        oApp.sreenChooseLicenceType.spinnerLicenceType.Touch()
        spinnerChooseLicenceType = Mobile.Device("emulator-5554").Process("com.eman.clatitlesearchs").RootLayout("", 2).Layout("content").Layout("parentPanel").Layout("NO_ID").ListView("list_items")
        spinnerChooseLicenceType.Child(2).touch()
	   
        oApp.sreenChooseLicenceType.spinnerSector.Touch()
        spinnerSector = Mobile.Device("emulator-5554").Process("com.eman.clatitlesearchs").RootLayout("", 2).Layout("content").Layout("parentPanel").Layout("NO_ID").ListView("list_items")
        spinnerSector.Child(2).touch()
        Log.Message("other was choosen successfully")
    
    oApp.btnSkipContinue.Touch()
    
    if changeSector == 1:
        CheckOptionsToSector()
	   
    Log.PopLogFolder()
    
    
def CheckOptionsToSector():     
    Log.AppendFolder("CheckOptionsToSector")     
    oDevice = Aliases.Mobile.Device 
    oApp = Aliases.Mobile.Device.App
    
    btnLogCopyingMusic = oApp.Find("ViewID", "dashboard_item_log_copying_printed_music" , 10)
    btnCheckPermission = oApp.Find("ViewID", "dashboard_item_check_permissions" , 10)  
    btnListPublications = oApp.Find("ViewID", "dashboard_item_list_publications" , 10)
    btnLogCopying = oApp.Find("ViewID", "dashboard_item_log_copying_printed_publications" , 10)

    Delay(1000)
    btnMenu = oApp.Find("ViewID", "drawer_button" , 10)
    btnMenu.Touch()
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite" , 10).getText().toString()
    Log.Message(txtLicence)
    oDevice.PressBack()
    
    if txtLicence == "Schools":
        if btnLogCopyingMusic.Exists:
            Log.Message("Pass. Log Copying Music is shown")
        else:
            Log.Warning("Fail. Log Copying Music is not shown")
    else:
        if btnLogCopyingMusic.Exists:
            Log.Warning("Fail. Log Copying Music is not shown")
        else:
            Log.Message("Pass. Log Copying Music is shown")

		  
    if btnCheckPermission.Exists:
        Log.Message("Pass. Check Permission is shown")
    else:
        Log.Warning("Fail. Check Permission is not shown")
	
	   
    if btnLogCopying.Exists:
        Log.Message("Pass. Log Copying is shown")
    else:
        Log.Warning("Fail. Log Copying is not shown")

	   
    if btnListPublications.Exists:
        Log.Message("Pass. List Publications is shown")
    else:
        Log.Warning("Fail. List Publications is not shown")
	   
    Delay(500)

	   
    Log.PopLogFolder()
    
