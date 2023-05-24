# Given the client ID and tenant ID for an app registered in Azure,
# provide an Azure AD access token and a refresh token.

# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.
#
# The demo may be extended to use the 

#
# The samle uses public profile, and require a browser logon
# ConfidentialClientApplication API

# pip install msal
# Python 3.x
#
#  (c) Inge Os, Oracle Norway 3/2-2023
#
from msal import PublicClientApplication
import sys
import os
import json
import argparse
import platform

# Default values

client_id = None
tenant_id = None
scopes = None

#
# Retrieve CMD line arguments
#
if platform.system().lower() == 'linux':
	configFile="/home/oracle/azuread-demo/config.json"
else:
	configFile="azadconfig.json"

argsParser=argparse.ArgumentParser(description='Azure Ad token generation 1.0')
argsParser.add_argument("--configfile",default=configFile,type=str,help="Site Config File")
argsParser.add_argument("--tokenfile",default="azadtoken",type=str,help="Resultfile where token are stored, .token and .refresh")
args=argsParser.parse_args()

#
# Load configuration
#
with open(args.configfile) as f:
	configText = f.read()
try:
	cfg=json.loads(configText)
except (Exception, ValueError) as ex:
	print('invalid configuration in configfile: ' + str(ex))
	exit(1)
#

#
# Verify configuration parameters
parameters=['client_id','tenant_id','scopes']
for parameterName in parameters:
	if parameterName not in cfg:
		print('Required parameter '+parameterName+' is missing from config file')
		exit(1)
client_id=cfg['client_id']
tenant_id=cfg['tenant_id']
scopes=cfg['scopes']
app = PublicClientApplication(
	client_id = client_id,
	authority = "https://login.microsoftonline.com/" +tenant_id
)

print('Logging on with the following')
print('Client id: '+client_id)
print('Tenant ID '+tenant_id)
print('Scope: '+scopes[0])

acquire_tokens_result = app.acquire_token_interactive(
	scopes = scopes
)

if 'error' in acquire_tokens_result:
	print("Error: " + acquire_tokens_result['error'])
	print("Description: " + acquire_tokens_result['error_description'])
else:
	print("Access token:\n")
	print(acquire_tokens_result['access_token'])
	with open(args.tokenfile+'.jwt', 'w') as f:
		f.write(acquire_tokens_result['access_token'])
	print("\nRefresh token:\n")
	print(acquire_tokens_result['refresh_token'])
	with open(args.tokenfile+'.rjwt', 'w') as f:
		f.write(acquire_tokens_result['refresh_token'])