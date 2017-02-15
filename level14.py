import xmlrpclib
def call(name):
    xml_url='http://www.pythonchallenge.com/pc/phonebook.php'
    phonebook=xmlrpclib.ServerProxy(xml_url)
    answer=phonebook.phone(name)
    return answer

if __name__=="__main__":
    level_url='http://www.pythonchallenge.com/pc/return/disproportional.html'
    xml_url='http://www.pythonchallenge.com/pc/phonebook.php'
    phonebook=xmlrpclib.ServerProxy(xml_url)
    print(phonebook.system.listMethods())
    print(phonebook.system.methodHelp("phone"))
    print(phonebook.system.methodSignature('phone'))
    print(phonebook.system.getCapabilities())
    answer=phonebook.phone('Bert')
    print(answer)

    #555-ITALY


