from raritan import rpc
from raritan.rpc import pdumodel
agent = rpc.Agent("https", "10.10.67.221", "admin", "P@ssw0rd")
pdu = pdumodel.Pdu("/model/pdu/0", agent)
metadata = pdu.getMetaData()
print (metadata)
