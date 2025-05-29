from pytube import YouTube
import os

def baixar_musica(url, artista, musica, pasta_destino="musicas_baixadas"):
    """
    Baixa áudio do YouTube como MP4 e renomeia para MP3 (sem conversão real).
    Nota: O arquivo será um MP4 com extensão .mp3 (funciona na maioria dos players).
    """
    try:
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        
        print(f"Baixando: {artista} - {musica}...")
        
        # Baixa como MP4 e renomeia para MP3
        caminho_mp4 = stream.download(output_path=pasta_destino, filename=f"{artista} - {musica}.mp4")
        caminho_mp3 = caminho_mp4.replace(".mp4", ".mp3")
        os.rename(caminho_mp4, caminho_mp3)
        
        print(f"✅ Concluído: {artista} - {musica}.mp3")

    except Exception as e:
        print(f"❌ Erro em {artista} - {musica}: {e}")

# Exemplo de uso:
if __name__ == "_main_":
    musicas = [
        {"url": "https://www.youtube.com/watch?v=MVYZayhlLJ8", "artista": "Lulu Santos", "musica": "Tempos Modernos"},
        {"url": "https://www.youtube.com/watch?v=JGEi1hxV-zA", "artista": "Lulu Santos", "musica": "Como Uma Onda"},
        {"url": "https://www.youtube.com/watch?v=HHNkleVOms0", "artista": "Lulu Santos", "musica": "Apenas Mais uma de Amor"},
        {"url": "https://www.youtube.com/watch?v=NA4sm_oKIBA", "artista": "Lulu Santos", "musica": "Assim Caminha a Humanidade"},
        {"url": "https://www.youtube.com/watch?v=wU6hX4EJlRM", "artista": "Lulu Santos", "musica": "Toda Forma de Amor"},
        {"url": "https://www.youtube.com/watch?v=ZdSaYRdTFdU", "artista": "Lulu Santos", "musica": "Um Certo Alguem"},
        {"url": "https://www.youtube.com/watch?v=Stu0HizgZAI", "artista": "Lulu Santos", "musica": "Tudo Azul"},
        {"url": "https://www.youtube.com/watch?v=EKC52rQqHEo", "artista": "Lulu Santos", "musica": "Casa"},
        {"url": "https://www.youtube.com/watch?v=zmDOuaCJQYw", "artista": "Lulu Santos", "musica": "Certas Coisas"},
        {"url": "https://www.youtube.com/watch?v=98r48fVksXk", "artista": "Lulu Santos", "musica": "Sábado a Noite"},
    ]

    for item in musicas:
        baixar_musica(item["url"], item["artista"], item["musica"])