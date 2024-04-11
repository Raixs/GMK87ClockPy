Esto es un repositorio inicial para crear un script que actualice la hora en el teclado GMK87

Se ha usado información relevante de los siguientes repositorios:

No funcional:
https://github.com/stefexec/GMK87TimeSetterPy/tree/master

Funcional en windows:
https://github.com/dove0rz/GMK87cmd/blob/master/GMK87cmd/GMK87cmd.cpp

Se incluye en esto repo un fichero llamado "captura.pcap" que contiene una captura de la comunicación entre el teclado y el software de configuración de GMK87.
Se debe usar WireShark para visualizar el contenido de este fichero.

Y el filtro para visualizar la comunicación es el siguiente:

usb.idVendor == 0x320f