from Read_Test_Data_From_Excel import *
from Registration import *

def SideMenu():
    Log.AppendFolder("SideMenu")
    oApp = Aliases.Mobile.Device.App
    oDevice = Aliases.Mobile.Device
    
    btnMenu = oApp.Find("ViewID", "drawer_button" , 10)
    btnMenu.Touch()
    Delay(400)
    
    btnChangeSector = oApp.Find("ViewID", "btn_change" , 20)
    btnAboutUs = oApp.Find("ViewID", "btn_about_us" , 20)
    btnHelp = oApp.Find("ViewID", "btn_help" , 20)
    
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite" , 10).getText().toString()
    txtOrganisation = oApp.Find("ViewID", "txt_your_organisation_value" , 10).getText().toString()
    txtPostcode = oApp.Find("ViewID", "txt_your_postcode_value" , 10).getText().toString()
    txtEmail = oApp.Find("ViewID", "txt_your_email_address_value" , 10).getText().toString()
    
    
    # Check 'About us'
    btnAboutUs.Touch()
    Delay(500)
    text = oApp.Find("ViewID", "txt_title" , 10)
    btnBack = oApp.Find("ViewID", "back_button" , 20)
    
    if text.getText().toString() == "About CLA":
        Log.Message("'About us' screen is displayed")
    btnBack.Touch()
    Delay(500)
  
    
    # Check 'Contact'
    btnContact = oApp.Find("ViewID", "btn_contact" , 20)
    if not btnContact.Exists:
         Log.Message("Yes")
         btnMenu.Touch()
    
    btnContact.Touch()
    Delay(500)
    text = oApp.Layout("NO_ID").Layout("action_bar_root").Layout("content").View("drawer_layout").Layout("NO_ID").ScrollView("NO_ID").TextView("NO_ID", 8)
    
    if text.getText().toString() == "cla@cla.co.uk":
        Log.Message("'Contact' screen is displayed")
    btnBack.Touch()
    Delay(200)
	
    
    # Check 'Help'
    oDevice.Move(27, 27)
    if not btnHelp.Exists:
         btnMenu.Touch()

    btnHelp.Touch()
    Delay(200)
    
    text = oApp.Find("ViewID", "help_text" , 20)
	
    if text.getText().toString() == "*mobileroyalties*":
        Log.Message("'Help' screen is displayed")
    btnBack.Touch()
	   


    # Check 'Your details' which were set during registration
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Side_Menu", 1)
	
    Delay(200)
    if txtOrganisation == newMap['name'] and txtPostcode == newMap['postcode'] and txtEmail == ewMap['email']:
        Log.message("User details which were set durring registration are displayed")
    else:
        Log.Warning("User details which were set durring registration are not mached") 
	
	  
    # Change 'Your details' - same Test cases as durring registration
    btnChangeYourDetails = oApp.Find("ViewID", "btn_change_details" , 20)
    Delay(200)
    if not btnChangeYourDetails.Exists:
         btnMenu.Touch()
	    
    btnChangeYourDetails.Touch()
    Registration("Side_Menu", 1)
    Registration("Side_Menu", 2)
    Registration("Side_Menu", 3)    
    Registration("Side_Menu", 4)
    Registration("Side_Menu", 5)
    Registration("Side_Menu", 6)
  
    
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Side_Menu", 7)
    
    # Log.Message(newMap['tc_name'])
    btnMenu.Touch()
    Delay(500)
    if txtOrganisation == newMap['name'] and txtPostcode == newMap['postcode'] and txtEmail == newMap['email']:
       Log.message("User details were changed successful")
    else:
        Log.Warning("User details were not changed successful") 
	
    oDevice.PressBack()
	  
    Log.PopLogFolder()
	