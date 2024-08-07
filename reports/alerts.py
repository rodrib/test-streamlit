import streamlit as st
import youtube_dl

# Título de la aplicación
st.title("Información de Videos de un Canal de YouTube")

# Campo de entrada para la URL del canal de YouTube
channel_url = st.text_input("Ingresa la URL del canal de YouTube:", "https://www.youtube.com/c/ProgrammingKnowledge")

if channel_url:
    try:
        # Configuración para youtube_dl
        ydl_opts = {
            'extract_flat': True,
            'quiet': True,
            'force_generic_extractor': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(channel_url, download=False)
            if 'entries' in info_dict:
                videos = info_dict['entries']
                st.header(f"Videos del canal: {info_dict.get('title', 'Canal no encontrado')}")

                # Barra de progreso
                video_count = len(videos)
                progress_bar = st.progress(0)

                # Extraer y mostrar información de videos
                for i, video in enumerate(videos):
                    title = video.get('title', 'Título no disponible')
                    url = video.get('url', 'URL no disponible')
                    description = video.get('description', 'Descripción no disponible')
                    
                    st.subheader(f"Title: {title}")
                    st.write(f"URL: [Ver Video]({url})")
                    st.write(f"Description: {description}")
                    st.write('-' * 40)
                    progress_bar.progress((i + 1) / video_count)
            else:
                st.write("No se encontraron videos en este canal.")
    except Exception as e:
        st.error(f"Error al procesar el canal: {e}")
