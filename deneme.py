
from re import S
import streamlit as st
import pandas as pd
from streamlit_player import st_player, _SUPPORTED_EVENTS
import matplotlib.pyplot as plt
import time
import numpy as np
#from streamlit_gallery.utils.readme import readme


def main():
    #with readme("streamlit-player", st_player, __file__):
    options = {
            "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
            "progress_interval": 500
        }
    spectra = st.file_uploader("upload file", type={"csv", "txt"})
    
    video= open("C:/Users/apache/Desktop/squirrel_animal_rodent_fur_cute_701.mp4","rb")
    video=st.video(video)
        
    event = st_player(video, **options)
        #xc=event.data["playedSeconds"]*100
        #xc=event.data["playedSeconds"]
        

    st.write(event)
    

       
    
    
    fig, ax = plt.subplots(3,2)
    if spectra is not None:
        spectra_df = pd.read_csv(spectra)
        spectra_df.set_index("TimeStamp (ms)", inplace=True)
        spectra_df=spectra_df.applymap(lambda x: str(x.replace(',','.')))
        spectra_df[list(spectra_df)] =spectra_df[list(spectra_df)].apply(pd.to_numeric)    
        
        spectra_df["Attention"].plot(ax=ax[0,0])
        spectra_df["Arousal"].plot(ax=ax[0,1])
        spectra_df["Engagement"].plot(ax=ax[1,0])
        spectra_df["Frustration"].plot(ax=ax[1,1])
        spectra_df["MentalWorkload"].plot(ax=ax[2,0])
        spectra_df["Positiveness"].plot(ax=ax[2,1])
    
    
        #while True:
            #ax[0,0].axvline(x=1000, color='r', linestyle='-')
    
     #plt.plot(spectra_df["Attention"])
    
    
    #while True:
    #    ax[0,0].axvline(x=2000, color='r', linestyle='-')
    #    ax[1,0].axvline(x=xc, color='r', linestyle='-')
    #    ax[0,1].axvline(x=xc, color='r', linestyle='-')
    #    ax[1,1].axvline(x=xc, color='r', linestyle='-')
    #    ax[2,0].axvline(x=xc, color='r', linestyle='-')
    #    ax[2,1].axvline(x=xc, color='r', linestyle='-')
    #    #st.write(event.data["playedSeconds"])
    st.pyplot()     
    #st.line_chart(spectra_df["Attention"])
    #st.line_chart(spectra_df["Arousal"])
    #plt.axvline(x=10000, color='r', linestyle='-')
    #st.pyplot()


    #st.line_chart(spectra_df["Engagement"])
    #st.line_chart(spectra_df["Frustration"])
    #st.line_chart(spectra_df["MentalWorkload"])
    #st.line_chart(spectra_df["Positiveness"])

if __name__ == "__main__":
    main()
