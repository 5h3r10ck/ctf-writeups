# FILESTORAGE

Once we enter the web app we are asked to enter a username, the request is bellow

![](https://i.ibb.co/K20XLVt/first1.png)
![](https://i.ibb.co/cLV6Yrc/req.png)

Capturing the request with burp, we see that the app takes the value entered as a param and then assign us a PHPSESSID. 
After we enter the name, we get this page with a couple of files we can read.

![](https://i.ibb.co/svhRsfp/page.png)


It uses a file param to a access the files.

![](https://i.ibb.co/0sTXPh2/bee.png)


The first thing we tested was LFI, and the test was positive.So now we can exploit this to read files from the system. But the problem is we dont know where the flag is.

![](https://i.ibb.co/41BpLMq/lfi.png)


So instead of blindly looking for the flag using LFI. We are going to use that PHPSESSID from the login form to try and escalate LFI to RCE. To do this, we gonna set the "name" param to an arbitary php code and gets it executed(after abit of research,we found that the server stores PHPSESSID in files in /tmp/sess_OURPHPSESSID).


The final exploit looks something like this:
log in with something like ```<?php system("ls -al /");?>```
and save the PHPSESSID assigned, then check the path ``` ../../../../../../../../../../tmp/sess_URPHPSESSID```

![](https://i.ibb.co/sqts0Ds/burp.png)


To get the flag, sign in with ```<?php system(cat /flag_is_here/flag.txt);?>```

![](https://i.ibb.co/B3B5G6C/FLAG.png)
