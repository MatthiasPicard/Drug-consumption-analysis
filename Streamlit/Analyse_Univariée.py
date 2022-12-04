from menu import *

def text(placeholder, dataset):
    with placeholder.container():
        st.title("\n\nPré-processing avant l'analyse")
        st.write("\nLes colonnes sur les infos personnelles et les tests de personnalité sont déjà "
                 "encodées et normalisées. Pour faire une analyse des données avec des valeurs compréhensibles,"
                 " nous allons retransformer ces données."
                 "\nNous allons enlever les personnes ayant indiqué qu'elles avaient consommé du Semeron "
                 "en considérant qu'ils ne sont pas fiables.")
        st.code('drugs.remove("fictious drug (Semeron)")'
                '\ndf=df.drop("fictious drug (Semeron)",axis=1);)')
        st.dataframe(dataset.head(10))

        st.write("\n\n\n")
        st.header("Analyse univariée, distribution des données sur chaque colonne")
        st.write("Dans cette partie, nous allons explorer chacunes des colonnes du dataset individuellement pour "
                 "avoir une bonne idée des valeurs qu'elles peuvent prendre et leur distribution."
                 "\nNotons que les chercheurs ayant travaillé sur les données ont indiqué que la population"
                 " échantillonée est non-représentative de la population globale et que la proportion de consommateurs"
                 " de drogues illicites est plus élevée ici que dans la réalité.")
        st.write()

        st.write("\n\n")

        st.image('Images/ana-uni/Distribution des données.png')

        st.write("- **Ethnicité**: La grande majorité des personnes interrogées ont répondu qu'elles étaient blanches."
                 " Les données à ce niveau ne sont pas représentative de la population des pays dont elles viennent."
                 "\n- **Age**: Les interrogés sont répartis par tranche d'âge. La majorité d'entre eux est jeune avec"
                 " une décroissance linéaire du nombre de personnes sur les tranches d'âges plus élevées."
                 "\n- **Genre**: Egalité quasi-parfaite entre les hommes et les femmes"
                 "\n- **Pays d'origine**: La grande majorité des interrogés viennent de pays anglo-saxons notamment"
                 " le Royaume-Uni et les Etats-unis. La catégorie \"Autre\" regroupe l'ensemble des pays non "
                 "anglo-saxons. "
                 "\n- **Niveau d'éducation**: La majorité des personnes ont un niveau de diplôme d'étude supérieur"
                 " en dessous du doctorat.")
        st.write("\n\n\n\n")
        st.subheader("Analyse des mesures sur les traits de personnalité")
        st.write("Nous n'avons pas dénormalisé les scores des tests de personnalité pour des raisons pratique. "
                 "De toutes façons, on ne perd pas d'information sur la distribution des scores pour chaque test.")
        st.image('Images/ana-uni/Distribution des données 2.png')
        st.write("\nOn peut voir que toutes les courbes dessinent une courbe proche d'une courbe en cloche. "
                 "On ne distingue pas d'anomalies dans ces données.")

        st.write("\n\n\n\n")
        st.image("Images/ana-uni/Distribution des données 3.png")
        st.write("Les drogues les plus utilisées sont celles qui sont légales (chocolat, caféine, nicotine et alcools)."
                 " Mais on remarque aussi une consommation très elevée de cannabis (illégal dans la plupart des pays"
                 " anglo-saxons et dans la majorité des états américains). Les autres drogues n'ont jamais été "
                 "utilisées par la plupart des participants, ou il y a longtemps."
                 "\nA noter que la drogue \"legal highs\" n'est en fait pas légale.")
    return placeholder