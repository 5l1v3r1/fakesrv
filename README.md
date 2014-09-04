fakesrv.py
==========
Fake Services with ease.

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

TODO:
Line by line file reading<br>
Conversations (to emulate FTP, SMTP, etc.)
