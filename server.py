import json
import math
import os
import socket

def main():
    connection()

def connection():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = '/tmp/socket_file'

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    sock.bind(server_address)

    sock.listen(1)

    while True:
        connection, client_address = sock.accept()

        try:
            print('connection from', client_address)

            while True:
                data = connection.recv(4096)

                if data:
                    data_str = data.decode("utf-8")

                    if is_correct_format(data_str):
                        json_dict = json.loads(data_str)
                        result = calculate_value(json_dict)
                        response = create_response_str(result, json_dict["id"])
                    else:
                        response = "Error"

                    connection.sendall(response.encode())
                else:
                    print('no data from', client_address)
                    break
        finally:
            print("closing current connection")
            connection.close()

# JSON形式で，かつ特定のkeyを持っているか判別
def is_correct_format(data_str):
    try:
        json_dict = json.loads(data_str)
    except:
        return False
    
    if (json_dict["method"] is None) or (json_dict["params"] is None) or (json_dict["id"] is None):
        return False

    return True

def calculate_value(json_dict):
    functions = {
        "floor": floor,
        "nroot": nroot,
        "reverse": reverse,
        "validAnagram": validAnagram,
        "sort": sort
    }

    try:
        method = json_dict["method"]
        params = json_dict["params"] 

        value = functions[method](*params)

        return value
    except:
        return "Error"

def floor(x):
    return math.floor(x)

def nroot(n, x):
    return math.pow(x, 1 / n) 

def reverse(str):
    return str[::-1] 

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(str):
    return sorted(str) 

def create_response_str(result, id):
    if str(result) == "Error":
        return "Error"

    response = {
        "results": result,
        "result_type": type(result).__name__,
        "id": id
    }
    return json.dumps(response)

if __name__ == '__main__':
    main()