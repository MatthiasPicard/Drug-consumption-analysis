from menu import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

#Fonction heatmap

def heatmap(dataset, analyse_column, columns, method = 'heatmap', cmap = "coolwarm"):

    fig, ax = plt.subplots(figsize = [25,12])

    analyse = sorted(list(dataset[f'{analyse_column}'].unique()), key = str)

    matrix = [[0]*len(columns) for i in range(len(analyse))]
    heatmap = np.array(matrix)

    for i in range(dataset.shape[0]):
        for k, obj in enumerate(columns):
          # 12 is first instance of drug in columns
          # this test is if columns = drugs
          if dataset.iloc[i, k+12] in [5,6]:
            heatmap[analyse.index(dataset.iloc[i,list(dataset.columns).index(f'{analyse_column}')]), k] += 1

    if method == 'barplot' :
        matrix= []
        for i in range(heatmap.shape[1]):
            for j in range(heatmap.shape[0]):
              line = [columns[i], heatmap[j,i], analyse[j]]
              matrix.append(line)
        dataframe = pd.DataFrame(matrix, columns = ['x', 'y', f"{analyse_column}"])
        #sns.barplot(data = dataframe, x = 'x', y = 'y', hue = analyse_column)
        fig = px.bar(dataframe, x = 'x', y = 'y', color = analyse_column)
    if method == 'heatmap' :
        #sns.heatmap(heatmap, cmap = cmap, linewidths = 0.5, annot= True, annot_kws = {'size':10}, square = True, fmt = 'g')
        fig = px.imshow(heatmap, x=columns, y =analyse)
        fig.update_traces(text=heatmap, texttemplate="%{text}")
        ax.set_yticklabels(analyse, rotation = 0)
        ax.set_xticklabels(columns, rotation = 90)
    return fig



def text(placeholder, dataset, columns):

    perso, personality, drugs = columns
    with placeholder.container():
        st.title("Analyse bivariée entre données et target et corrélations")
        st.write("\nDans cette partie, nous allons compléter notre analyse univariée en comparant les variables avec"
                 " l'ensemble des colonnes drogues (que nous regrouperons ensuite pour créer notre target) et en"
                 " établissant des corrélations, ce qui nous permettera de tirer des conclusions sur les modifications"
                 " à apporter sur le dataset avant de créer notre modèle")

        st.write("\n\n\n\n")
        st.header("Heatmaps")
        st.write("\nRegardons la distribution de chaque groupe de colonnes sur les informations personnelles avec la"
                 " consommation de chaque drogue."
                 "\nPour les heatmaps, nous allons compter uniquement les personnes ayant consommé de la drogue il y a"
                 " moins d'une semaine, puisque ce sont ces personne que nous inclurons dans notre target.")
        st.write("\n")

        g = heatmap(dataset, 'Age', drugs, cmap="crest")
        st.subheader("**Répartition des personnes ayant consommées de la drogue il y a moins d'une semaine selon les tranches d'âges**")
        st.plotly_chart(g)
        #st.image('Images/ana-bi/Répartition 1.png')
        st.write("\nLa heatmap ci-dessus est en accord avec les premières observations de l'analyse univariée"
                 " (sur-représentation des \"jeunes\" dans le dataset). Même en prenant en compte ce biais dans "
                 "les données, on ne distingue pas de changement de tendance quand on \"descend\" dans la heatmap.")
        st.write("\n")

        st.image('Images/ana-bi/Répartition 2.png')
        st.write("\nEncore une fois, la tendance correspond aux premières observations: les USA et le Royaume-Uni sont"
                 " sur-représentés. On constate tout de même que le canabis est particulièrment consommé aux Etats-Unis"
                 " même si le pays ne represente que 30% des données (le cannabis est légal dans certains états).")
        st.write("\n")

        st.image('Images/ana-bi/Répartition 3.png')

        g = heatmap(dataset, 'Gender', drugs, cmap="crest", method='barplot')
        st.subheader(
            "**Répartition des personnes ayant consommées de la drogue il y a moins d'une semaine selon les tranches d'âges**")
        st.plotly_chart(g)
        #st.image('Images/ana-bi/Répartition 4.1.png')
        st.write("\nLa répartiton des hommes et des femmes est quasiment équivalente dans le dataset, mais on constate"
                 " que les hommes sont nettement plus nombreux à avoir consommé des drogues illégales il y a moins "
                 "d'une semaine que les femmes. Le genre semble être un critère discriminant important pour notre "
                 "analyse.")
        st.write("\n")

        st.image('Images/ana-bi/Répartition 5.png')
        st.write("\nLa sur-représentation des personnes blanches est très visible.")

        st.write("\n**Dans toutes les heatmaps ci-dessus, on constate qu'un grand nombre de cases ont 0 ou très peu de"
                 " données. Pour notre futur modèle, ce genre de chose peut créer de l'overfitting si on lui demande de"
                 " faire une prédiction sur un profil qu'il n'a que très peu vu. On va donc chercher à regrouper nos"
                 " classes ou enlever les personnes appartenant à des classes sous-representées.**")

        st.write("\n\n\n\n")
        st.header("Graphes de corrélation")
        st.write("\nPour mieux visualiser les relations nous allons faire des corrélations heatmaps selon différentes"
                 " méthodes."
                 "\nNous utiliserons toujours la corrélation de Pearson (corrélation linéaire, hypothèse de répartition"
                 " des données suivant la loi normale). Toutefois, les résultats étaient assez similaire avec la "
                 "méthode de spearman (car il n'y a pas d'outliers dans nos données).")
        st.image("Images/ana-bi/Corr 1.png")
        st.write("\nOn voit clairement que le chocolat, la caféine et l'alcool n'ont presque pas de corrélation avec"
                 " les autres drogues (cela n'a donc pas de sens de les inclure dans le même groupe que les autres"
                 " drogues). Ce qui n'est pas vraiment le cas du cannabis et de la nicotine.")
        st.write("\n")

        st.image("Images/ana-bi/Corr 2.png")
        st.write("\nOn trouve encore une fois que la consommation d'alcool, de chocolat et de caféine n'ont pas "
                 "vraiment de corrélation avec le comportement. La corrélation avec les autres drogues n'est pas très"
                 " élevée mais reste non négligeable. Le comportement semble être un bon critère discriminant pour "
                 "notre analyse, surtout la recherche de sensations. La nicotine a des valeurs semblables aux autres"
                 " drogues, mais elles restent suffisament faibles pour se dire que l'ajout d'une colonne "
                 "\"consomation de nicotine\" dans le dataset pour prédire la target reste pertinent.")
        st.write("\n")

        st.image("Images/ana-bi/Corr 3.png")
        st.write("\nLa corrélation entre l'ethnie/l'éducation et la consommation de drogue est très faible.")

    return placeholder