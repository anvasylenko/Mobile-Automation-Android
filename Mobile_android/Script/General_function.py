from Read_Test_Data_From_Excel import *

def restart():
    Mobile.SetCurrent("emulator-5554")
#    TestedApps.CLA.Run()
    Delay(500)
    oApp = Aliases.Mobile.Device.App
    oApp.Restart()
    
def TC_SkipRegisrtration():
    Log.AppendFolder("TC_SkipRegisrtration")
    oApp = Aliases.Mobile.Device.App
#    oApp.sreenChooseLicenceType.Drag(5,5, 0, 500)
#    oApp.sreenChooseLicenceType.Drag(5,5, 0, 500)
#    oApp.sreenChooseLicenceType.Drag(67, 304, 224, 1)
#    oApp.sreenChooseLicenceType.Drag(67, 304, 224, 1)
   
    Delay(500)
    oApp.btnSkipContinue.Touch()
    Log.PopLogFolder()

    
def TC_RestartOnRePage():
    Log.AppendFolder("TC_RestartOnRePage") 
    restart()
    oApp = Aliases.Mobile.Device.App
	
     #This functionality does not work as expacted -> bug 
    if oApp.sreenChooseLicenceType.Exists:
        Log.Message("App continues from Registration screen")
    else:
        Log.Warning("App continues from OTHER screen")
	   
    Log.PopLogFolder()
    
    

def TakePhoto(whatPage):   # values: "first_page" and "ideftifier_page"
     
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
    
    btnTakePhotoFirstPage = oApp.Find("ViewID", "btn_take_photo_first" , 20)
    btnTakePhotoFirstImg = oApp.Find("ViewID", "btn_take_photo_first_img" , 20)
    
    btnTakePhotoIdentPage = oApp.Find("ViewID", "btn_take_photo" , 20)
    btnTakePhotoImg = oApp.Find("ViewID", "btn_take_photo_img" , 20)
    
    if whatPage == "first_page":
        btnTakePhotoFirstPage.Touch()
       # Take a photo of first page
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(1000)
	   
    elif whatPage == "ideftifier_page":
        btnTakePhotoIdentPage.Touch()
        #Take a photo
        ImageRepository.camera.ImageView_UnnamedCtrl.Touch(61, 76)
        ImageRepository.camera.ImageView_UnnamedCtrl1.Touch(43, 77)
        Delay(1000)
	
	   
def LogCopying(nameSheet, TestCaseNumber):
     
    oDevice = Aliases.Mobile.Device
    oApp = Aliases.Mobile.Device.App
     
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel(nameSheet, TestCaseNumber)

    oISBN = oApp.Find("ViewID", "txt_isbn_title" , 10)
    oUsage = oApp.Find("ViewID", "spinner_usage" , 10)
    oNumCopies = oApp.Find("ViewID", "txt_copies_made" , 10)
    oFrom1 = oApp.Find("ViewID", "txt_from" , 20)
    oTo1 = oApp.Find("ViewID", "txt_to" , 20)
    btnAddpageRange = oApp.Find("ViewID", "btn_add_page_range" , 10)
    oPageRange = oApp.Find("ViewID", "container_page_range" , 10)
    ISBN = oApp.Find("ViewID", "txt_isbn_title" , 10)


#    #Check ISBN
#    if newMap['search'] == "":
#        if ISBN.getText().toString() == "0000000000":
#            Log.Message("ISBN = 0000000000 as expected")
#        else:
#            Log.Warning("ISBN not equal 0000000000 as expected")
#    else:
#        if ISBN.getText().toString() == newMap['isbn']:
#            Log.Message ("ISBN is correct")
#        else:
#            Log.Warning("ISBN is NOT correct")


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
    Delay(1000)
    
    if int(newMap['tc_fail_log']) == 1:
        oUsage = oApp.Find("ViewID", "spinner_usage" , 10)
        if oUsage.Exists:
            Log.Message("PASS. Test failed as expected")
            Delay(500)
            oDevice.PressBack()
            oDevice.PressBack()
            txtSearch = oApp.Find("ViewID", "txt_search" , 20)
            if txtSearch.Exists:
                oDevice.PressBack()
        else:
            Log.Warning("Log Test did not failed as expected")
    else:
        oMessageScreen = oApp.Find("ViewID", "data_submitted", 20)
        if oMessageScreen.Exists:
            Log.Message(oMessageScreen)
            btnLogAnoterTitle = oApp.Find("ViewID", "btn_finish_button", 20)
            btnLogAnoterTitle.Touch()	   
            Delay(1000)
        else:
            Log.Warning("Successful Message does not appared")

        
