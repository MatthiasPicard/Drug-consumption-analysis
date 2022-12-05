import streamlit as st
from streamlit_option_menu import option_menu
import Analyse_Univariée
import Analyse_Bivariée
import Machine_Learning
import pandas as pd
import init
import Intro
import CCL

if __name__ == '__main__':
    st.set_page_config(page_title='Drug Analysis ESILV Project', page_icon='💉', layout='wide')

    dataset, perso, personality, drugs = init.init()
    columns = [perso, personality, drugs]

    intro = st.empty()
    a_u = st.empty()
    a_b = st.empty()
    ml = st.empty()
    ccl = st.empty()

    with st.sidebar:
        selected = option_menu("Analyse de la consommation de drogue selon la personnalité et le profil des individus",
            ["Introduction", "Analyse univariée",  "Analyse bivariée", 'Machine Learning', 'Conclusion et limites'],
            icons=['house', 'box', 'boxes', 'file-code-fill',
                   #'easel',
                   'door-open-fill'],
            menu_icon="three-dots-horizontal",
            default_index=0, orientation="vertical",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "25px", "icon-align": "left"},
                "menu-title": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee",
                               "color": "#000000"},
                "nav-link": {"font-size": "15px", "icon-align": "left", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "#000000"},
                "nav-link-selected": {"background-color": "green"},
            }
        )


    if selected == "Introduction":
        intro.empty()
        Intro.text(intro)

    elif selected == "Analyse univariée":
        a_u.empty()
        Analyse_Univariée.text(a_u, dataset)

    elif selected == "Analyse bivariée":
        a_b.empty()
        Analyse_Bivariée.text(a_b, dataset, columns)

    elif selected == "Machine Learning":
        ml.empty()
        Machine_Learning.text(ml, dataset, columns)

    elif selected == "Conclusion et limites":
        ccl.empty()
        CCL.text(ccl)
