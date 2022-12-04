from menu import *
import pandas as pd


def init():
    perso = ['Age',
             'Gender',
             'Education',
             'Country',
             'Ethnicity']

    personality = [
        'Neuroticism',
        'Extraversion',
        'Openness to experience',
        'Agreeableness',
        'Conscientiousness',
        'Impulsiveness',
        'Sensation seeking'
    ]

    drugs = [
        "alcohol",
        "amphetamines",
        "amyl nitrite",
        "benzodiazepine",
        "caffeine",
        "cannabis",
        "chocolate",
        "cocaine",
        "crack",
        "ecstasy",
        "heroin",
        "ketamine",
        "legal highs",
        "LSD",
        "methadone",
        "mushrooms",
        "nicotine",
        "fictious drug (Semeron)",
        "volatile substance abuse"
    ]

    all_columns = perso + personality + drugs

    df = pd.read_csv(".data/drug_consumption.data", names=all_columns).reset_index(drop=True)

    drugs.remove("fictious drug (Semeron)")
    df = df.drop("fictious drug (Semeron)", axis=1);

    for i in drugs:
        df[i] = df[i].map({'CL0': 0, 'CL1': 1, 'CL2': 2, 'CL3': 3, 'CL4': 4, 'CL5': 5, 'CL6': 6})
        df[i] = df[i].apply(lambda x: int(x))

    df_analyse = df.copy()

    df_analyse["Age"] = df_analyse["Age"].map({-0.95197: '18-24',
                                               -0.07854: '25-34',
                                               0.49788: '35-44',
                                               1.09449: '45-54',
                                               1.82213: '55-64',
                                               2.59171: "65+"})

    df_analyse["Gender"] = df_analyse["Gender"].map({0.48246: "Female",
                                                     -0.48246: "Male"})

    df_analyse["Education"] = df_analyse["Education"].map({-2.43591: "Left school before 16 years",
                                                           -1.73790: "Left school at 16 years",
                                                           -1.43719: "Left school at 17 years",
                                                           -1.22751: "Left school at 18 years",
                                                           -0.61113: "Some college or university, no certificate or degree",
                                                           -0.05921: "Professional certificate/ diploma",
                                                           0.45468: "University degree",
                                                           1.16365: "Masters degree",
                                                           1.98437: "Doctorate degree"})

    df_analyse["Country"] = df_analyse["Country"].map({-0.09765: "Australia",
                                                       0.24923: "Canada",
                                                       -0.46841: "New Zealand",
                                                       -0.28519: "Other",
                                                       0.21128: "Republic of Ireland",
                                                       0.96082: "UK",
                                                       -0.57009: "USA"})

    df_analyse["Ethnicity"] = df_analyse["Ethnicity"].map({-0.50212: "Asian",
                                                           -1.10702: "Black",
                                                           1.90725: "Mixed-Black/Asian",
                                                           0.12600: "Mixed-White/Asian",
                                                           -0.22166: "Mixed-White/Black",
                                                           0.11440: "Other",
                                                           -0.31685: "White"})

    return df_analyse, perso, personality, drugs


def model(df_analyse, columns):
    df_model = df_analyse.copy()
    perso, personality, drugs = columns
    drugs_not_target = ['alcohol', 'caffeine', 'chocolate', 'nicotine', "cannabis"]

    drugs_target = [drug for drug in drugs if drug not in drugs_not_target]

    targets = []
    for i in range(len(df_model)):
        target = 0
        for col in drugs_target:
            if df_model.loc[i, col] in [5, 6]:
                target = 1
        targets.append(target)

    df_model["target"] = targets

    df_model = df_model.drop(drugs_target + ['alcohol', 'caffeine', 'chocolate', "cannabis"], axis=1)

    df_model = df_model.drop("Ethnicity", axis=1)

    df_model.loc[df_model["Age"] == "65+", "Age"] = '55-64'
    df_model.loc[df_model["Age"] == '55-64', "Age"] = '55+'

    df_model["Education"] = df_model["Education"].map({"Left school before 16 years": "Left school before 18 years",
                                                       "Left school at 16 years": "Left school before 18 years",
                                                       "Left school at 17 years": "Left school before 18 years",
                                                       "Left school at 18 years": "Left school before 18 years",
                                                       "Some college or university, no certificate or degree": "Some college or university, no certificate or degree",
                                                       "Professional certificate/ diploma": "Professional certificate/ diploma",
                                                       "University degree": "University degree",
                                                       "Masters degree": "Masters degree",
                                                       "Doctorate degree": "Doctorate degree"})

    df_model["Country"] = df_model["Country"].map({"Australia": "Australia+NZ",
                                                   "Canada": "Canada",
                                                   "New Zealand": "Australia+NZ",
                                                   "Other": "Other",
                                                   "Republic of Ireland": "UK+Ireland",
                                                   "UK": "UK+Ireland",
                                                   "USA": "USA"})

    df_model = df_model.drop(df_model[df_model["Country"] == "Other"].index, axis=0)

    return df_model