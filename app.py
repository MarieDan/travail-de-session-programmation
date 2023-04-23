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


st.write(f"_Il est souvent difficile de choisir entre l'achat ou la location d'un véhicule neuf. C'est pourquoi cette application vous permettra de déterminer le meilleur choix selon les conditions du marché automobile en vigueur._", font_size= [35])

st.markdown("<hr>", unsafe_allow_html=True)

#Questions générales
année_véhicule = st.text_input("Quel est l'année du véhicule ?")
modèle = st.text_input("Quel est le modèle du vehicule ?")

#Section sur l'achat de la voiture
st.header (" :shopping_trolley: Achat d'une voiture ")

prix_vehicule = st.number_input ("Quel est le prix de vente du véhicule", key =1)
p = prix_vehicule*1.14975 
st.write(f" Le prix de vente total incluant les taxes est de {p:.2f}$", key=500)

depot_garantie_achat = (st.number_input ("Quel est le montant du dépôt de garantie du véhicule, s'il y a lieu ? ", key=2))
accompte_achat = st.number_input ("Quel est l'accompte applicable en cas d'achat du véhicule?", key =3)
aa = accompte_achat*1.14975
st.write ( f" Le montant total du financement en cas d'achat du véhicule est de {aa:.2f}$ ", key =2)

terme = st.slider("Terme en mois :", min_value=12, max_value=120, key="terme")
Taux_financement_achat_pourcent = st.slider("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0, key="taux_financement")
Taux_financement_achat = Taux_financement_achat_pourcent / 100

vma= ((p-aa)/(((1-(1+(Taux_financement_achat/12))**(-terme)))/(Taux_financement_achat/12)))

st.write(f" Votre versement mensuel estimé si vous décidez d'acheter la voiture est de **{vma:.2f}** $", key=3, text_size="50pt")
#Comptant nécessaire avant l'achat du véhicule
st.write (f"En cas de d'achat du véhicule, vous auriez besoins d'un montant de **{accompte_achat:.2f}**$", text_size='24pt')

#Section sur la location de la voiture

st.header (" :spiral_calendar_pad: Location d'une voiture ")

prix_location = st.number_input ("Quel est le prix du véhicule en cas de location", key ="prix_location")
st.write ( f" Le prix de la voiture pour location est de {prix_location:.2f}$", key =4)

accompte_loc = st.number_input ("Quel est l'accompte applicable en cas de location , sur le vehicule?", key =5)
al = accompte_loc*1.14975

frais_gestion = st.number_input ("Quel est le frais de gestion applicable en cas de location , s'il y a lieu?", key =6)

st.write ( f" Le montant total du financement est de {(prix_location - al ) + frais_gestion:.2f}$", key =5)

financement_loc_pourcent = st.slider("Taux de financement en pourcentage :", min_value=0.0, max_value=10.0, key="financement_loc")
financement_loc = financement_loc_pourcent / 100
terme_loc = st.number_input(" Quel est le terme en mois ?", key="terme_loc")

valeur_residuelle = (st.number_input ("Quel est la valeur résiduelle du véhicule, s'il y a lieu ? ", key=9))
depot_garantie = (st.number_input ("Quel est le montant du dépôt de garantie du véhicule, s'il y a lieu ? ", key=10))

vml = (((prix_location-al)+frais_gestion) - ((valeur_residuelle)*((1+(financement_loc/12))**(-terme_loc))))/(((1-(1+(financement_loc/12))**(-terme_loc)))/(financement_loc/12))*(1+(financement_loc/12))
vml_taxes = vml*1.14975
st.write(f" Votre versement mensuel estimé si vous décidez de louer la voiture est de **{vml_taxes:.2f}** $, taxes incluses", font_size=[30], key=6)

#comptant nécessaire avant la location de la voiture
comptant_loc = (accompte_loc + vml_taxes + depot_garantie)
st.write (f" En cas de location, vous auriez besoins d'un montant de **{comptant_loc:.2f}** $.", font_size=[30])

st.markdown("<hr>", unsafe_allow_html=True)

#Résumer des deux sections à l'aide d'un tableau récapitulatif 
st.subheader (" :bar_chart: Voici un tableau qui résume les deux options qui s'offrent à vous : acheter ou louer le véhicule")

data = {'Options': ['Achat', 'Location'],
        'Versement mensuel': [vma,vml_taxes],
        'Comptant total requis': [depot_garantie_achat,comptant_loc] }

df = pd.DataFrame(data)
df = df.round(2)
st.table(df)

st.markdown("<hr>", unsafe_allow_html=True)

if vma < vml_taxes:
    st.subheader(":heavy_check_mark: _Étant donné que le versement mensuel estimé pour l'achat du véhicule est moins cher que celui de la location, il est recommandé **d'acheter le véhicule**._" )

elif vml_taxes < vma:
    st.subheader(":heavy_check_mark: _Étant donné que le versement mensuel estimé pour la location est moins cher que celui de l'achat, il est recommandé **de louer le véhiule**._" )

else:
    st.subheader(":heavy_check_mark: Les versements mensuels estimés pour l'achat et la location du véhicule sont les mêmes. À vous de choisir l'option qui vous convient le mieux.")
