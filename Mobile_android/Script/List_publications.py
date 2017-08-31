def ListPublicutoions():
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    btnListPublications = oApp.Find("ViewID", "dashboard_item_list_publications" , 10)
    
    btnListPublications.Touch()
    
    btnContinue = oApp.Find("ViewID", "btn_continue" , 20)
    oApp.ScreenWhatToDo.txtSearch.Keys("some")
    btnContinue.Touch()
    
    btnSaveContinue = oApp.Find("ViewID", "btn_save_continue" , 20)
    btnFinishSend = oApp.Find("ViewID", "btn_finish_send" , 20)
    
    btnSaveContinue.Tuoch()
    oApp.ScreenWhatToDo.txtSearch.Keys("some")
    btnContinue.Touch()
    
    btnFinishSend.Touch()
    btnNo = oApp.Find("ViewID", "no_button" , 20)
    
    btnFinishSend.Touch()
    btnYes = oApp.Find("ViewID", "yes_button" , 20)
    
    popUp = oApp.ScreenWhatToDo.screenThankyou
    
    if popUp.Exists:
        btnBack = oApp.Find("ViewID", "btn_finish_button" , 20)
        btnBack.Touch()
    
#    Log.Message("Done")
    
#    if btnContinue.Exists:
#        Log.Message("Done")