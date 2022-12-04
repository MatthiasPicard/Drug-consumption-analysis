from menu import *


def text(intro):
    with intro.container():
        st.title("Analyse de la consommation de drogue selon la personnalité et le profil des individus")
        st.title("Introduction")
        st.write("lien du dataset:\n"
                 "https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29")
        st.write("\n")
        with open('doc.txt', 'r', encoding='utf8') as file:
            for line in file:
                st.write(f'{line}')

        st.write("\n\n")
        st.header("Description du dataset")
        st.write("**Shape** : (1885, 31)")
        st.write("Les 11 premières colonnes relatives aux données personnelles et à la personnalité sont au format "
                 "**float64** et toutes les colonnes relatives aux drogues sont au format **object**. Nous allons "
                 "donc transformer les données personnelles qui sont numériques en données catégorielles, et "
                 "transformer les données relatives aux drogues au format  numérique en enlevant la particule "
                 "**\"CL\"**.")
        st.write("Il n'y a pas de données dupliquées, et aucune valeur Nan dans le DataFrame.")

    return intro