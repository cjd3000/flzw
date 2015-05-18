import zmq


def zsend(host, mesg):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    try:
        socket.setsockopt(zmq.LINGER, 0)
        socket.connect("tcp://" + host)
        socket.send_json(mesg)

        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)
        if poller.poll(2000):
            got = socket.recv_json()
            return got
        else:
            raise Exception("timeout")

    finally:
        socket.close()
        context.term()
