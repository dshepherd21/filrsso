#!/usr/bin/env python
import os
import Cookie
import cgi
import cgitb
import requests
import ConfigParser
import lib

webpath="/srv/www/cgi-bin"
config=ConfigParser.ConfigParser()
temp=config.read(webpath+"/auth.conf")
try:
	filrsrv=config.get("server","ip")
except:
	print "No Filr Server Defined"
#filrsrv="172.17.2.79"
cgitb.enable(display=1, logdir="/srv/www/cgi-bin")
arguments = cgi.FieldStorage()
# create the cookie
#c=Cookie.SimpleCookie()
#d=Cookie.SimpleCookie()
# assign a value
#c['fuser']='admin'
# set the xpires time
#c['fuser']['expires']=1*1*3*60*60
#d['fpass']="n0v3ll"
#d['fpass']['expires']=1*1*3*60*60
#print c
#print d
print "Content-type: text/html\n"
print
print """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content=type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="/css/login.css" />
</head>"""
try:
	ck=os.environ["HTTP_COOKIE"]
	look="fuser" not in os.environ["HTTP_COOKIE"]
	cooks=ck.split(";")
	#print cooks
	for temp in cooks:
		if "fuser" in temp:
			items=temp.split("=")
			user=items[1]
		if "fpass" in temp:
			items=temp.split("=")
			password=items[1]
			#password1=lib.decrypt_val(password)
	mark=False
except:
	mark=True
	

if mark:
	print "<BR><h1>Logging in to Filr Server "+filrsrv+"</h1></BR>"
	print "No Cached Credentials"
	print "<BR></BR>"
	print "<body class=\"text\">"
	print "<form action=\"/cgi-bin/process.py\" method=\"post\">"
	print "<table class='center';id='table1';cellspacing='5px' cellpadding='5%';align='center' bgcolor='#007BEF'>"
	print "<font color=\"white\">"
	print "<tr>"
	print "<td text-align=\"center\"><img border='0' src=\"/css/mflogo.png\"></td>"
	print "</tr>"
	print "<tr>"
	print "<td class=\"text\">"
	print "Login Form"
	print "</td>"
	print "</tr>"
	print "<tr>"
	print "<td class=\"text\"> User Name</td>"
	print "<td> <input type=\"text\" name=\"user_name\" required/></td>"
	print "</tr>"
	print "<tr>"
	print "<td class=\"text\"> Password</td>"
	print "<td> <input type=\"password\" name=\"password\" required/></td>"
	print "</tr>"
	print "<tr>"
	print "<td><input type=\"submit\" value=\"Login to Filr\"/></td>"
	print "</tr>"
	print "</table>"
	print "</form>"
	print "</body>"
	print "</html>"
	
	
else:
	#print password
	password1=lib.decrypt_val(password.replace("\\","="))
	#print password1
	print "<script>"
	print """function del_cookie() {
		document.cookie = 'fuser' + '=;expires=Thu, 01-Jan-70 00:00:01 GMT;';
		document.cookie = 'fpass' + '=;expires=Thu, 01-Jan-70 00:00:01 GMT;';
		window.location.href = '/cgi-bin/cookies.py';
		}
		function createCookie(name,value,days) {
		if (days) {
			var date = new Date();
			date.setTime(date.getTime()+(days*24*60*60*1000));
			var expires = "; expires="+date.toGMTString();
		}
		else var expires = "";
		document.cookie = name+"="+value+expires+"; path=/";
		
		}
		function eraseCookie() {
			createCookie("fuser","",-1);
			createCookie("fpass","",-1);
		}

		"""
	print "</script>"
	print "<BR><h1>Logging in to Filr Server "+filrsrv+"</h1></BR>"
	print "Credentials Already Cached"
	print "<html>"
	print "<body>"
	print "<table class='center';id='table1';cellspacing='5px' cellpadding='5%';align='center' bgcolor='#007BEF'>"
	print "<font color=\"white\">"
	print "<tr>"
	print "<td text-align=\"center\"><img border='0' src=\"/css/mflogo.png\"></td>"
	print "</tr>"
	print "<tr>"
	print "<td class=\"text\"><button onclick='del_cookie()'>Delete Cached Credentials</button></td>"
	print "</tr>"
	print "<tr>"
	print "<td>"
	print "<form name=\"loginFormName\" id=\"loginFormId\" action=\"https://"+filrsrv+"/ssf/s/portalLogin\" method=\"post\">"
	print "<input type=\"hidden\" size=\"20\" name=\"j_username\" value=\""+user+"\">"
	print "<input type=\"hidden\" size=\"20\" name=\"j_password\" value=\""+password1+"\">"
	print "<input type=\"submit\" value=\"Login With Cached Credentials\"/>"
	print "</form>"
	print "</td>"
	print "</table>"
	print "</body>"
	print "</html>"
	
