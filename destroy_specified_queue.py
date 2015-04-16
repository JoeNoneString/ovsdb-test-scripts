
import socket
import json

OVSDB_IP = '127.0.0.1'
OVSDB_PORT = 6640

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((OVSDB_IP, OVSDB_PORT))

specified_queue_id = 'fba45412-b3fd-4257-91c3-3b39f8fd2355'

print "========monitor-queue========"
get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Open_vSwitch":{"columns":["cur_cfg"]},"Queue":{"columns":[]}}], 'id':0}

s.send(json.dumps(get_schema))
response = json.loads(s.recv(409600))

print "monitor response: ", response
print ""
c = [] 
if response['result'].has_key('Queue'):
    c = response['result']['Queue'].keys()
    print "queue_id: ", c
if specified_queue_id in c:
    print response['result']['Queue'][specified_queue_id]
else:
    print "not found the queue: ", specified_queue_id

print "========destroy queue: fba45412-b3fd-4257-91c3-3b39f8fd2355========"
get_schema = {"method":"transact", \
              "params":["Open_vSwitch",\
              {"table":"Queue","where":[["_uuid","==",["uuid",specified_queue_id]]],"op":"delete"},\
              {"mutations":[["next_cfg","+=",1]],"table":"Open_vSwitch",\
               "where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"mutate"},\
              {"columns":["next_cfg"],"table":"Open_vSwitch","where":[["_uuid","==",\
              ["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"select"}],'id':1}
              #{"comment":"ovs-vsctl: ovs-vsctl -vjsonrpc destroy queue d701d00e-c468-4fa6-85b5-cfba9117ea22",\
              # "op":"comment"}], 'id':1}

s.send(json.dumps(get_schema))
#response = json.loads(s.recv(4096))
response = s.recv(4096)
print response

