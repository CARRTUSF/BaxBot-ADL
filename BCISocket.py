# Copyright (c) 2014, Andoni Aguirrezabal
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Remote
import socket

class BCISocket:
    def __init__(self):
        self.UDP_SERVER_IP = "0.0.0.0"
        self.UDP_PORT_RECV = 7500

        self.UDP_CLIENT_IP = "192.168.1.126"
        self.UDP_PORT_SEND = 7501

        self.bciSocketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bciSocketServer.bind((self.UDP_SERVER_IP, self.UDP_PORT_RECV))
        self.bciSocketServer.settimeout(None)
        print "Server Listening on port:", self.UDP_PORT_RECV

        self.bciSocketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "Client Sending on port:", self.UDP_PORT_SEND

    def sendMessage(self, message):
        self.bciSocketClient.sendto(message, (self.UDP_CLIENT_IP, self.UDP_PORT_SEND))

    def waitForCommand(self):
        data, addr = self.bciSocketServer.recvfrom(1024)
        data = data.split()
        return data
