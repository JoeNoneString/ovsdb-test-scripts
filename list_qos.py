import socket
import json

OVSDB_IP = '127.0.0.1'
OVSDB_PORT = 6640

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((OVSDB_IP, OVSDB_PORT))


print "========list_qos========"
#get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Port":{"columns":["fake_bridge","interfaces","name","tag"]},"Interface":{"columns":["name"]},"Bridge":{"columns":["controller","fail_mode","name","ports"]},"Controller":{"columns":[]},"Open_vSwitch":{"columns":["bridges","cur_cfg"]}}], 'id':300}
get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Port":{"columns":["name","qos"]},"QoS":{"columns":["external_ids","other_config","queues","type"]},"Queue":{"columns":[]},"Open_vSwitch":{"columns":["cur_cfg"]}}], "id":0}

s.send(json.dumps(get_schema))
response = json.loads(s.recv(4096))
print response


