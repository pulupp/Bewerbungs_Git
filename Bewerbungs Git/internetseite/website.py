from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
     

#---load assets----
lottie_coding = load_lottieurl("https://lottie.host/6581ad67-9fbc-47e9-b610-f94b15509a63/wqNpL6ERxw.json")
img_contact_form = Image.open("bilder/Bewerbungsfoto.jpeg")
# HEADER SECTION

with st.container():
    st.subheader("Hi, ich bin Philipp :wave:")
    st.title("Ein sportlicher, humorvoller Mensch aus Köln.")
    st.write("Ich bin immer auf der Suche nach neuem Wissen und setze mich daher gerne mit neuen Technologien wie Python auseinander, um meinen Wissensstand kontinuierlich zu erweitern.")
    st.write("Ich benutze diese Website um zu lernen, aber auch um meinen Lernstand mit euch zu teilen.")

# what to do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Was ich so mache:")
        st.write("##")
        st.write(
            """
            Aktuell arbeite ich als Schulbegleiter, setzte mich neben meinem Beruf aber auch mit Informatik außeinander.
            Ich bin sehr gerne von Menschen umgeben, befasse mich aber auch gerne mit Themen, die mich kognitiv herrausfordern. Mit der Informatik versuche ich beide Welten zu verbinden.
            Darüber hinaus bin ich ein leidenschafftlicher Sportler:
            - ich spiele Basketball (seit ich 11 Jahre alt bin.)
            - betreibe seit einiger Zeit Jiu-Jitsu.
            - habe für ein paar Jahre Kickboxen gemacht.
            - und mache regelmäßig Fitnesssport.
            
            Außerdem begeistere ich mich für Musik, weshalb ich seit einigen Jahren Gitarre spielen
            - das jedoch weniger gut.
            
            """
        )
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
    
with st.container():
    st.write("---")
    st.header("Was ich sonst so gemacht habe:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image here
        st.image(img_contact_form)
    with text_column:
        st.subheader("Meine beruflichen Stationen")
        st.write(
            """
            Ich habe gearbeitet als:
            - Fahrer beim Westdeutschen Rundfunk
            - bei der Flaschenpost im Lieferdienst
            - bei Duratent als Lagermitarbeiter
            - und bei Arztpraxis Dr. Knopp als Labormitarbeiter
            """
        )
        st.subheader("Tätigkeiten in meiner Freizeit")
        st.write(
            """
            Ehrenamtlich war/bin ich tätig bei:
            - der Deutschen Kinderkrebs Stiftung und habe Camps der Waldpiraten in Heidelberg begleitet.
            - DJK Köln Ost eV. und betreue dort zwei Jugendmannschaften im Basketball.
            
            Und ich bin Mitglied einer Band, in der ich Gitarre spiele.
            
            """
        )

with st.container():
    st.write("---")
    st.header("Bringt euch mit mir in Verbindung")
    st.write("##")
    
    contact_form = """
    
    <form action="https://formsubmit.co/ph.gross@mail.de" method="POST">
        <input type = "hidden" name = "_captcha" value = "false">
        <input type="text" name="name" placeholder = "Dein Name" required>
        <input type="email" name="email" placeholder = "Deine Emailadresse" required>
        <textarea name = "Nachricht" placeholder = "Deine Nachricht an mich" requierd></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
    st.empty()