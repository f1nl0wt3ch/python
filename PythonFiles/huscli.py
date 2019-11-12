import urllib
intro="""
:::::::::::::::::::::::::::::::::::::::::
:::::: Welcome to HUS COMMAND TOOL ::::::
:::::: Author - Dinh Duc Thinh ::::::::::
:::::: Created date - 13.05.2019 ::::::::
::::: Email - thinh.dinh@bisnode.com ::::
:::::::::::::::::::::::::::::::::::::::::
"""
TARGET_URI='/Users/dinhthinh/Documents/JunoSpace/installer_project/hus-css/'
TARGET_FILE='com/sn4mobile/meo/hus_css/servlet/HusIndexServlet.java'

# Edit HusIndexServlet
def editHusIndex(target_uri, target_file):
    data = urllib.request.urlopen(urllib.parse(target_uri+target_file))
    for line in data:
        if 'case' in line:
            print(line)
        else:
            continue
print(intro)
editHusIndex(TARGET_URI, TARGET_FILE)
