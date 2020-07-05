import socket
import json

with socket.socket() as s:
    host = '127.0.0.1'
    port = 8889
    address_and_port = (host, port)
    s.bind(address_and_port)
    s.listen()
    conn, addr = s.accept()

    with conn:
        data = conn.recv(1024)
        r = str(data).split('Host: ')[1]
        host = r.split("\\r\\nConnection")[0]
        r = str(data).split('Connection: ')[1]
        connection = r.split("\\r\\nCache-Control")[0]
        if 'Cache-Control' in str(data):
            r = str(data).split('Cache-Control: ')[1]
            cache_control = r.split("\\r\\nUpgrade")[0]
        else:
            cache_control = None
        r = str(data).split('Upgrade-Insecure-Requests: ')[1]
        upgrade_insecure_requests = r.split("\\r\\nUser-Agent")[0]
        r = str(data).split('User-Agent: ')[1]
        user_agent = r.split("\\r\\nAccept")
        r = str(data).split('Accept: ')[1]
        accept = r.split("\\r\\nAccept")[0]
        r = str(data).split('\\r\\nAccept-Language: ')[1]
        accept_language = r.split("\\r\\n")[0]

        response = json.dumps({
            "Host": host,
            "Connection": connection,
            "Cache-Control": cache_control,
            "Upgrade-Insecure-Requests": upgrade_insecure_requests,
            "User-Agent": user_agent,
            "Accept": accept,
            "Accept-Language": accept_language
        })

        conn.send(f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: application/json\n\n "
                  f"{response}".encode("utf-8"))
