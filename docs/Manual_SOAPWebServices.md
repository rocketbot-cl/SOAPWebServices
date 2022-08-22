# SOAP Web Services
  
Module to excecute methods from SOAP Web Services  
  
*Read this in other languages: [English](Manual_SOAPWebServices.md), [Español](Manual_SOAPWebServices.es.md), [Portuguese](Manual_SOAPWebServices.pr.md).*

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connects to the SOAP Web Service
  
Connects to the SOAP Web Service
|Parameters|Description|example|
| --- | --- | --- |
|SOAP Web Service's URL|URL to connect to|http://www.dneonline.com/calculator.asmx?WSDL|
|Username|Username with which you will connect to the service|username|
|Password|Password with which you will connect to the service|********|
|Alternate Login|Login with another method in case the default login does not work|False|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Select method to execute
  
Selects a method to execute
|Parameters|Description|example|
| --- | --- | --- |
|Select the method that you want to use|Service method to be used||
|Service Inputs|Parameters that will be sent to the service|[120, 240]|
|Assign result to variable|Variable where the result of the execution will be stored|Variable|
