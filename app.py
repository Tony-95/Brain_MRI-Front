import streamlit as st
import pandas as pd
from io import StringIO
import requests
import matplotlib.pyplot as plt

# Fonction pour envoyer l'image à l'API 
def get_predictions(image_file):

    api_url = "http://adresse_api/prediction"

    # Envoi de l'image à l'API
    files = {'file': image_file}
    response = requests.post(api_url, files=files)

    # Obtenir les résultats de l'API
    predictions = response.json()

    return predictions

def main():
    st.write("""#  Brain MRI Images""")

    st.image('MRI-Brain.png', caption='Brain MRI Images for Brain Tumor Detection')

    uploaded_file = st.file_uploader("Selectionnez votre IRM")
    
    if uploaded_file is not None:
        # Afficher l'image téléchargée
        st.image(uploaded_file, caption="Image téléchargée", use_column_width=True)

        # Bouton pour démarrer la prédiction
        if st.button("Faire la prédiction"):
            # Appeler la fonction pour obtenir les prédictions
            predictions = get_predictions(uploaded_file)

            # Afficher les prédictions dans un tableau
            st.subheader("Résultats de la prédiction")
            df = pd.DataFrame(predictions.items(), columns=["Classe", "Probabilité"])
            st.write(df)

            # Afficher les prédictions dans un graphique
            st.subheader("Graphique des prédictions")
            plt.bar(predictions.keys(), predictions.values())
            st.pyplot()

# Exécution de l'application
if __name__ == "__main__":
    main()