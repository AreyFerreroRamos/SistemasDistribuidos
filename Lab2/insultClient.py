import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

proxy.addInsult('gilipollas')
proxy.addInsult('payaso')

print(proxy.getInsult())

proxy.insultme()