from Read_Test_Data_From_Excel import *
from Select_Sector import *


def Registration(nameSheet, TestCaseNumber):
     
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel(nameSheet, TestCaseNumber)
        
    Log.AppendFolder(VarToString(TestCaseNumber) + " - " + nameSheet  + " - " + (newMap['tc_name']))
    
    oApp = Aliases.Mobile.Device.App
    btnSave = oApp.btnSkipContinue
    oRegPage = Mobile.Device("*").Process("*").RootLayout("")
    oName = oApp.Find("ViewID", "txt_org_name" , 20)
    oPostcode = oApp.Find("ViewID", "txt_postcode" , 20)
    oEmail = oApp.Find("ViewID", "txt_email", 20)
    
    
    
    # Clear data before test
    oName.Keys("^a")
    oName.Keys("[BS]")
    oPostcode.Keys("^a")
    oPostcode.Keys("[BS]")
    oEmail.Keys("^a")
    oEmail.Keys("[BS]")
	    
    # test
    oName.Keys(newMap['name'])
    oPostcode.Keys(newMap['postcode'])
    oEmail.Keys(newMap['email'])
    btnSave.Touch()
    Delay(1000)

    
    if newMap['warning_message'] != "pass":
        oWarning = Aliases.Device.App.Find("ViewID", "lbl_validation", 40)
        oWarningMess = oWarning.getText().toString()
        Log.Message(oWarningMess)
        if oWarningMess == newMap['warning_message']:
            oApp.btnClose.Touch()
            Log.Checkpoint ("PASS. Warning message Shown")
        else:
            Log.Warning("Warning message WAS NOT Shown")
            oApp.btnClose.Touch()
    elif newMap['warning_message'] == "pass":
        if oApp.ScreenWhatToDo.btnCheckPermissions.Exists:
            Log.Checkpoint("User registrated successfully")
        else:
            Log.Warning("User DID NOT registrated")
	
    Delay(500)

    Log.PopLogFolder()
    

