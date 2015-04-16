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
print response
print ""
for i in response['result']['Bridge']:
    print response['result']['Bridge'][i]['new']['name']

c = response['result']['Bridge'].keys()
print ""
print c

print "========del-bridge========"
get_schema = {"method":"transact",\
              "params":["Open_vSwitch",\
              {"rows":[{"bridges":["uuid",c[0]]}],\
              "columns":["bridges"],"table":"Open_vSwitch","until":"==","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],\
              "timeout":0,"op":"wait"},\
              {"row":{"bridges":["set",[]]},"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"update"},\
              {"mutations":[["next_cfg","+=",1]],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"mutate"},\
              {"columns":["next_cfg"],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"select"},\
              {"comment":"ovs-vsctl: ovs-vsctl -vjsonrpc del-br br100","op":"comment"}], 'id':1} 

s.send(json.dumps(get_schema))
#response = json.loads(s.recv(4096))
response = s.recv(4096)
print response

#

#{u'error': None, u'id': 0, u'result': {u'Interface': {u'39acea99-be8c-4dd1-9029-1a55abf1cf5f': {u'new': {u'name': u'br100'}}}, u'Bridge': {u'ada4f1d9-5e4b-43ff-a601-ba19361b07f6': {u'new': {u'controller': [u'set', []], u'fail_mode': [u'set', []], u'name': u'br100', u'ports': [u'uuid', u'1c9aa6bf-6af8-4260-878b-5b6716d40e4b']}}}, u'Open_vSwitch': {u'e3fbe585-bee5-4633-b085-56d31f76e3fe': {u'new': {u'bridges': [u'uuid', u'ada4f1d9-5e4b-43ff-a601-ba19361b07f6'], u'cur_cfg': 51}}}, u'Port': {u'1c9aa6bf-6af8-4260-878b-5b6716d40e4b': {u'new': {u'interfaces': [u'uuid', u'39acea99-be8c-4dd1-9029-1a55abf1cf5f'], u'fake_bridge': False, u'tag': [u'set', []], u'name': u'br100'}}}}}



