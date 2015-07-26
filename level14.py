level_url='http://www.pythonchallenge.com/pc/return/disproportional.html'
xml_url='http://www.pythonchallenge.com/pc/phonebook.php'
import xmlrpclib
phonebook=xmlrpclib.ServerProxy(xml_url)
print(phonebook.system.listMethods())
answer=phonebook.phone('Bert')
print(answer)

#555-ITALY

