# if any error like module not found install pip install pypiwin32 # if any error occurs while installing pypiwin32 run this command: python -m pip install --user --upgrade pip
import win32api
import os

userinput = win32api.MessageBox(0, 'Successfully uploaded to s3 bucket. Would you like to deploy?', 'S3 Upload status', 0x00000004)
print(userinput)
# os.system('dir')
if userinput == 6:
    win32api.MessageBox(0, 'Successfully deployed.', 'Deploment status')

#########################################################################

# if any error like module not found install pip install pypiwin32 # if any error occurs while installing pypiwin32 run this command: python -m pip install --user --upgrade pip
import win32api
import os
import pywin.mfc.dialog

userinput = win32api.MessageBox(0, 'Successfully uploaded to s3 bucket. Would you like to deploy?', 'S3 Upload status', 0x00000004)
print(userinput)
# os.system('dir')
if userinput == 6:
    reason = pywin.mfc.dialog.GetSimpleInput("Why are you deploying?")
    if reason != None:
        os.system("ssh -l user -p port number ipaddress build jobname -s -v -p REASON='" + reason + "'")
        win32api.MessageBox(0, 'Successfully deployed.', 'Deploment status')

        
#########################################################################

# if any error like module not found install pip install pypiwin32 # if any error occurs while installing pypiwin32 run this command: python -m pip install --user --upgrade pip
import win32api, os, pywin.mfc.dialog, sys

environment = sys.argv[1]

userinput = win32api.MessageBox(0, 'Successfully uploaded to s3 bucket. Would you like to deploy?', 'S3 Upload status', 0x00000004)
print(userinput)

if userinput == 6:
    reason = pywin.mfc.dialog.GetSimpleInput("Why are you deploying?")
    if reason != None:
        if environment == "QA":
            os.system("ssh -l user -p port number ipaddress build jobname" + environment + "' -s -v -p REASON='" + reason + "'")
        elif environment == "STAGE":
            os.system("ssh -l user -p port number ipaddress build jobname" + environment + "' -s -v -p REASON='" + reason + "'")
        elif environment == "PROD":
            os.system("ssh -l user -p port number ipaddress build jobname" + environment + "' -s -v -p REASON='" + reason + "'")
        win32api.MessageBox(0, 'Successfully deployed.', 'Deployment status')
    else:
        win32api.MessageBox(0, 'Without a valid reason you can never deploy.', 'Deploment status')
