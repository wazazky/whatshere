import os

def main():
    carpeta_actual = os.getcwd()
    excluir = {'WhatsHere.py'}
    archivos = []

    for carpeta, subcarpetas, archivos_en_carpeta in os.walk(carpeta_actual):
        for archivo in archivos_en_carpeta:
            ruta_relativa = os.path.relpath(os.path.join(carpeta, archivo), carpeta_actual)
            if archivo.startswith('.') or archivo in excluir:
                continue
            archivos.append(ruta_relativa)

    with open('lista_archivos.txt', 'w', encoding='utf-8') as f:
        for archivo in archivos:
            f.write(archivo + '\n')

    os.startfile('lista_archivos.txt')

if __name__ == '__main__':
    main()
