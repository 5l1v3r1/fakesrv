fakesrv.py
==========
Fake services with ease.

Usage ./fakesrv.py {PROTOCOL} {PORT} {FILE OR MESSAGE}

EX...
<pre>
In one terminal...
# ./fakesrv.py -t -p 80 -m "have fun inside"
</pre>
<pre>
In another terminal
# nc 127.0.0.1 80
GET / HTTP/1.1

have fun inside
#
</pre>

It's really easy. You can use a file instead of a message with the -f option<br>

TODO
-----
- Line by line file reading
- Conversations (to emulate FTP, SMTP, etc.)
