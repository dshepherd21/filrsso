#!/usr/bin/python
# -*- coding: utf-8 -*-
import lib
import os
import Cookie
import cgi
import cgitb
import requests
form = cgi.FieldStorage()
import ConfigParser

webpath="/srv/www/cgi-bin"
try:
	user=form["user_name"].value
	password=form["password"].value
except:
	user=""
	password=""
passw=lib.encrypt_val(password)
config=ConfigParser.ConfigParser()
temp=config.read(webpath+"/auth.conf")
try:
	filrsrv=config.get("server","ip")
	hours=int(config.get("server","hours"))+1
except:
	print "No Filr Server Defined"
	sys.exit()
cgitb.enable(display=1, logdir="/srv/www/cgi-bin")
arguments = cgi.FieldStorage()
# create the cookie
c=Cookie.SimpleCookie()
d=Cookie.SimpleCookie()
# assign a value
c['fuser']=user
# set the xpires time
#c['fuser']['expires']=1*1*3*60*60
c['fuser']['expires']=1*1*hours*60*60
d['fpass']=passw.replace("=","\=")
#d['fpass']['expires']=1*1*3*60*60
d['fpass']['expires']=1*1*hours*60*60
print c
print d
print "Content-type: text/html\n"
print
print "Credentials Being Cached"
print "<html>"
print "<body>"
print "<form name=\"loginFormName\" id=\"loginFormId\" action=\"https://"+filrsrv+"/ssf/s/portalLogin\" method=\"post\">"
print "<input type=\"hidden\" size=\"20\" name=\"j_username\" value=\""+user+"\">"
print "<input type=\"hidden\" size=\"20\" name=\"j_password\" value=\""+password+"\">"
print "<input type=\"submit\" value=\"Submit\"/>"
print "</form>"
print "<SCRIPT LANGUAGE=JavaScript>document.forms[0].submit();</SCRIPT>"
#print password+" "+passw
print "</body>"
print "</html>"
	

