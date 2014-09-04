fakesrv.py
==========
Fake services with ease.

Usage ./fakesrv.py {PROTOCOL} {PORT} {FILE OR MESSAGE}

EX...
<pre>
In one terminal...
# ./fakesrv.py TCP 80 "have fun inside"
File "have fun inside" does not exist. Using input as message to send.
</pre>
<pre>
In another terminal
# nc 127.0.0.1 80
GET / HTTP/1.1

have fun inside
#
</pre>

It's really easy. You can use a file instead of a message. The script just checks if the {MESSAGE OR FILE} argument exists as a file and if not then it just prints as a message.

TODO:
- Line by line file reading
- Conversations (to emulate FTP, SMTP, etc.)
