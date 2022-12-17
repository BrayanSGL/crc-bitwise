# Código CRC
Este código permite calcular y verificar el código de verificación de redundancia cíclica (CRC) para una cadena de texto. El polinomio generador y la longitud del código CRC están configurados al principio del código.

## Funciones
- string_to_binary(string): convierte una cadena de texto en una cadena binaria.
- crc(string_binary, polynomial): calcula el código CRC para una cadena binaria y un polinomio generador específico.
- verify(string_binary, polynomial, code_crc): verifica si una cadena binaria y un código CRC son válidos.
- main(): función principal que permite al usuario ingresar una cadena de texto y muestra el código CRC calculado y si la cadena es correcta o incorrecta.

## Uso
Para usar el código, ejecute el archivo CRC.py. Se le pedirá ingresar una cadena de texto. Después se mostrará el polinomio generador y el código CRC calculado para la cadena de texto. Además, se verificará si la cadena es correcta o incorrecta.

Para salir del programa, ingrese @Salir.

## Autor
Este código fue hecho por Brayan Snader Galeano Lara (@brayangaleanolara).

## Licencia
Este código esta bajo una licencia MIT.
