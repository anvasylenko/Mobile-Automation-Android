from Read_Test_Data_From_Excel import *
from Select_Sector import *

def Registration(nameSheet, TestCaseNumber):
    Log.AppendFolder("Registration")
    
    oApp = Aliases.Mobile.Device.App
    btnSave = oApp.btnSkipContinue
    oRegPage = Mobile.Device("*").Process("*").RootLayout("")
    oName = oApp.Find("ViewID", "txt_org_name" , 20)
    oPostcode = oApp.Find("ViewID", "txt_postcode" , 20)
    oEmail = oApp.Find("ViewID", "txt_email" , 20)
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel(nameSheet, TestCaseNumber)
    
    # Clear data before test
#    if newMap['warning_message'] != "pass":
    oName.Keys("^a")
    oName.Keys("[BS]")
    oPostcode.Keys("^a")
    oPostcode.Keys("[BS]")
    oEmail.Keys("^a")
    oEmail.Keys("[BS]")
	    
    # test
#    Log.Message(newMap['tc_name'])
    oName.Keys(newMap['name'])
    oPostcode.Keys(newMap['postcode'])
    oEmail.Keys(newMap['email'])
    btnSave.Touch()
    Delay(1000)

    
    if newMap['warning_message'] != "pass":
        oWarningMess = Aliases.Device.App.ScreenWhatToDo.btnLogCopying.TextView("lbl_validation").getText().toString()
        Log.Message(oWarningMess)
        if oWarningMess == newMap['warning_message']:
            oApp.btnClose.Touch()
            Log.Message ("PASS. Warning message Shown for")
        else:
            Log.Message("Warning message WAS NOT Shown")
            oApp.btnClose.Touch()
    elif newMap['warning_message'] == "pass":
        if oApp.ScreenWhatToDo.btnCheckPermissions.Exists:
            Log.Message("User registrated successfully")
        else:
            Log.Warning("User DID NOT registrated")
	
    Delay(500)

    Log.PopLogFolder()
    

def RegistrationAllTests():
#    SelectSector(0, "Schools")
    Registration("Registration", 2)
    Registration("Registration", 3)
    Registration("Registration", 4)
    Registration("Registration", 5)
    Registration("Registration", 6)
    Registration("Registration", 7)  
    
def RegPass():
    Registration("Registration", 7)    
