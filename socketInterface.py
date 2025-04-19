from socket import *
from constants import *
from html_functions import *

def create_server_socket(port=SERVER_PORT):
    """
    Create, bind and configure a server socket
    Returns the socket on success or None on failure
    """
    try:
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
        server_socket.bind(('', port))
        server_socket.listen(1)
        print(f"Server socket created and listening on port {port}")
        return server_socket
        
    except OSError as e:
        print(f"Socket error: {e}")
        # Specific error handling
        if e.errno == 98:  # Address already in use
            print("Port is already in use")
        elif e.errno == 13:  # Permission denied
            print("Permission denied when binding to port")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def handle_client_connection(connection_socket, addr, num_of_connections):

    try: 
        print(f"Connection {num_of_connections}\
                New connection from {addr}")   
        # connection_socket.settimeout(CONN_TIMEOUT)
        request = connection_socket.recv(1024).decode()
        
        response = process_html_request(request)
        
        if response:
            connection_socket.send(response.encode())
        
        connection_socket.close()
        return True
    
    except Exception as e:
        print(f"Error handling client: {e}")
        connection_socket.close()
        return False