import streamlit as st
from download_config import download_youtube_video
import os

st.set_page_config(page_title='Youtube Video Downloader', page_icon='📹', layout='wide')
st.title('📹 Youtube Video Downloader')
st.caption('Enter the URL in the sidebar and press the button.')

video_url = st.sidebar.text_input('Enter the video URL:')
button= st.sidebar.button('Start Download')
if video_url and button:
    download_file_path = download_youtube_video(video_url) 
    if download_file_path:
        try:
            with open(download_file_path, 'rb') as f:
                video_bytes = f.read()

            file_names = os.path.basename(download_file_path)

            st.download_button(
                label='Click to Download the video',
                data=video_bytes,
                file_name=file_names,
                mime='video/mp4'
            )

            st.success('Download Video Successfully!')
            os.remove(download_file_path)
        except Exception as e:
            st.error(f'Could not remove the file {e}') 
            
else:
    st.warning('Please enter a valid URL and click the button to start the download.')
