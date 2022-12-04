from menu import *
from init import model

def text(placeholder, dataset, columns):
    with placeholder.container():
        st.title("Prédiction des profils plus disposés à consommer souvent des drogues avec du machine learning")
        st.header("Définition de la target et pré-processing")
        st.subheader("Préparation de la target et modification des données")
        st.write("Au vu de l'analyse que nous avons faite précédemment, nous allons modifier quelque peu notre dataset:"
                 "\nPour la création de notre target, nous n'allons pas prendre en compte les consommations de "
                 "chocolat, de caféine, de nicotine et d'alcool. Nous allons aussi enlever le cannabis à cause de sa"
                 " sur-représentation parmi les autres drogues non citées ci-dessus (si on ne l'avait pas enlevée,"
                 " notre modèle aurait un gros biais et ferait essentiellement de la prédiction de consommation de"
                 " cannabis). La consommation de nicotine sera une des datas qui nous permettera de prédire la target."
                 "\nPour les autres variables, nous allons regrouper certaines classes pour éviter les problèmes "
                 "d'overfitting à cause du peu de donnée."
                 "\nPour l'âge, nous allons regrouper les 65+ avec les 55-64 (groupe de personnes similaires."
                 "\nPour l'éducation, nous allons regrouper toute les personnes ayant arrêté l'école avant 18 ans "
                 "(groupe de personnes similaires aussi)"
                 "\nNous allons enlever la classe \"autres\" pour les pays (manque de précision). Nous allons regrouper"
                 " l'Australie et la Nouvelle-Zélande ainsi que le Royaume-Uni et l'Irlande (à priori assez similaires)"
                 "\nNous allons enlever la colonne ethnie (corrélation linéaire faible avec la consommation de drogue,"
                 " sur-représentation des blancs et potentiel problème moral lié au fait de se servir de l'éthnie comme"
                 " d'un critère discriminant).")

        st.code("targets=[]"
                "\nfor i in range(len(df_model)):"
                "\ntarget=0"
                "\nfor col in drugs_target:"
                "\nif df_model.loc[i,col] in [5,6]:"
                "\ntarget=1"
                "\ntargets.append(target)"
                "\n\ndf_model[\"target\"]=targets")

        data_ml = model(dataset, columns)
        st.dataframe(data_ml.head(10))

        st.write("\n\n\n\n")
        st.header("Création et comparaison des modèles")
        st.write("Nous allons considérer que nous travaillons pour une association ou un organisme d'assistance sociale"
                 " qui souhaite anticiper si une personne a plus ou moins de chance de devenir consommateur régulier de"
                 " drogue. Nous allons résoudre ce problème en développant un modèle de prédiction."
                 "\nDans ce cadre, nous considérons qu'il est plus grave que le modèle considère qu'une personne ne va"
                 " pas se tourner vers la drogue alors que c'est le cas (faux négatif), que le cas inverse où "
                 "l'algorithme est trop prudent et considère qu'une personne \"safe\" risque de se tourner vers la "
                 "drogue (faux négatif). Nous allons viser 80% de recall, c'est à dire que le modèle classe au moins "
                 "80% des vraies potentiels toxicomanes en tant que tels, et n'en oublie que 20%. Le but sera donc de "
                 "limiter au maximum les conséquences sur la précision du modèle (c'est à dire limiter le nombre de "
                 "personnes considérées comme toxicomane alors qu'elles sont \"safe\")."
                 "Nous allons d'abord tester six modèles sans apporter de tuning et en les évaluant avec une courbe ROC"
                 " et une matrice de confusion, puis nous apporterons du tuning. Nous examinerons enfin le compromis "
                 "entre recall et précision.")
        st.write("\nLes différents modèles sont :"
                 "\n\nModèles simples : "
                 "\n- **SVC** : Ou Support Vector (Machine) Classifier"
                 "\n- **Voisins** : Le modèle voisins utilise à l'algorithme du KNN"
                 "\n- **Logistique** : Effectue une régression logistique"
                 "\n\nModèles complexes :"
                 "\n- **ADAboost** : utilise la fonction AdaBoostClassifier"
                 "\n- **randomforest** : utilise la fonction RandomForestClassifier"
                 "\n- **xgb** : utilise la fonction XGBClassifier de la bibliothèque xgboost")

        st.write("\n")
        st.subheader("Evaluation des modèles sans tuning")
        st.write("On teste 3 modèles simples et 3 modèles plus complexes. L'intérêt est de voir si un modèle complexe "
                 "apporte réellement une plus-value à l'estimation. Si ce n'est pas le cas, on va préférer un modèle "
                 "simple pour éviter les potentiels problèmes d'overfitting."
                 "\nOn va d'abord directement tester nos modèles sur le testset:")
        st.write("")

        st.image("Images/ml/ROC 1.png")

        st.write("")
        with open('doc2.txt', 'r', encoding='utf8') as file_:
            for line_ in file_:
                st.text(f'{line_}')

        st.write("\n\n")
        st.write("Tous les modèles testés ont des résultats assez similaires. On constate qu'ils ont du mal à prédire "
                 "correctement les vraies positifs (recall faible). La courbe ROC indique que chaque modèle peut "
                 "espérer environ 80% de vrais positifs (recall=80%) au prix de 30% sur le taux de faux positifs "
                 "environ (plutôt 25% pour SVC).")

        st.write("\n\n")
        st.subheader("Tuning des modèles")
        st.write("On modifie les hyperparamètres du modèle pour améliorer le modèle. On passe par une cross-validation "
                 "sur les données d'entrainement pour limiter l'overfitting. On utilise le score ROC_AUC pour évaluer "
                 "les configurations possibles de chaques modèles.")

        with open('doc3.txt', 'r', encoding='utf8') as file_:
            for line_ in file_:
                st.text(f'{line_}')

        st.write("\nLa meilleure configuration possible pour le KNN ressemble à de l'overfitting (k_neighbors=8 --> "
                 "élevé donc risque d'overfitting). Elle affiche aussi un score ROC_AUC légèrement en dessous des "
                 "autres modèles."
                 "\nLa random forest à aussi des valeurs élevées qui sous-entendent un risque d'overfitting, mais le "
                 "fait d'avoir un grand nombre d'estimateurs dans la forêt fait \"lisser\" l'overfiting.")

        st.write("\n\n")
        st.subheader("Evaluation avec tuning")
        st.write("On teste maintenant les configurations sélectionnées sur notre testset")
        st.image("Images/ml/ROC 2.png")

        with open('doc4.txt', 'r', encoding='utf8') as file_:
            for line_ in file_:
                st.text(f'{line_}')

        st.write("\n\n")
        st.write("Les modèles tunés sont légèrement meilleurs que les non-tunés quand on regarde les scores (sauf pour "
                 "le KNN, qui s'empire à cause de l'overfitting)."
                 "\nEn regardant les courbes ROC, on peut voir qu'on arrive à atteindre un recall de 80% au prix d'un "
                 "taux de faux positifs d'environ 25% avec les modèles SVC et random forest. Nous allons considérer que"
                 " ce sont les deux meilleurs modèles pour notre problème."
                 "\nOn va maintenant changer le compromis précision/recall pour les deux modèles.")

        st.write("\n\n")
        st.subheader("Compromis recall/précision et conclusions")
        st.write("Nous allons récuperer les probabilités associées à chaque prédictions par le modèle et modifier le"
                 " seuil de décision (à la base, le modèle calcule une probabilité et renvoie la valeur 1 si la proba "
                 "est supérieur à 50% et 0 sinon)."
                 "\nLe but étant d'indiquer à l'utilisateur quelle est le meilleur seuil de probabilité pour avoir 80% "
                 "de vrais positifs. Nous allons ensuite comparer les deux modèles pour voir lequel des deux offre la "
                 "meilleure précision à ce seuil."
                 "\nOn va tracer une courbe de précision et de rappel pour les deux courbes et trouver la précision et "
                 "la valeur de seuil associée aux 80% de recall pour les deux modèles.")
        st.image("Images/ml/ROC 3.png")
        st.write("La précision devient assez chaotique quand le seuil de probabilité augmente (ce n'est pas un "
                 "comportement anormal, mais on ne peut pas vraiment faire confiance à cette partie de la courbe quand "
                 "on sera sur notre testset, on ne touchera pas à des valeurs de seuil supérieures à 0.5 de toutes "
                 "façons)")
        st.text("précision  à 80% de recall pour random forest: 0.5169628432956381, seuil de proba associé:0.306722188092048"
                "\nprécision  à 80% de recall pour SVC: 0.508716323296355, seuil de proba associé:0.24973200779854532")

        st.write("La random forest a une précision légerement meilleure à 80% de recall, mais on reste essentiellement "
                 "dans la marge d'erreur."
                 "\nSi on applique les seuils de probabilité sur le testset, on obtient les résultats suivants:")

        st.text("SVC: "
                "\nf1 score= 0.6640316205533596"
                "\nprecision= 0.56"
                "\nrecall= 0.8155339805825242"
                "\nRandomForest: "
                "\nf1 score= 0.6533864541832669"
                "\nprecision= 0.5540540540540541"
                "\nrecall= 0.7961165048543689")
        st.image("Images/ml/ROC 4.png")

        st.write("Le SVC a une précision et un rappel légèrement plus élevés que le random forest sur le testset. "
                 "Cela confirme que les deux sont assez proches.")

    return placeholder