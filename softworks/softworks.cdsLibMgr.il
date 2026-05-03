printf("  Adding Softworks Menu\n")

lmgrCreateMenuItem( "StartVsCode" "simple"
   '(("label" "Start VS Code" )
     ("callback" ("SdmVsCodeStartLmgrCB")) ))

lmgrCreateMenuItem( "ImportDocAsView" "simple"
   '(("label" "Import Document as Cell View")
     ("callback" ("SdmCreateViewFromFileGUI")) ))

lmgrCreateMenu("SoftworksMenu" '(("label" "Softworks")))
lmgrInsertMenuItems("VirtueHelpMenu" "" '("StartVsCode" "ImportDocAsView"))

printf("  Done adding softworks menu\n")
