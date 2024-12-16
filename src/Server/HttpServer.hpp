/**********************************************************************************/
/** __          __  _                                                            **/
/** \ \        / / | |                                by:                        **/
/**  \ \  /\  / /__| |__  ___  ___ _ ____   __                                   **/
/**   \ \/  \/ / _ \ '_ \/ __|/ _ \ '__\ \ / /        Eromon Agbomeirele         **/
/**    \  /\  /  __/ |_) \__ \  __/ |   \ V /         Casimir Lundberg           **/
/**     \/  \/ \___|_.__/|___/\___|_|    \_/          Tim Campbell               **/
/**                                                                              **/
/**                                                                              **/
/**                                W E B S E R V                                 **/
/**********************************************************************************/

#pragma once
# include <string>
# include <sys/socket.h>
# include <iostream>
# include <stdlib.h>
# include <unistd.h>
# include <netinet/in.h>
# include <sstream>
# include <arpa/inet.h>
# include <vector>
# include <sys/epoll.h>
# include <fcntl.h>
# include <sys/sendfile.h>
# include "../HttpParsing/HttpParser.hpp"
# include "../Config/ServerSettings.hpp"
#include <errno.h>
#include <string.h>
#include "../Response/Response.hpp"
#include <memory>
#include "../Response/ServerHandler.hpp"
#include <csignal>

# define MAX_EVENTS 20 //Can define this in config file or create a funct based on cpu load or leave it
# define TIME_OUT_PERIOD 100

struct fdNode
{
	int				fd;
	ServerSettings *serverPtr = nullptr;
	std::vector<char> _clientDataBuffer;
	bool			_connection = true;
};

class HttpServer
{
private:
	static HttpServer *_instance;
	std::vector<std::pair<std::string, int>> _ip_port_list;
	std::vector<int> _server_fds;
	std::vector<fdNode*> server_nodes;
	std::map<int, fdNode*> client_nodes;
	int 			_clientSocket;
	sockaddr_in 	_socketInfo; //reusable
	int				epollFd;
	epoll_event		_events;
	epoll_event		_eventsArr[MAX_EVENTS];
	int				numEvents;
	std::unordered_map<int, time_t> _fd_activity_map;
	
public:
	std::vector<ServerSettings> settings_vec;
	//constructors & destructors
	HttpServer(std::vector<ServerSettings>& vec);
	~HttpServer();
	
	//methods
	static void signalHandler(int signal);
	void	fdActivityLoop(const time_t);
	bool	isRequestComplete(const std::vector<char>& data, ssize_t bytesReceived);
	bool	isChunkedTransferEncoding(const std::string& requestStr);
	bool	isRequestWithBody(std::string requestStr);
	size_t	getContentLength(const std::string& requestStr);
	void	startServer();
	void	closeServer();
	void	startListening();
	void	acceptNewClient(fdNode* nodePtr, int eventFd, time_t current_time);
	void	addServerToEpoll();
	void	fillHostPortPairs();
};
