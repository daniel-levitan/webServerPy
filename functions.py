import os.path

def getFile(filepath):
   response = ""

   if os.path.isfile(filepath):
      with open(filepath, 'r') as file:
         response = file.read()      
   
   return response
