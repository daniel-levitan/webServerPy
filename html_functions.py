from constants import *
from functions import *
from templates import *
from datetime import datetime

def parse_http_request(request):
   """
   Check if this is a valid HTML request
   The request must have 3 parts, for example:
   GET /somedir/page.html HTTP/1.1 (Method Path HTTP/Version)
   """
   try:
      request_array = request.split("\r\n")  # This split the whole request into lines
      request_line_array = request_array[0].split() #  This split the first line of the request into parts
      print(f"Received request for: {request_line_array[1]}") 

      if len(request_line_array) < 2:
        return False, None, None

      request_method = request_line_array[0]
      filepath = request_line_array[1]

      if request_method in HTTP_METHODS:
         return True, request_method, filepath

   except Exception as e:
      print(f"Error parsing request: {e}")
      print(f"Request: {request}")
      return False, None, None

   return False, None, None


def build_headers(status, headers):
    response = f"HTTP/1.1 {status}\r\n"
    response += '\r\n'.join(f"{k}: {v}" for k, v in headers.items())
    response += "\r\n\r\n"
    return response


def build_http_response(method, filepath):
    headers = {
        'Date': datetime.now().strftime("%a, %-d %b %Y %H:%M:%S"),
        'Server': 'Levi/1.0 (Mac)',
        'Content-Type': 'text/html'
    }
    
    if method == 'GET':
        content = getFile(filepath)
        if not content:
            return build_headers('404 Not Found', headers) + NOT_FOUND_TEMPLATE
        return build_headers('200 OK', headers) + content
    
    if method == 'HEAD':
        return build_headers('200 OK', headers)
        
    return build_headers('501 Not Implemented', headers) + NOT_IMPLEMENTED_TEMPLATE
   

def process_html_request(request):

   ok, method, filepath = parse_http_request(request)

   if ok:
      response = build_http_response(method, filepath[1:])
   else:
      response = build_http_response("", "")

   return response
