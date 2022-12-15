# Made by Brayan Snader Galeano Lara
# @brayangaleanolara

import os
import sys


# Configuración del código CRC
POLYNOMIAL = {
    'name': 'CRC-16',
    'generator': 'x^16 + x^15 + x^2 + 1',
    'polynomial': 98309,  # 0b11000000000000101
    'size': 16
}


def string_to_binary(string):
    """Convierte una cadena de texto en una cadena binaria"""
    string_binary = ''
    for character in string:
        string_binary += f'{ord(character):08b}'
    return '0b' + string_binary


def crc(string_binary, polynomial):
    """Calcula el código CRC para una cadena binaria y un polinomio generador específico"""
    while True:
        if string_binary.bit_length() < polynomial.bit_length():
            return string_binary

        string_binary = string_binary ^ (polynomial << (
            string_binary.bit_length() - polynomial.bit_length()))


def verify(string_binary, polynomial, code_crc):
    """Verifica si una cadena binaria y un código CRC son válidos"""
    string_binary = string_binary | code_crc
    code_crc = crc(string_binary, polynomial)

    return code_crc == 0


def main():
    while True:
        os.system('cls')
        print(' ------ Calculo de código CRC -------\n \n1.Ingrese cualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string == '@Salir':
            print('------Programa terminado por el usuario-----')
            break

        # Convertir la cadena de texto a binario
        try:
            string_binary = int(string_to_binary(string), 2)
        except ValueError:
            print('La cadena de texto no puede ser convertida a binario.')
            os.system('pause')
            continue

        string_binary = string_binary << POLYNOMIAL['size']

        # Calc CRC
        code_crc = crc(string_binary, POLYNOMIAL['polynomial'])

        os.system('cls')
        print('-----------------------------------')
        print(f'Polinomio: {POLYNOMIAL["name"]}')
        print(f'Generador: {POLYNOMIAL["generator"]}')
        print(f'Polinomio: {POLYNOMIAL["polynomial"]}')
        print(f'Polinomio en binario: {bin(POLYNOMIAL["polynomial"])}')
        print('-----------------------------------')
        print(f'Cadena de texto: {string}')
        print(
            f'Cadena de texto en binario: {bin(string_binary >> POLYNOMIAL["size"])}')
        print(f'Código CRC: {bin(code_crc)}')

        # Verificar la cadena y el código CRC
        if verify(string_binary, POLYNOMIAL['polynomial'], code_crc):
            print('-----------------------------------')
            print('La cadena es correcta')
        else:
            print('-----------------------------------')
            print('La cadena es incorrecta')

        os.system('pause')


if __name__ == '__main__':

    try:
        main()
    except:
        print('Ha ocurrido un error inesperado. El programa se cerrará.')
        sys.exit()
