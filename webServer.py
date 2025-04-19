from socket import *
from functions import *
from html_functions import *
from socketInterface import *
from constants import *

def main():
   server_socket = create_server_socket()
   if not server_socket:
      return

   num_of_connections = 0
   while True:
      connection_socket, addr = server_socket.accept()
      num_of_connections += 1
      print(f"Connection {num_of_connections} New connection from {addr}")         

      request = connection_socket.recv(1024).decode()
      response = process_html_request(request)
               
      if response:
         connection_socket.send(response.encode())
               
      connection_socket.close()

if __name__ == '__main__':
   main()