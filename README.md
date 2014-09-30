fakesrv.py
==========
Fake services with ease.

<pre>
usage: fakesrv.py [-h] [-t] [-u] -p PORT [-m MSG] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -t, --tcp             listen on TCP
  -u, --udp             listen on UDP
  -p PORT, --port PORT  port number to listen on
  -m MSG, --message MSG
                        message to output on connection
  -f FILE, --file FILE  file to read a message from, read out on conneciton
</pre>

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
The server waits for input before it responds to anything. Feel free to modify it to just spit out stuff right away.<br>
The default protocol is TCP and the default message is "Hello World!"<br>
The only required argument is the port to listen on.<br>

TODO
-----
- Line by line file reading
- Conversations (to emulate FTP, SMTP, etc.)
