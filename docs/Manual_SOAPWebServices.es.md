# SOAP Web Services
  
Module to excecute methods from SOAP Web Services 

*Read this in other languages: [English](Manual_SOAPWebServices.md), [Español](Manual_SOAPWebServices.es.md), [Portuguese](Manual_SOAPWebServices.pr.md).*
  
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conectar al SOAP Web Service
  
Conectar al SOAP Web Service
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL del SOAP Web Service|URL a la que se conectará|http://www.dneonline.com/calculator.asmx?WSDL|
|Nombre de usuario|Nombre de usuario con el que se conectará al servicio|usuario|
|Password|Contraseña con la que se conectará al servicio|********|
|Login alternativo|Iniciar sesión con otro método en caso de que el login por defecto no funcione|False|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Ejecutar método
  
Ejecutar método
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione el método que desea usar|Método del servicio que se utilizará||
|Parámetros del servicio|Parámetros que serán enviados al servicio|[120, 240]|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|Variable|
