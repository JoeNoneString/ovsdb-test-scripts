import socket
import json

OVSDB_IP = '127.0.0.1'
OVSDB_PORT = 6640

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((OVSDB_IP, OVSDB_PORT))

'''
print "========list_dbs_query========"
list_dbs_query = {"method":"list_dbs", "params":[], "id":0}
s.send(json.dumps(list_dbs_query))
response = s.recv(4096)
tmp = json.loads(response)
print tmp['result'][0]

print "========get_schema========"
get_schema = {"method":"get_schema", "params":["Open_vSwitch"], "id":0}
s.send(json.dumps(get_schema))
response = s.recv(4096*4)
print response

print "========echo========"
get_schema = {"method":"echo", "params":["aaaaaaaaaa"], "id":0}
s.send(json.dumps(get_schema))
response = json.loads(s.recv(4096))
print response

print "========create_bridge========"
get_schema = {"op":"insert", "table":"Bridge", "row":{"name": "br101"}}

#get_schema = {'op':'insert', "table":"Bridge", 'row':{'name': 'br101'}}
#get_schema = {'table': 'Bridge', 'op': 'insert', 'row': {'name': 'br100', 'ports': ['named-uuid', 'rowae9c0426_d593_4e9b_953b_12ea0ba18cd6']}}
s.send(json.dumps(get_schema))
response = json.loads(s.recv(4096))
print response

'''
print "========list_bridge========"
#get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Bridge":{"columns":["controller","fail_mode","name","ports"]}}], "id":0}
get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Port":{"columns":["fake_bridge","interfaces","name","tag"]},"Interface":{"columns":["name"]},"Bridge":{"columns":["controller","fail_mode","name","ports"]},"Controller":{"columns":[]},"Open_vSwitch":{"columns":["bridges","cur_cfg"]}}], 'id':300}
s.send(json.dumps(get_schema))
response = json.loads(s.recv(4096))
print response

