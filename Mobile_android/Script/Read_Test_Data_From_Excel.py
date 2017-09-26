def ReadTestDataFromExcel(sSheetName, testCaseNumber):
    
#    Log.AppendFolder("Listening parameters")
    
    projPath = Project.Path
    testDataPath = projPath + "Testing_Data.xlsx"
#    Log.Message(testDataPath)
    testCaseNumber = testCaseNumber + 1
    
    # Open Excel
    Excel = Sys.OleObject["Excel.Application"]
    
    # This is a call to the indexed property
    Sheet = Excel.Workbooks.open(testDataPath).Sheets.Item[sSheetName]
    
    parameterNameColunm = 1
    valueColumn = testCaseNumber  # = 2 
    iRow = 2
    
    mapParameters = {}
    
    while trim(VarToString(Sheet.Cells.Item[iRow, parameterNameColunm])) != "":
        rowValue = VarToString(Sheet.Cells.Item[iRow, parameterNameColunm])
        mapParameters[rowValue] = VarToString(Sheet.Cells.Item[iRow, valueColumn])
#        Log.Message(str(rowValue) + " : " + VarToString(Sheet.Cells.Item[iRow, valueColumn]))
        iRow = iRow + 1

#    Log.PopLogFolder()
    
    Excel.Quit()

    return mapParameters

