from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
from suds.wsse import *
from suds.transport.https import HttpAuthenticated
from urllib.request import HTTPSHandler, ProxyHandler

class SoapObject:

    def __init__(self, wsdl, username='', password=''):
        self.wsdl = wsdl
        self.client = Client(self.wsdl, username=username, password=password)
        self.username = username
        self.password = password

    def getServiceNames(self):
        a = self.client.__str__()
        a = a.replace(" ", "")
        a = a.split("\n")

        lugar = None
        for index, i in enumerate(a, start=0):
            encontro = i.find("Methods")
            if encontro != -1:
                lugar = index
                break

        cuantosSon = a[lugar].replace("Methods(", "")
        cuantosSon = cuantosSon.replace("):", "")
        cuantosSon = eval(cuantosSon)
        lugar = lugar + 1
        cuantosSon = lugar + cuantosSon
        b = a[lugar:cuantosSon]
        c = []
        for each in b:
            where = each.find("(")
            if where != -1:
                each = each[:where]
                c.append(each)
        return c

    def serviceExe(self, serviceName, parameters):
        ejecucionServicio = f"self.client.service.{serviceName}(*{parameters})"
        result = eval(ejecucionServicio)
        print(dir(result))
        print(type(result))
        # result = getattr(self.client.service, serviceName)(*parameters)
        return result

class CustomTransport(HttpAuthenticated):
    def u2handlers(self):
        import ssl
        """
        Get a collection of urllib handlers.

        @return: A list of handlers to be installed in the opener.
        @rtype: [Handler,...]

        """
        handlers = []
        unverified_context = ssl.create_default_context()
        unverified_context.check_hostname = False
        unverified_context.verify_mode = ssl.CERT_NONE
        unverified_handler = HTTPSHandler(context=unverified_context)
        handlers.append(unverified_handler)
        handlers.append(ProxyHandler(self.proxy))
        return handlers 


class SoapObjectNew:
    def __init__(self, wsdl, username='', password=''):
        self.wsdl = wsdl
        self.username = username
        self.password = password
        imp2 = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
        imp2.filter.add('http://tempuri.org/')

        self.client = Client(self.wsdl, username=self.username, password=self.password, transport=CustomTransport(), doctor=ImportDoctor(imp2), timeout=100)

    def getServiceNames(self):
        a = self.client.__str__()
        a = a.replace(" ", "")
        a = a.split("\n")

        lugar = None
        for index, i in enumerate(a, start=0):
            encontro = i.find("Methods")
            if encontro != -1:
                lugar = index
                break

        cuantosSon = a[lugar].replace("Methods(", "")
        cuantosSon = cuantosSon.replace("):", "")
        cuantosSon = eval(cuantosSon)
        lugar = lugar + 1
        cuantosSon = lugar + cuantosSon
        b = a[lugar:cuantosSon]
        c = []
        for each in b:
            where = each.find("(")
            if where != -1:
                each = each[:where]
                c.append(each)
        return c

    def serviceExe(self, serviceName, parameters):
        theType = eval(parameters)
        if isinstance(theType, dict):
            ejecucionServicio = f"self.client.service.{serviceName}(**{parameters})"
        else:
            ejecucionServicio = f"self.client.service.{serviceName}(*{parameters})"
        result = eval(ejecucionServicio)
        return result
