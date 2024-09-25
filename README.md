La base de datos por ahora es simple, esta compuesta de una clase Coche que tiene parametros para, desde una base de datos extraer marca, modelo y año de un coche desde una id registrada en una base de datos sql.
A parte se observan dos funciones; cargar_desde_bd que inicializa una conexion con una base de datos en sql y verifica que la id esta asociada a una marca, modelo y año; y una funcion detalles encargada de 
imprimir los detalles del coche en caso de que existan unos asociados a la id y de imprimir un mensaje de error en caso contrario
