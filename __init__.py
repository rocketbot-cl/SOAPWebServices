# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import json
from operator import attrgetter
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'SOAPWebServices' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)


def convert(J):
    global convert
    if hasattr(J, "__keylist__"):
        J = {key: convert(value) for key, value in dict(J).items()}
            
    if hasattr(J, "append"):
        J = [convert(data) for data in J]
        
    return J


from soapObject import SoapObject, SoapObjectNew

global clientSoapObject

module = GetParams("module")

try:

    if (module == "connectTo"):

        username = GetParams("username")
        password = GetParams("password")
        wsdl = GetParams("wsdl")
        checkLogin = GetParams("checkLogin")

        if not username:
            username = ''
        if not password:
            password = ''
            
        if checkLogin != 'True':
            clientSoapObject = SoapObject(wsdl, username, password)
        else:
            clientSoapObject = SoapObjectNew(wsdl, username, password)

        whereToStore = GetParams("whereToStore")
        
        resultConnection = False
        if clientSoapObject.client:
            resultConnection = True

        SetVar(whereToStore, resultConnection)

    if (module == "getMethods"):
        
        serviceNames = clientSoapObject.getServiceNames()
        ServiceNames = []

        for each in serviceNames:
            ServiceNames.append(each)

        SetVar("SOAPWebServices_fake_var", {
            "serviceNames" : serviceNames,
        })

    if (module == "sendData"):

        iframe = GetParams("iframe")
        serviceName = eval(iframe)["serviceName"]
        
        variables = GetParams("vars")
        
        resultSoap = clientSoapObject.serviceExe(serviceName, variables)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, convert(resultSoap))

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e