﻿from Install_App import *
from General_functions import *
from Check_permissions_tests import *
from List_publications_tests import *
from Log_copying_music_tests import *
from Registration_tests import *
from Log_copying_publications_tests import *
from Side_menu_tests import *
from Select_Sector import *


def main():
    before()
    viewTutorial()
    
    RegistrationAllTests()
    CheckOptionsToSector()
    SelectSector(1, "other")
    
    SideMenu()
    restart()
    
    checkPermissionTestAllCases()
    LogCopyingPublicationsAllTestCases()
    LogCopyingMusicAllTestCases()
    ListPublicationsAllTestCases()