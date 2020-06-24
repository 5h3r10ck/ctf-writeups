# Game modding from nullcon HackIM 2020 CTF

Yesterday I played Nullcon ctf which had a category by the name: Zelda Adventure .In this category, we needed to download a [unity game](https://drive.google.com/file/d/1W_KJhSn6wTQiUYBNY5xhmbseJXC0l2Up) :

![game flag1](https://i.imgur.com/eIyj20X.png)

And we are asked to complete couple of tasks:
- Killing one NPC
- Crossing a pont
- Getting to the end of the jungle
- Didnt have time to check the last task

To solve this, I used dnSpy which is a .NET debugger and assembly editor, you just need to open Assembly-CSharp with dnSpy and start modding(If you are interested in this stuff [Guided Hacking](https://www.youtube.com/user/L4DL4D2EUROPE) is your friend)
Here is how it looks like:
![](https://i.imgur.com/fodlkU4.png)

To kill NPC you need to buff your damage in the TakeDamage method, just multiply by 99999 or whatever:
![](https://i.imgur.com/pbEGfjZ.png)

For the second and third task, I multiplied my speed by 5 and multiplied the camera max position. Now you can sprint all over the map and pass obstacles without a problem:
![](https://i.imgur.com/2ebWLjD.png)

![](https://i.imgur.com/XV1iugn.png)

The flags looks like this: 

![](https://i.imgur.com/Y8LQoTI.png)
