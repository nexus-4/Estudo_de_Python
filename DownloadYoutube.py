#Se nao funcionar so isso:
#No terminal: pip install certifi depois utilize: /Applications/Python\ 3.9/Install\ Certificates.command de acordo com a versao do python

def DownloadVideo():
    import pytube
    link = input('Link: ')
    yt = pytube.YouTube(link)
    titulo = yt.title
    print(f'Inicializando Download de \033[33m{titulo}\033[m ')

    output_path = "/path/to/save/the/downloaded/file" #pasta selecionada

    yt.streams.first().download() #Linha para fazer o Download e guardar na pasta so sistema
    print('Download feito!!! ')
DownloadVideo()
