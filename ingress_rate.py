import socket
import json

OVSDB_IP = '127.0.0.1'
OVSDB_PORT = 6640

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((OVSDB_IP, OVSDB_PORT))


print "========monitor-bridge========"
get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Port":{"columns":["fake_bridge","interfaces","name","tag"]},"Interface":{"columns":["name"]},"Bridge":{"columns":["controller","fail_mode","name","ports"]},"Controller":{"columns":[]},"Open_vSwitch":{"columns":["bridges","cur_cfg"]}}], 'id':0}

s.send(json.dumps(get_schema))
response = json.loads(s.recv(409600))

print "monitor response: ", response
print ""
for i in response['result']['Bridge']:
    print 'bridge name: ', response['result']['Bridge'][i]['new']['name']

c = response['result']['Bridge'].keys()
print ""
print 'bridge ID: ', c

c = response['result']['Interface'].keys()
print ""
print "interface ID: ", c
print "========set ingress_policing_rate========"
get_schema = {"method":"transact",\
              "params":["Open_vSwitch",\
              {"row":{"ingress_policing_rate":1000},\
               "table":"Interface","where":[["_uuid","==",["uuid",c[0]]]],"op":"update"},\
              {"mutations":[["next_cfg","+=",1]],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"mutate"},\
              {"columns":["next_cfg"],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"select"},\
              {"comment":"ovs-vsctl: ovs-vsctl -vjsonrpc set interface br100 ingress_policing_rate=10000","op":"comment"}], 'id':1}

s.send(json.dumps(get_schema))
#response = json.loads(s.recv(4096))
response = s.recv(4096)
print response

