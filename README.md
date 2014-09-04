fakesrv.py
==========
Fake Services with ease.

Usage ./fakesrv.py {PROTOCOL} {PORT} {FILE OR MESSAGE}

EX... 
$ ./fakesrv.py TCP 80 "have fun inside"
$ nc 127.0.0.1 80
GET / HTTP/1.1

have fun inside
$ 

TODO:
Line by line file reading
Conversations (to emulate FTP, SMTP, etc.)
