def SideMenu():
    Log.AppendFolder("Settings")
    oApp = Aliases.Mobile.Device.App
    
    btnMenu = oApp.Find("ViewID", "drawer_button" , 10)
    btnChangeSector = oApp.Find("ViewID", "btn_change" , 10)
    btnChangeYourDetails = oApp.Find("ViewID", "btn_change_details" , 10)
    btnAboutUs = oApp.Find("ViewID", "btn_about_us" , 10)
    btnContact = oApp.Find("ViewID", "btn_contact" , 10)
    btnHelp = oApp.Find("ViewID", "btn_help" , 10)
    
    txtLicence = oApp.Find("ViewID", "txt_your_licence_subtite" , 10).getText().toString()
    txtOrganisation = oApp.Find("ViewID", "txt_your_organisation_value" , 10).getText().toString()
    txtPostcode = oApp.Find("ViewID", "txt_your_postcode_value" , 10).getText().toString()
    txtEmail = oApp.Find("ViewID", "txt_your_email_address_value" , 10).getText().toString()
    
    btnMenu.Touch()
    
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
	
    
    # Check Sector
    if txtLicence == "School":
        Log.message("Sector which was set durring registration is displayed")
    
    btnChangeSector.Touch()
    
    btnMenu.Touch()
    Delay(200)
    
    if txtLicence == "School":
        Log.message("Sector is changed")
	   
    # Check 'Your details'
    if txtOrganisation == "TestSectorgalaxy" and txtPostcode == "NE15 7GT" and txtEmail == "TestSectorgalaxy@cla.co.uk":
       Log.message("User details which were set durring registration are displayed")
	
	  
    btnChangeYourDetails.Touch()
    
    # -> to separate function
    oRegPage.EditText("txt_org_name").Keys("NewTestSectorgalaxy")
    oRegPage.EditText("txt_postcode").Keys("SE15 7GT")
    oRegPage.EditText("txt_email").Keys("NewSectorgalaxy@cla.co.uk")
    oApp.btnSkipContinue.Touch()
    Delay(100)
    
    btnMenu.Touch()
    Delay(200)
    
    if txtOrganisation == "TestSectorgalaxy" and txtPostcode == "NE15 7GT" and txtEmail == "TestSectorgalaxy@cla.co.uk":
       Log.message("User details are changed")
	  
    Log.PopLogFolder()
	