#Webserv, a HTTP1.1 server made in C++

made by [@Welhox](https://github.com/Welhox) , [@tcampbel22](https://github.com/tcampbel22) and [@codinggolfer](https://github.com/codinggolfer)

The server uses NGINX as reference.
It is non blocking, and is able to execute Python scripts using CGI.
It includes directory listing.
Support for different levels of error pages. Location block level, Server level and in the end default error generator.
Can launch and handle multiple servers.
Handles default pages and directory listing including links to resources per location block.



To compile it, do make in root folder.
Due to the use of epoll(), it sadly runs only on linux.

To run it, launch it with a configuration file from the config folder as argument. 
./webserv config/server.conf

default adress is 127.0.0.1:8081.

Works with GET, POST and DELETE.


We split up the project so that I did the responses, Tim the config file parsing, and logger, and Eromon did the request parsing.
We did the CGI and main server loop together. I got to immerse myself in the world of RFC in order to understand the structure of responses correctly. 
I created also did the GET/DELETE/POST functionalities on server level. 


