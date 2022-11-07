# Made by Brayan Snader Galeano Lara
# @brayangaleanolara

import os

POLYNOMIAL = {
    'name': 'CRC-16',
    'generator': 'x^16 + x^15 + x^2 + 1',
    'polynomial': 98309,  # 0b11000000000000101
    'size': 16
}


def string_to_binary(string):
    string_binary = ''
    for character in string:
        string_binary += f'{ord(character):08b}'
    return '0b'+string_binary


def crc(string_binary, polynomial):

    while True:
        # print('-----------------------------------')
        #print(f'P: {polynomial}, {bin(polynomial)}, {polynomial.bit_length()}')
        #print(f'S: {string_binary}, {bin(string_binary)}, {string_binary.bit_length()}')
        if string_binary.bit_length() < polynomial.bit_length():
            return string_binary

        string_binary = string_binary ^ (polynomial << (
            string_binary.bit_length() - polynomial.bit_length()))
        #print(f'R: {string_binary}, {bin(string_binary)}, {string_binary.bit_length()}')
        # os.system('pause')


def main():
    while True:
        os.system('cls')
        print(' ------ Calculo de código CRC -------\n \n1.Ingrese cualquier cadena\n2.Ingrese: @Salir para cerrar el programa\n')
        string = input('# Ingrese la cadena de Texto > ')
        if string == '@Salir':
            print('------Programa terminado por el usuario-----')
            break

        string_binary = int(string_to_binary(string), 2)
        string_binary = string_binary << POLYNOMIAL['size']

        # Calc CRC
        code_crc = crc(string_binary, POLYNOMIAL['polynomial'])
        os.system('cls')
        print('-----------------------------------')
        print(f'Polinomio: {POLYNOMIAL["name"]}')
        print(f'Generador: {POLYNOMIAL["generator"]}')
        print(f'Polinomio: {POLYNOMIAL["polynomial"]}')
        print(f'Polinomio: {bin(POLYNOMIAL["polynomial"])}')
        print('-----------------------------------')
        print(f'Cadena de texto: {string}')
        print(
            f'Cadena de texto en binario: {bin(string_binary>>POLYNOMIAL["size"])}')
        print(f'Código CRC: {bin(code_crc)}')

        # Verific
        string_binary = string_binary | code_crc
        code_crc = crc(string_binary, POLYNOMIAL['polynomial'])

        if code_crc == 0:
            print('-----------------------------------')
            print('La cadena es correcta')
        else:
            print('-----------------------------------')
            print('La cadena es incorrecta')

        os.system('pause')


if __name__ == '__main__':
    main()
