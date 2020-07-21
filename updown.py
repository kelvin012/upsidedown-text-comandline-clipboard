import upsidedown
import sys
import pyperclip


def main(args):
    c = 0
    lista = []
    texto = ''

    while c < len(args):
        lista.append(args[c])
        c += 1

    del (lista[0])  # Remove a primeira posição da lista que cotem o nome do arquivo 'updown.py'
    texto = ' '.join(lista)
    texto_invetido = inverter_string(texto)
    pyperclip.copy(texto_invetido)
    print(texto)
    print(texto_invetido)
    return 0


def inverter_string(text):
    texto_invertido = upsidedown.transform(text)
    return texto_invertido


if __name__ == '__main__':
    sys.exit(main(sys.argv))
