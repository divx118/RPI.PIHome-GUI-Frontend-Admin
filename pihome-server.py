#!/usr/bin/env python

# PiHome v1.0
# http://pihome.harkemedia.de/
# 
# PiHome Copyright 2012, Sebastian Harke
# Lizenz Informationen.
# 
# This work is licensed under the Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Unported License. To view a copy of this license,
# visit: http://creativecommons.org/licenses/by-nc-sa/3.0/.


import time
import RPi.GPIO as GPIO
import os
import cgi,time,string,datetime,re
from os import curdir, sep, path
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
        	self.send_response(200)
        	self.send_header('Content-type', 'text/html')
        	self.end_headers()
        	datastring = str(self.path).split("request/")[1].split("/")
                print(datastring)
                # Check the received string
                if bool(re.match("^[a-d]$", string.lower(datastring[0]), flags = 0)):
                  letter = ord(string.lower(datastring[0])) - 97
                  print ("letter ",letter)
                  if bool(re.match("^(on)$", string.lower(datastring[1]), flags = 0)):
        	    status = 1
                  elif bool(re.match("^(off)$", string.lower(datastring[1]), flags = 0)):
                    status = 0
        	  if bool(re.match("^([0-1]{5})$",datastring[2],flags = 0)):
                    print ("hello ",datastring[2])
                    os.system("/home/div/rcswitch-pi/send " + datastring[2] + " " + str(letter) + " " + str(status))
                    print(datastring[2] + " " + str(letter) + " " + "1")                
                  return      
	except IOError:
		self.send_error(404,'File Not Found: ' + self.path)



def main():
    try:
        srv = HTTPServer(('', 8888), Handler)
        print 'START PiHome SERVER'
        srv.serve_forever()
    except KeyboardInterrupt:
        print ' STOP PiHome SERVER'
        srv.socket.close()


if __name__ == '__main__':
  main()

