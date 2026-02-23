import streamlit as st
import yt_dlp
import os

def download_youtube_video(url, output_path='downloads'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    
    ydl_opts = {
    'format': 'best',
    'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    'noplaylist': True,
    'quiet': True,
    'extractor_args': {
        'youtube': {
            'player_client': ['android', 'ios'],
            'player_skip': ['web', 'mweb']
        }
    },
}
    try:
        st.info(f"Currently given URL: {url}")
        with st.spinner('Downloading the video...'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                final_filepath = ydl.prepare_filename(info_dict)
        
        return final_filepath
    except Exception as e:
        st.error(f"Download Error: {e}")
        return None