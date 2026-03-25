#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/socket.h>

#include <netinet/in.h>

int main () {

        // Create a socket
        int networkSocket;
        networkSocket = socket(AF_INET, SOCK_STREAM, 0);

        // spedify an address for the socket
        struct sockaddr_in serverAddress;
        serverAddress.sin_family = AF_INET;
        serverAddress.sin_port = htons()
        

        return 0;
}