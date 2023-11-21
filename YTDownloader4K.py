
def DownloadVideo():
    import os
    import pytube

    link = input('Link: ')
    yt = pytube.YouTube(link)
    titulo = yt.title
    print(f'Inicializando Download de \033[33m{titulo}\033[m ')

    # Caminho para a pasta de documentos no Mac
    output_path = os.path.expanduser("~/Documents/")

    # Filtrar apenas a stream 4K
    stream = yt.streams.get_by_itag(313)  # Use o ITAG correspondente à stream desejada

    if not stream:
        print("Stream 4K não disponível. Encerrando o programa.")
        return

    # Exibir informações sobre a stream antes de baixar
    print("Informações sobre a stream selecionada:")
    print(f" Resolução: {stream.resolution}, FPS: {stream.fps}, Tipo: {stream.subtype}")

    stream.download(output_path)

    print('Download feito!!! ')

DownloadVideo()
