from pathlib import Path
import shutil

from pylint.extensions.mccabe import PathGraph

CATEGORIAS = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Documentos': ['.pdf', '.docx', '.txt', '.pptx'],
    'Planilhas': ['.xlsx', '.xls', '.csv'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Programas': ['.exe', '.msi'],
}

def descobrir_categoria(extensao):
    for categorias, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categorias
    return 'Outros'

def nome_disponivel(destino):
    if not destino.exists():
        return destino
    contador = 1
    while True:
        novo = destino.with_name(f'{destino.stem} ({contador}){destino.suffix}')
        if not novo.exists():
            return novo
        contador += 1

def organizar(pasta, simular=True):
    pasta = Path(pasta)
    for item in pasta.iterdir():
        if not item.is_file():
            continue
        if item.name == Path(__file__).name:
            continue

        categoria = descobrir_categoria(item.suffix.lower())
        pasta_destino = pasta / categoria
        destino  = nome_disponivel(pasta_destino / item.name)

        print(f'{item.name} -> {categoria}/')
        if not simular:
            pasta_destino.mkdir(exist_ok=True)
            shutil.move(str(item), str(destino))

if __name__ == '__main__':
    caminho = input('Caminho da pasta a organizar: ')
    organizar(caminho, simular=True)
    if input('\nExecutar de verdade? (s/n): ').lower() == 's':
        organizar(caminho, simular=False)
        print('Pronto!')