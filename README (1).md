# Webserv - A Lightweight HTTP/1.1 Server in C++  

[![Linux](https://img.shields.io/badge/Platform-Linux-blue.svg)](https://en.wikipedia.org/wiki/Linux)  
A non-blocking HTTP/1.1 server written in C++, inspired by NGINX.  

## 🚀 Introduction  
**Webserv** is a lightweight, event-driven HTTP server built using C++ and `epoll()`. It is designed to handle multiple requests efficiently while remaining non-blocking. It supports **GET, POST, and DELETE** methods and can execute Python scripts via CGI.  

## 👥 Contributors  
- [@Welhox](https://github.com/Welhox) – Developed and implemented full HTTP response handling, including the core functionalities of GET, POST, and DELETE methods on the server side.  
- [@tcampbel22](https://github.com/tcampbel22) – Configuration file parsing, Logger  
- [@codinggolfer](https://github.com/codinggolfer) – Request parsing  

### 🛠 Collaborative Work  
- CGI support & main server loop developed together  

## ✨ Features  
✅ **Non-blocking I/O** (using `epoll()`)  
✅ **CGI support** for executing Python scripts  
✅ **Custom error pages** at different levels: location block, server level, and default error handler  
✅ **Directory listing** with resource links  
✅ **Multiple server instances**  
✅ **Basic file upload support**  
✅ **Configuration-based setup** (similar to NGINX)  

## 🛠 Installation  

**Requirements:**  
- A Linux environment (due to `epoll()` usage)  
- `make` and `g++` are required to compile the project. If they are not installed, you can install them using:  
  ```sh
  sudo apt update && sudo apt install build-essential
  ```  

### 🔧 Build Instructions  
```sh
git clone https://github.com/your-repo/webserv.git
cd webserv
make
```

## ▶️ Usage  

To start the server, provide a configuration file:  
```sh
./webserv config/server.conf
```
**Default Address:** `127.0.0.1:8081`  

## ⚙️ Configuration  

Webserv reads configurations from a file (similar to NGINX). Example configuration files can be found in the `config/` directory.  

### Example `server.conf`:  
```nginx
server {
    host 127.0.0.1
    port 8081;
    server_name myserver;

    error_page 404 /errors/404.html;
    
    location / {
        root /root/var/html;
        index index.html;
        methods GET;
    }
    
    location /cgi-bin/ {
    	cgi_path /root/bin/cgi/;
    	cgi_script cgitester.py;
    }

}
```

## 📸 Examples  

### Custom 404 Error Page  
![404](https://github.com/user-attachments/assets/45b36325-2162-40e4-b890-5e463ff64b95)  

### Directory Listing  
![directory-listing](https://github.com/user-attachments/assets/63e2601c-079a-4ef0-9545-aafd4eece85b)  

### File Upload Support  
![File-upload](https://github.com/user-attachments/assets/183fd28f-aad0-40f8-9c6e-a3cc7fad411d)  

### Homepage  
![Homepage](https://github.com/user-attachments/assets/6bc92d3d-4dac-4da9-8593-1043c7c11e9e)  
