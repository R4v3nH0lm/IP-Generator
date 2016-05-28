################################################################################
### Import library's
from netaddr import *

################################################################################
### Global Variables


################################################################################
### Scripted Actions

def OutputToJson(IP_ADDRESS, NETMASK, GATEWAY):
	info = {
	'IP': IP_ADDRESS,
	'NetMask': NETMASK,
	'GateWay': GATEWAY
	}
	print info

def GetGatewayAndNetmask(IP_ADDRESS):
	IP = IPNetwork(IP_ADDRESS +'/25')
	NETMASK = str(IP.netmask)
	GATEWAY = str(IPAddress(IP.last))
	#print 'Gateway address is: ' + GATEWAY
	OutputToJson(IP_ADDRESS, NETMASK, GATEWAY)

def GenerateIP(SITE_BINARY, POD_BINARY, CLUSTER_BINARY, RACK_BINARY, U_BINARY):
	RAW_BINARY_STRING = SITE_BINARY + POD_BINARY + CLUSTER_BINARY + RACK_BINARY + U_BINARY
	#print 'Raw binary string: ' + RAW_BINARY_STRING
	SECOND_OCTECT = int(RAW_BINARY_STRING[:8], 2)
	THIRD_OCTECT = int(RAW_BINARY_STRING[8:16], 2)
	FOURTH_OCTECT = int(RAW_BINARY_STRING[16:32], 2)
	IP_ADDRESS = '10.' + str(SECOND_OCTECT) + '.' + str(THIRD_OCTECT) + '.' + str(FOURTH_OCTECT)
	#print 'IP Address is: ' + IP_ADDRESS
	GetGatewayAndNetmask(IP_ADDRESS)

def ConvertToBinary(USER_INPUT_SITE, USER_INPUT_POD, USER_INPUT_CLUSTER, USER_INPUT_RACK, USER_INPUT_U):
	SITE_INT = int(USER_INPUT_SITE)
	SITE_BINARY = "{0:05b}".format(SITE_INT)
	POD_INT = int(USER_INPUT_POD)
	POD_BINARY = "{0:05b}".format(POD_INT)
	CLUSTER_INT = int(USER_INPUT_CLUSTER)
	CLUSTER_BINARY = "{0:04b}".format(CLUSTER_INT)
	RACK_INT = int(USER_INPUT_RACK)
	RACK_BINARY = "{0:04b}".format(RACK_INT)
	U_INT = int(USER_INPUT_U)
	U_BINARY = "{0:06b}".format(U_INT)
	#print 'Site binary is: ' + SITE_BINARY + '\n' + 'Pod binary is: ' + POD_BINARY + '\n' + 'Cluster binary is: ' + CLUSTER_BINARY + '\n' + 'Rack binary is: ' + RACK_BINARY + '\n' + 'U binary is: ' + U_BINARY
	GenerateIP(SITE_BINARY, POD_BINARY, CLUSTER_BINARY, RACK_BINARY, U_BINARY)

def GetUserInput():
	USER_INPUT_SITE = raw_input ('Site number? ')
	USER_INPUT_POD = raw_input ('Pod number? ')
	USER_INPUT_CLUSTER = raw_input ('Cluster number? ')
	USER_INPUT_RACK = raw_input ('Rack number? ')
	USER_INPUT_U = raw_input ('Rack U location? ')
	#print 'Generating IP for a server at site ' + USER_INPUT_SITE + ' in pod ' + USER_INPUT_POD + ' in cluster ' + USER_INPUT_CLUSTER + ' in rack ' + USER_INPUT_RACK + ' in U location ' + USER_INPUT_U
	ConvertToBinary(USER_INPUT_SITE, USER_INPUT_POD, USER_INPUT_CLUSTER, USER_INPUT_RACK, USER_INPUT_U)

GetUserInput()