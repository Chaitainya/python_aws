# if any error like module not found install pip install pypiwin32 # if any error occurs while installing pypiwin32 run this command: python -m pip install --user --upgrade pip
import win32api
import os

userinput = win32api.MessageBox(0, 'Successfully uploaded to s3 bucket. Would you like to deploy?', 'S3 Upload status', 0x00000004)
print(userinput)
# os.system('dir')
if userinput == 6:
    win32api.MessageBox(0, 'Deployment started', 'Deploment status')
