import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

proxy.addInsult('gilipollas')
proxy.addInsult('payaso')
proxy.addInsult('idiota')
proxy.addInsult('irresponsable')
proxy.addInsult('impresentable')

print(proxy.getInsults())

print(proxy.insultme())
print(proxy.insultme())
print(proxy.insultme())
print(proxy.insultme())