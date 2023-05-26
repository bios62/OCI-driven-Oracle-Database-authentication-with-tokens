# OCI-driven-Oracle-Database-authentication-with-tokens
This is a repository for two different token based authentication to Oracle 19C database. Yo can integrate database authentication into OCI IAM Domain or Azure AD
it is a common securty desire not to managed users, especially priviledged users directly in the databases, bt have a central management from either OCI IAM Domain or AzureAd. 
By permitting token only authenticstion, the management of local DBAs are offloaded to external IAM soruces like OCI IAM.

For OCI the token is most easily created with the OCI CLI: <BR>
  oci iam db-token get --profile pelle<BR>
Private key written at /home/oracle/.oci/db-token/oci_db_key.pem<BR><BR>
  
![image](https://github.com/bios62/OCI-driven-Oracle-Database-authentication-with-tokens/assets/23355458/30641e28-53e4-4976-af51-0daf59ddb0f8)

The repo consist of:<BR>
[Description of how to configure OCI IAM Domain token based Database athentication](https://github.com/bios62/OCI-driven-Oracle-Database-authentication-with-tokens/blob/main/ociiam_oracleDB.pdf))
[Description of how to configure AzureAZ for db token](https://github.com/bios62/OCI-driven-Oracle-Database-authentication-with-tokens/blob/main/db_authentication.pdf)

[Python scipt for retrieving AzureAD JWT token](https://github.com/bios62/OCI-driven-Oracle-Database-authentication-with-tokens/blob/main/getazadtokenV3.py)

