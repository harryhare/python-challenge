import pdb
input="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
def fun(x):
	print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
	result=""
	for c in x:
		d=ord(c)
		if(d>=97 and d<=122):
				d=d+2
				if(d>122):
						d=d-26
				result+=chr(d)
		else:
				result+=c
	print(result)
	return result
fun(input)
