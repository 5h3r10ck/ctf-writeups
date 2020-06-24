![Image](https://i.postimg.cc/nVP0J5mH/Screenshot-5.png)

This challenge is easy once you understand the concept of hop by hop HTTP headers.

There is two types of HTTP header:

    End-to-end headers, which must be transmitted to the ultimate recipient of a request or response. They are present in the request all the way through to the end of it.

    Hop-by-hop headers, which are meaningful only for a single transport-level connection. They are only processed by the present proxy handling the request. 

Back to our challenge, once we enter the website and go to the admin page, we get:

![Image2](https://i.postimg.cc/YqtCX8rM/Screenshot-6.png)

the website is filtering the ip addresses to only allow access to local users.
What we can do is use the X-Forwarded-For HTTP header (which store our ip address) as a Hop-By-Hop header so the backend app wont be able to process our IP.

We can do that by adding X-Forwarded-For to the Connection header wich makes sure our IP isnt being communicated by proxies over further connections.

![Image3](https://i.postimg.cc/CLMfZwfG/Screenshot-1.png)

You can read more about this here: [Link](https://nathandavison.com/blog/abusing-http-hop-by-hop-request-headers)
