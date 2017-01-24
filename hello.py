#!/usr/bin/env python

import os
from pprint import pprint
import json
import urlparse
import sys

from templates import login_page

print "Content-type: text/HTML"

username = 'xin'
password = 'nix'
cL = os.environ["CONTENT_LENGTH"]
cookie = os.environ["HTTP_COOKIE"]
logged_in=False

if cookie == "logged-in=True":
	logged_in = True
elif cL:
	bytes_to_read = int(cL)
	content = sys.stdin.read(bytes_to_read)
	params = urlparse.parse_qs(content)

	if(params["username"][0]==username and params["password"][0]==password):
		print "Set-Cookie: logged-in=True"
		logged_in=True
	else:
		print "nope"

print

if not logged_in:
	print r"""
	    <h1> Welcome! </h1>

	    <form method="POST" action="hello.py">
		<label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
		<label> <span>Password:</span> <input type="password" name="password"></label>

		<button type="submit"> Login! </button>
	    </form>
	    """
else:
	print "this is a secret message for", username

