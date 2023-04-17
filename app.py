import streamlit as st
import pandas as pd

image = "auto.png"
col1, mid, col2, col3 = st.columns([1,15,30,1])
with col1:
    st.image(image, width=120)
with col2:
    st.title (" Louer ou acheter ?")
with col3:
    st.image(image, width=120) 


#st.write(f"_Il est souvent difficile de choisir entre l'achat ou la location d'un véhicule neuf. C'est pourquoi cette application vous permettra de déterminer le meilleur choix selon les conditions du marché automobile en vigueur._")

st.markdown("<hr>", unsafe_allow_html=True)

année_véhicule = st.text_input("Quel est l'année du véhicule ?")
modèle = st.text_input("Quel est le modèle du vehicule ?")

st.header (" Achat d'une voiture ")

prix_vehicule = st.number_input ("Quel est le prix de vente du véhicule", key =1)
p = prix_vehicule*1.14975 
st.write (f" Le prix de vente total incluant les taxes est de {p:.2f}", key =1)

depot_garantie_achat = (st.number_input ("Quel est le montant du dépôt de garantie du véhicule, s'il y a lieu ? ", key=2))
accompte_achat = st.number_input ("Quel est l'accompte applicable en cas d'achat du véhicule?", key =3)
aa = accompte_achat*1.14975
st.write ( f" Le montant total du financement en cas d'achat du véhicule est de {aa} ", key =2)

#Taux_financement_achat = float(st.number_input("Quel est le taux de financement accordé ?"))
#st.write(f" {Taux_financement_achat},%")
#Taux_financement_achat = float(st.number_input("Quel est le taux de financement accordé ?", min_value=0.0, max_value=100.0))
#Taux_financement_achat = Taux_financement_achat / 100.0  # conversion en décimal
#terme = (st.number_input ("Quel est le terme de financement, en mois", key=4))
#Taux_financement_achat = st.slider(("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0) / 100, key="taux_financement")

terme = st.slider("Terme en mois :", min_value=12, max_value=120, key="terme")
Taux_financement_achat_pourcent = st.slider("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0, key="taux_financement")
Taux_financement_achat = Taux_financement_achat_pourcent / 100

vma= ((p-aa)/(((1-(1+(Taux_financement_achat/12))**(-terme)))/(Taux_financement_achat/12)))



st.write(f" Votre versement mensuel estimé si vous décidez d'acheter la voiture est de {vma:.2f} $", key=3)

st.header (" Location d'une voiture ")

prix_location = prix_vehicule
st.write ( f" Le prix de la voiture pour location est de {prix_location}", key =4)

accompte_loc = st.number_input ("Quel est l'accompte applicable en cas de location , sur le vehicule?", key =5)
al = accompte_loc*1.14975

frais_gestion = st.number_input ("Quel est le frais de gestion applicable en cas de location , s'il y a lieu?", key =6)

st.write ( f" Le montant total du financement est de {(prix_location - al ) + frais_gestion}", key =5)

#financement_loc = float(st.number_input("Quel est le taux de financement accordé ?", key=7))
#financement_loc = float(st.number_input("Quel est le taux de financement accordé ?", min_value=0.0, max_value=100.0), key=6)
#financement_loc = financement_loc/ 100.0 
#financement_loc = st.slider(("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0) / 100 , key = "financement_loc")

financement_loc_pourcent = st.slider("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0, key="financement_loc")
financement_loc = financement_loc_pourcent / 100
terme_loc = st.slider("Terme en mois :", min_value=12, max_value=120, key="terme_loc")

valeur_residuelle = (st.number_input ("Quel est la valeur résiduelle du véhicule, s'il y a lieu ? ", key=9))
depot_garantie = (st.number_input ("Quel est le montant du dépôt de garantie du véhicule, s'il y a lieu ? ", key=10))

vml = prix_location /(((1-(1+(financement_loc/12))**(-terme_loc)))/(financement_loc/12))*(1+(financement_loc/12)) + ((valeur_residuelle)*(1+(financement_loc/12))**(-terme_loc))
vml_taxes = vml*1.14975
st.write(f" Votre versement mensuel estimé si vous décidez de louer la voiture est de {vml_taxes:.2f} $, taxes incluses", key=6)

comptant_loc = (accompte_loc + vml_taxes + depot_garantie)
st.write = (f" En cas de location, vous auriez besoins d'un montant de {comptant_loc}.")

#vml = ((prix_vehicule /(1-(1+ financement_loc ))/12)**((-(terme_loc)*12)/(financement_loc/12))*(1+(financement_loc/12))) + (valeur_residuelle *(1+(financement_loc/12))**((-(terme_loc)*12)/(financement_loc/12)))
#comptant_loc = accompte_loc + depot_garantie + ((prix_vehicule /(1-(1+ financement_loc ))/12)**((-(terme_loc)*12)/(financement_loc/12))*(1+(financement_loc/12)))+(((valeur_residuelle *1.14975)-depot_garantie)*(1+(financement_loc/12))**((-(terme_loc)*12)/(financement_loc/12)))

st.header (" Voici un tableau résumé les deux options qui s'offrent à vous, acheter ou louer le véhicule")

data = {'Options': ['Achat', 'Location'],
        'Versement mensuel': [vma,vml_taxes],
        'Comptant total requis': [depot_garantie_achat,comptant_loc] }

df = pd.DataFrame(data)
st.table(df)


#Ajouter une phrase qui dit qu'etant donner X est moins cher de prendre cette option 
