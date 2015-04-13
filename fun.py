import socket
import json

OVSDB_IP = '127.0.0.1'
OVSDB_PORT = 6640

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((OVSDB_IP, OVSDB_PORT))


print "========create_bridge========"
#get_schema = {"method":"monitor", "params":["Open_vSwitch",None,{"Port":{"columns":["fake_bridge","interfaces","name","tag"]},"Interface":{"columns":["name"]},"Bridge":{"columns":["controller","fail_mode","name","ports"]},"Controller":{"columns":[]},"Open_vSwitch":{"columns":["bridges","cur_cfg"]}}], 'id':300}

#get_schema = {"method":"transact", "params":["Open_vSwitch",{"rows":[{"bridges":["set",[]]}],"columns":["bridges"],"table":"Open_vSwitch","until":"==","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"timeout":0,"op":"wait"},{"row":{"name":"br100","ports":["named-uuid","rowfa753343_fbd2_48a9_86b7_cc9d7882b8bc"]},"table":"Bridge","uuid-name":"row97d37aed_cf0e_412f_83d9_b8f3e9ba16aa","op":"insert"},{"row":{"bridges":["named-uuid","row97d37aed_cf0e_412f_83d9_b8f3e9ba16aa"]},"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"update"},{"row":{"name":"br100","type":"internal"},"table":"Interface","uuid-name":"row8a5737e6_7bde_442e_a049_1648495551af","op":"insert"},{"row":{"name":"br100","interfaces":["named-uuid","row8a5737e6_7bde_442e_a049_1648495551af"]},"table":"Port","uuid-name":"rowfa753343_fbd2_48a9_86b7_cc9d7882b8bc","op":"insert"},{"mutations":[["next_cfg","+=",1]],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"mutate"},{"columns":["next_cfg"],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"select"},{"comment":"ovs-vsctl: ovs-vsctl -vjsonrpc add-br br100","op":"comment"}], "id":1}

get_schema = {"method":"transact", \
              "params":["Open_vSwitch",\
              {"rows":[{"bridges":["set",[]]}],"columns":["bridges"],"table":"Open_vSwitch","until":"==","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"timeout":0,"op":"wait"},\

              {"row":{"bridges":["named-uuid","switch123"]},"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"update"},\

              {"row":{"name":"br100","ports":["named-uuid","bridge123"]},"table":"Bridge","uuid-name":"switch123","op":"insert"},\

              {"row":{"name":"br100","interfaces":["named-uuid","port123"]},"table":"Port","uuid-name":"bridge123","op":"insert"},\

              {"row":{"name":"br100","type":"internal"},"table":"Interface","uuid-name":"port123","op":"insert"},\


              {"mutations":[["next_cfg","+=",1]],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"mutate"},\
              {"columns":["next_cfg"],"table":"Open_vSwitch","where":[["_uuid","==",["uuid","e3fbe585-bee5-4633-b085-56d31f76e3fe"]]],"op":"select"}\
               ],"id":1}

s.send(json.dumps(get_schema))
response = json.loads(s.recv(4096))
print response


