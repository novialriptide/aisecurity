import aisecurity.utils.socket as socket
import websocket


def real_time_recognize_socket(socket_url)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(socket_url,
                              on_message = lambda ws,msg: socket.on_message(ws, msg),
                              on_error = socket.on_error,
                              on_close = socket.on_close)
    ws.on_open = socket.on_open
    ws.run_forever()