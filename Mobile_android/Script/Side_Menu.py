from Read_Test_Data_From_Excel import *
from Registration import *

def SideMenu():
    Log.AppendFolder("Settings")
    oApp = Aliases.Mobile.Device.App
    
    btnMenu = oApp.Find("ViewID", "drawer_button" , 10)
    btnMenu.Touch()
    
    btnChangeSector = oApp.Find("ViewID", "btn_change" , 10)
    btnChangeYourDetails = oApp.Find("ViewID", "btn_change_details" , 10)
    btnAboutUs = oApp.Find("ViewID", "btn_about_us" , 10)
    btnContact = oApp.Find("ViewID", "btn_contact" , 10)
    btnHelp = oApp.Find("ViewID", "btn_help" , 10)
    
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite" , 10).getText().toString()
    txtOrganisation = oApp.Find("ViewID", "txt_your_organisation_value" , 10).getText().toString()
    txtPostcode = oApp.Find("ViewID", "txt_your_postcode_value" , 10).getText().toString()
    txtEmail = oApp.Find("ViewID", "txt_your_email_address_value" , 10).getText().toString()
    
	# Check 'About us'
    btnAboutUs.Touch()
    Delay(200)
    text = oApp.Layout("NO_ID").Layout("action_bar_root").Layout("content").View("drawer_layout").Layout("NO_ID").Layout("NO_ID").TextView("NO_ID")
    btnBack = oApp.Find("ViewID", "back_button" , 20)
    text.Touch()
    
    if text.getText().toString() == "*CLA services*":
        Log.Message("'About us' screen is displayed")
    btnBack.Touch()
    
    # Check 'Contact'
    btnContact.Touch()
    Delay(200)
    text = oApp.Layout("NO_ID").Layout("action_bar_root").Layout("content").View("drawer_layout").Layout("NO_ID").ScrollView("NO_ID").TextView("NO_ID", 8)
    
    if text.getText().toString() == "cla@cla.co.uk":
        Log.Message("'Contact' screen is displayed")
    btnBack.Touch()
	
    # Check 'Help'
    btnHelp.Touch()
    Delay(200)
    
    text = oApp.Find("ViewID", "help_text" , 20)
	
    if text.getText().toString() == "*mobileroyalties*":
        Log.Message("'Help' screen is displayed")
    btnBack.Touch()
	   
    # Check 'Your details' which were set durring registration
    # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Side_Menu", 2)
	    
#    Log.Message(newMap['tc_name'])
#    btnBack.Touch()
#    btnMenu.Touch()
    Delay(200)
    if txtOrganisation == newMap['name'] and txtPostcode == newMap['postcode'] and txtEmail == ewMap['email']:
       Log.message("User details which were set durring registration are displayed")
	  
    # Change 'Your details' -. same Test cases as durring registration 
    btnChangeYourDetails.Touch()
    Registration("Side_Menu", 3)    
    Registration("Side_Menu", 4)
    Registration("Side_Menu", 5)
    Registration("Side_Menu", 6)
    Registration("Side_Menu", 7)
    Registration("Side_Menu", 8)
    
   # Get parameters
    newMap = {}
    newMap = ReadTestDataFromExcel("Side_Menu", 8)
    
#    Log.Message(newMap['tc_name'])
    btnMenu.Touch()
    Delay(200)
    if txtOrganisation == newMap['name'] and txtPostcode == newMap['postcode'] and txtEmail == ewMap['email']:
       Log.message("User details were changed successful")
	  
    Log.PopLogFolder()
	