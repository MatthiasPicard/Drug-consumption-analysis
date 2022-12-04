from menu import *

def text(placeholder):
    with placeholder.container():
        st.title("Conclusion et limites de l'analyse et du dataset")
        st.header("Conclusion")
        st.write(
            "**Conclusion: le modele SVC tuné et random forest tuné sont les meilleurs parmis ceux testés pour "
            "prédire avec un recall de 80% les personnes qui sont toximanes ou qui risquent de le devenir. Les "
            "deux modèles obtiennent une précision d'environ 55%.**"
            "\n**Concrètement, l'utilisateur du modèle peut espérer que 80% de personnes réellement "
            "\"toxicomanes\" soient prédites correctement si on assume que 45% des personnes \"non-toxicomanes\" "
            "sont classées en tant que \"toxicomane\". Il faut pour cela que les seuils de probabilité des "
            "probabilités soient de 23% (SVM) et 30% (RandomForest).**"
            "\n**Toutefois l'utilisateur reste libre de se fier à son jugement, en choisissant comment classifier "
            "une personne en regardant les probabilités prédites par le modèle.**")

        st.header("Limites de l'analyse et du dataset")
        st.write("- Nos résultats ne s’appliquent qu’aux habitants des pays anglo-saxons"
                 "\n- Nombre relativement faible de donnée (1886 personnes interrogées, dont 8 menteurs affirmant "
                 "avoir consommé la drogue fictive). Manque de représentativité des personnes âgées et de "
                 "certains pays."
                 "\n- Données légèrement biaisées, les personnes de l’échantillons consomment plus de drogue que la"
                 " population globale. (selon le papier de recherche qui a utilisé les données)"
                 "\n- Nous devons faire attention à l’interprétation de la target: une personne ayant consommé une "
                 "drogue illégale la semaine dernière n’est pas nécessairement toxicomane. Il faut prendre des "
                 "précautions quant aux prédiction du modèle. On peut dire qu’une personne prédite positivement a "
                 "des dispositions à consommer de la drogue, ce qui peut être une information intéressante pour "
                 "l’organisme d’assistance sociale où nous travaillons.")
