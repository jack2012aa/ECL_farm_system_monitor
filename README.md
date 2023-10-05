# ECL_farm_system_monitor
> Check the status of distributed computers and equipment.

## Introduction
In our lab (__*NTUAST SBL*__), several computers are in different farms to control devices like cameras, thermometers, etc. However, the Internet is unstable in such location and so do electricity. We need a way to make sure that every device works correctly. This is this program's job: to check the status of devices and alarm lab members when error happens.

## Structure
`farm` is the part installed in farms' computers. It is a server, which `lab` application can access the status of local devices. Those devices include:
* Cameras
* Routers
* File systems (whether data are collected correctly)
* PLC
* Gateways

Ｍost tests are done by ping the device. The server uses __Flask__, __Tornado__ and __nginx__ on __Windows__.

`lab` is the part installed in lab's computer. It trys to access computers in different location and log their status every 10 second. If the server returns an error message, emails will be sent to people in charge, which is done by __smtp__.

At the beginning, I constructed the server in `lab` and let `farm` apps send message to it. But I found that there is a __Cisco__ firewall in lab's internet and no one know how to configure it. It blocks requests into the server. As a result, I move the server out.

## To Do
* A common interface for those devices tested through IP ping.