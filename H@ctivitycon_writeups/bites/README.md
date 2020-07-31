# bites
![desc](https://i.ibb.co/Z6mbRcQ/bite0.png)

In this challenge we are give a link to a webapp. The only intersting thing we could find is the page parameter wich end up being vulnerable to LFI. the param takes any strings append .php and tries to read it.

Upon playing with the param for abit we found out the location of the flag.
![test](https://i.ibb.co/RNbD4nB/bite-test.png)
![flagloc](https://i.ibb.co/RNLYHL5/bite-flagloc.png)

Trying to give /flag.txt as a param end up as trying to read /flag.txt.php to bypass this we used null byte.

![flag](https://i.ibb.co/MsYCrWK/Screenshot-9.png)
