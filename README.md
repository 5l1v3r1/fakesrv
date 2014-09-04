fakesrv.py
==========
Fake Services with ease.

Usage ./fakesrv.py {PROTOCOL} {PORT} {FILE OR MESSAGE}

EX... <br>
<pre>
$ ./fakesrv.py TCP 80 "have fun inside"<br>
$ nc 127.0.0.1 80<br>
GET / HTTP/1.1<br><br>
have fun inside<br>
$ 
</pre>

TODO:
Line by line file reading<br>
Conversations (to emulate FTP, SMTP, etc.)
