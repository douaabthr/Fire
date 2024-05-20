from django.shortcuts import render, redirect
from admin_atlantis.forms import RegistrationForm,LoginForm,UserPasswordChangeForm,UserPasswordResetForm,UserSetPasswordForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def signup(request):
  if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        print('Account created successfully!')
        return redirect('/accounts/login/')
      else:
        print("Registration failed!")
  else:
    form = RegistrationForm()
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class AuthSignin(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/change-password.html'
  form_class = UserPasswordChangeForm 

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/recover-password.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/reset-password.html'
  form_class = UserSetPasswordForm

@login_required(login_url='/accounts/login/')
def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login')

@login_required(login_url='/accounts/login/')
def password_change_done(request):
    return render(request, 'accounts/password-reset-done.html') 

@login_required(login_url='/accounts/login/')
def recover_password(request):
    return render(request,'accounts/recover-password.html')        

# Pages -- Dashboard
def dashboard(request):
    context = {
        'active_page': 'dashboard' 
    }
    return render(request, 'index.html',context)

@login_required(login_url='/accounts/login/')
def starter_template(request):
    return render(request, 'starter-template.html')

# Components
@login_required(login_url='/accounts/login/')
def avatars(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/avatars.html',context)

@login_required(login_url='/accounts/login/')
def buttons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/buttons.html',context)

@login_required(login_url='/accounts/login/')
def flaticons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/flaticons.html',context)    

@login_required(login_url='/accounts/login/')
def fontawesome(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/font-awesome-icons.html',context)

@login_required(login_url='/accounts/login/')
def simple_line_icons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/simple-line-icons.html',context)

@login_required(login_url='/accounts/login/')
def gridsystem(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/gridsystem.html',context)  

@login_required(login_url='/accounts/login/')
def panels(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/panels.html',context)

@login_required(login_url='/accounts/login/')
def notifications(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/notifications.html',context)

@login_required(login_url='/accounts/login/')
def sweetalert(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/sweetalert.html',context)

@login_required(login_url='/accounts/login/')
def typography(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/typography.html',context)


# Sidebar layouts
@login_required(login_url='/accounts/login/')
def sidebarone(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'sidebar-style-1.html',context)

@login_required(login_url='/accounts/login/')
def sidebar_overlay(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'overlay-sidebar.html',context)


@login_required(login_url='/accounts/login/')
def sidebar_compact(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'compact-sidebar.html',context)  

@login_required(login_url='/accounts/login/')
def sidebar_static(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'static-sidebar.html',context)

@login_required(login_url='/accounts/login/')
def icon_menu(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'icon-menu.html',context)


# Forms
@login_required(login_url='/accounts/login/')
def forms(request):
    context = {
        'active_page': 'forms' 
    }
    return render(request, 'forms/forms.html',context)

# Tables  
@login_required(login_url='/accounts/login/')  
def datatables(request):
    context = {
        'active_page': 'tables' 
    }
    return render(request, 'tables/datatables.html',context)

@login_required(login_url='/accounts/login/')
def tables(request):
    context = {
        'active_page': 'tables' 
    }
    return render(request, 'tables/tables.html',context)

# Charts 
@login_required(login_url='/accounts/login/') 
def charts(request):
    csv_file_path = 'firestatstique.csv'
    year_counts = Counter()

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = row['ACQ_DATE'].split('/')[0]  # Assuming 'date' is in 'YYYY-MM-DD' format
            year_counts[year] += 1

    # Préparer les données pour Chart.js
    years = list(range(2009, 2023))
    counts = [year_counts[str(year)] for year in years]

    context = {
        'active_page': 'charts',
        'years': years,
        'counts': counts,
    }

    return render(request, 'charts/charts.html', context)

import csv
from collections import Counter
from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def sparkline(request):
    context = {
        'active_page': 'charts' 
    }
    return render(request, 'charts/sparkline.html',context) 

# Maps

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
@login_required(login_url='/accounts/login/')
def maps(request):
    context = {
        'active_page': 'widgets' 
    } 
    if request.method == 'POST':
    
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        start_date = datetime.strptime(start_date, '%Y-%m-%d').strftime('%d/%m/%Y')
        end_date = datetime.strptime(end_date, '%Y-%m-%d').strftime('%d/%m/%Y')

        reponse=generation_carte_risque(request,start_date,end_date)
        #context = {
        #'active_page': 'maps' ,
        #'geometry': reponse
        #}
        if reponse:
            return render(request, 'maps/jqvmap.html')
        else:
            return render(request, 'maps/jqvmap.html')
    else:
        # Gérer la logique pour les autres méthodes HTTP si nécessaire
        #return HttpResponseNotAllowed(['POST'])
        return render(request, 'maps/jqvmap.html',context)
    

# Widgets
@login_required(login_url='/accounts/login/')
def widgets(request):
    context = {
        'active_page': 'widgets' 
    }
    return render(request, 'widgets.html',context) 
             
# data base
from django.shortcuts import render
import pandas as pd
import geopandas as gpd
from shapely import wkt
from datetime import datetime, timedelta



def get_data_static_from_api():
    url = 'https://pfedouwaf.rmrdevdz.com'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
       # diri wch thabi traitement
    else:
        return None

def get_data_temporelle_from_api(type,dateS,dateE):
    url = f'https://pfedouwaf.rmrdevdz.com/{type}/{dateS}/{dateE}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
       # diri wch thabi traitement
    else:
        return None
    
def set_geometry_from_api(donnees):
    print("dkhllt set set set set.................................................")
    url = 'https://pfedouwaf.rmrdevdz.com'
    response = requests.post(url, json=donnees)  # Utilisez json=donnees pour envoyer les données en JSON

    if response.status_code == 200:
        return response.json()
        # Ajoutez ici le traitement de la réponse si nécessaire
    else:
        return None
def get_geometry_from_api():
    url = 'https://pfedouwaf.rmrdevdz.com/geo'
    response = requests.get(url)  # Utilisez json=donnees pour envoyer les données en JSON

    if response.status_code == 200:
        return response.json()
        # Ajoutez ici le traitement de la réponse si nécessaire
    else:
        return None
''''
def constructionData(request,dateS,dateE):
    periods = [(datetime(dateS), datetime(dateE))]
    date_list = []
    for start_date, end_date in periods:
        current_date = start_date
        while current_date <= end_date:
            date_list.append(current_date)
            current_date += timedelta(days=1)

            #data static ##################

    date_df = pd.DataFrame(date_list, columns=['Date'])

    staticDataContent = get_data_static__from_api(request)
    dataStatic = pd.read_json(staticDataContent)
    dataStatic['geometry'] = dataStatic['WKT'].apply(wkt.loads)
    dataStatic = gpd.GeoDataFrame(dataStatic, geometry='geometry')
    df1 = pd.merge(dataStatic.assign(key=0), date_df.assign(key=0), on='key').drop('key', axis=1)

    #meteo data##################################

    metoeDataContent = get_data_temporelle_from_api(request,'meteo2023',dateS,dateE)

    meteoData = pd.read_json(metoeDataContent)

    df1['Date'] = pd.to_datetime(df1['Date'])
    meteoData['Date'] = pd.to_datetime(meteoData['DATE'])

    intersection = pd.merge(df1, meteoData, on='Date', how='inner')

    #indice veg ##################################
    asiDAtaContent = get_data_temporelle_from_api(request,'asi2023',dateS,dateE)
    ndviDataContent = get_data_temporelle_from_api(request,'ndvi2023',dateS,dateE)
    vhiDataContent = get_data_temporelle_from_api(request,'vhi2023',dateS,dateE)
    rainDataContent = get_data_temporelle_from_api(request,'rain2023',dateS,dateE)
    
    df1 = pd.read_csv(asiDAtaContent)
    df2 = pd.read_csv(ndviDataContent)
    df3 = pd.read_csv(vhiDataContent)
    df4 = pd.read_csv(rainDataContent)

    intersection['DATE']=pd.to_datetime(intersection['DATE'])
    df1['Date'] = pd.to_datetime(df1['Date'])
    df2['Date'] = pd.to_datetime(df2['Date'])
    df3['Date'] = pd.to_datetime(df3['Date'])
    df4['Date'] = pd.to_datetime(df4['Date'])
    
    intersection = pd.merge(intersection, df1,left_on='DATE', right_on='Date', how='inner',suffixes=('', 'a'))
    intersection = pd.merge(intersection, df2, left_on='DATE', right_on='Date', how='inner',suffixes=('', 'b'))
    intersection = pd.merge(intersection, df3,left_on='DATE', right_on='Date', how='inner',suffixes=('', 'c'))
    intersection = pd.merge(intersection, df4, left_on='DATE', right_on='Date', how='inner',suffixes=('', 'd'))
    intersection = intersection.drop_duplicates()
    # Colonnes à supprimer avec apostrophes simples
    colonnes_a_supprimer = [
    'Datea', 'Indicator', 'Country', 'ADM1_CODE', 'Province', 'Land_Type', 'Year', 'Month',
    'Dekad', 'Unit', 'Dateb', 'Indicatorb', 'Countryb', 'ADM1_CODEb', 'Provinceb', 'Land_Typeb',
    'Data_long_term_Average', 'Yearb', 'Monthb', 'Dekadb', 'Unitb', 'Datec', 'Indicatorc', 'Countryc',
    'ADM1_CODEc', 'Provincec', 'Land_Typec', 'Data_long_term_Averagec', 'Yearc', 'Monthc', 'Dekadc', 'Unitc',
    'Dated', 'Indicatord', 'Countryd', 'ADM1_CODEd', 'Provinced', 'Yeard', 'Monthd', 'Dekadd', 'Unitd','geometry','Date','TEMPERATURE_MORNING_C','TEMPERATURE_NOON_C','TEMPERATURE_EVENING_C','WEATHER_CODE_MORNING'
    ,'WEATHER_CODE_NOON','WEATHER_CODE_EVENING','SUNHOUR','OPINION','SUNSET','SUNRISE','TEMPERATURE_NIGHT_C'
]
    colonnes_a_supprimer_avec_geo = [
    'Datea', 'Indicator', 'Country', 'ADM1_CODE', 'Province', 'Land_Type', 'Year', 'Month',
    'Dekad', 'Unit', 'Dateb', 'Indicatorb', 'Countryb', 'ADM1_CODEb', 'Provinceb', 'Land_Typeb',
    'Data_long_term_Average', 'Yearb', 'Monthb', 'Dekadb', 'Unitb', 'Datec', 'Indicatorc', 'Countryc',
    'ADM1_CODEc', 'Provincec', 'Land_Typec', 'Data_long_term_Averagec', 'Yearc', 'Monthc', 'Dekadc', 'Unitc',
    'Dated', 'Indicatord', 'Countryd', 'ADM1_CODEd', 'Provinced', 'Yeard', 'Monthd', 'Dekadd', 'Unitd','Date','TEMPERATURE_MORNING_C','TEMPERATURE_NOON_C','TEMPERATURE_EVENING_C','WEATHER_CODE_MORNING'
    ,'WEATHER_CODE_NOON','WEATHER_CODE_EVENING','SUNHOUR','OPINION','SUNSET','SUNRISE','TEMPERATURE_NIGHT_C'
]

    columns_to_process = ['sand % topsoil', 'silt % topsoil', 'clay % topsoil', 'pH water topsoil',
                      'OC % topsoil', 'N % topsoil', 'BS % topsoil', 'CEC topsoil',
                      'CEC clay topsoil', 'CaCO3 % topsoil', 'BD topsoil', 'C/N topsoil']

# Remplacement des virgules par des points et conversion en float
    for col in columns_to_process:
        intersection[col] = intersection[col].str.replace(',', '.').astype(float)

# Supprimer les colonnes spécifiées
    dataSansGeo = intersection.drop(columns=colonnes_a_supprimer_avec_geo, inplace=True)

    dataAvecGeo = intersection.drop(columns=colonnes_a_supprimer_avec_geo, inplace=True)

    return {
        'dataSansGeo':dataSansGeo,
        'dataAvecGeo':dataAvecGeo
    }
    '''

def constructionData(request,dateS,dateE):
    dataAvecGeo = None
    print("******************:dkhlt construction")

        # Vérifier si le format de date est "d-m-y" et le convertir en "d/m/y"
    if '-' in dateS:
        dateS = dateS.replace('-', '/')
    if '-' in dateE:
        dateE = dateE.replace('-', '/')
    
    dateS_cp=datetime.strptime(dateS, '%d/%m/%Y')
    dateE_cp=datetime.strptime(dateE, '%d/%m/%Y')

    periods = [(dateS_cp,dateE_cp)]
    date_list = []
    for dateS, dateE in periods:
        current_date = dateS
        while current_date <= dateE:
            date_list.append(current_date)
            current_date += timedelta(days=1)

    #data static ##################

    date_df = pd.DataFrame(date_list, columns=['Date'])
    print(date_df)

    staticDataContent = get_data_static_from_api()
    dataStatic = pd.DataFrame(staticDataContent[1:],columns=staticDataContent[0])
    print(dataStatic)
    dataStatic['geometry'] = dataStatic['WKT'].apply(wkt.loads)
    dataStatic = gpd.GeoDataFrame(dataStatic, geometry='geometry')
    df1 = pd.merge(dataStatic.assign(key=0), date_df.assign(key=0), on='key').drop('key', axis=1)

    #meteo data##################################

    metoeDataContent = get_data_temporelle_from_api('meteo2023',dateS,dateE)

    meteoData = pd.DataFrame(metoeDataContent[1:],columns=metoeDataContent[0])
    print(meteoData)
    print(meteoData.columns)

    df1['Date'] = pd.to_datetime(df1['Date'])
    meteoData['Date'] = pd.to_datetime(meteoData['DATE'])

    intersection = pd.merge(df1, meteoData, on='Date', how='inner')

    #indice veg ##################################
    asiDAtaContent = get_data_temporelle_from_api('asi2023',dateS,dateE)
    ndviDataContent = get_data_temporelle_from_api('ndvi2023',dateS,dateE)
    rainDataContent = get_data_temporelle_from_api('rain2023',dateS,dateE)
    vhiDataContent = get_data_temporelle_from_api('vhi2023',dateS,dateE)
    

    df1 = pd.DataFrame(asiDAtaContent[1:],columns=asiDAtaContent[0])
    df2 = pd.DataFrame(ndviDataContent[1:],columns=ndviDataContent[0])
    df3 = pd.DataFrame(rainDataContent[1:],columns=rainDataContent[0])
    df4 = pd.DataFrame(vhiDataContent[1:],columns=vhiDataContent[0])


    intersection['DATE']=pd.to_datetime(intersection['DATE'])
    df1['Date'] = pd.to_datetime(df1['Date'])
    df2['Date'] = pd.to_datetime(df2['Date'])
    df3['Date'] = pd.to_datetime(df3['Date'])
    df4['Date'] = pd.to_datetime(df4['Date'])

    df1 = df1.drop(['Indicator', 'Country', 'ADM1_CODE', 'Province', 'Land_Type',
            'Year', 'Month', 'Dekad', 'Unit'], axis=1)

    df2 = df2.drop(['Indicator', 'Country', 'ADM1_CODE', 'Province', 'Land_Type',
            'Data_long_term_Average', 'Year', 'Month', 'Dekad', 'Unit'], axis=1)

    df3 = df3.drop(['Indicator', 'Country', 'ADM1_CODE', 'Province', 'Land_Type',
        'Data_long_term_Average', 'Year', 'Month', 'Dekad', 'Unit'], axis=1)

    df4 = df4.drop(['Indicator', 'Country', 'ADM1_CODE', 'Province', 'Year',
        'Month', 'Dekad', 'Unit'], axis=1)

    intersection = pd.merge(intersection, df1,left_on='DATE', right_on='Date', how='inner',suffixes=('', 'a'))
    intersection = pd.merge(intersection, df2, left_on='DATE', right_on='Date', how='inner',suffixes=('', 'b'))
    intersection = pd.merge(intersection, df3,left_on='DATE', right_on='Date', how='inner',suffixes=('', 'c'))
    intersection = pd.merge(intersection, df4, left_on='DATE', right_on='Date', how='inner',suffixes=('', 'd'))
    intersection = intersection.drop_duplicates()
    # Colonnes à supprimer avec apostrophes simples
   
    colonnes_a_supprimer = ['AREA','fid','geometry', 'Date','CLOUDCOVER_AVG_PERCENT'
       , 'TEMPERATURE_MORNING_C', 'TEMPERATURE_NOON_C', 'TEMPERATURE_EVENING_C',
        'WEATHER_CODE_MORNING',
       'WEATHER_CODE_NOON', 'WEATHER_CODE_EVENING', 'SUNHOUR', 'OPINION', 'SUNSET', 'SUNRISE',
       'TEMPERATURE_NIGHT_C', 'Datea',
       'Source', 'Dateb', 'Sourceb', 'Datec', 
       'Sourcec', 'Dated', 'Sourced']

    columns_to_process = ['sand % topsoil', 'silt % topsoil', 'clay % topsoil', 'pH water topsoil',
                      'OC % topsoil', 'N % topsoil', 'BS % topsoil', 'CEC topsoil',
                      'CEC clay topsoil', 'CaCO3 % topsoil', 'BD topsoil', 'C/N topsoil']

# Remplacement des virgules par des points et conversion en float
    for col in columns_to_process:
        intersection[col] = intersection[col].str.replace(',', '.').astype(float)

# Supprimer les colonnes spécifiées
    print(intersection)
    print(intersection.columns)

    dataAvecGeo = intersection.drop(columns=colonnes_a_supprimer)
    print(dataAvecGeo.columns)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    print(len(dataAvecGeo))

    return dataAvecGeo

import requests

'''
def get_geometry_from_api():
    url = 'https://pfedouwaf.rmrdevdz.com/geo'
    response = requests.get(url)  # Utilisez json=donnees pour envoyer les données en JSON

    if response.status_code == 200:
        return response.json()
        # Ajoutez ici le traitement de la réponse si nécessaire
    else:
        return None
'''

def pretraitement(request,dateS,dateE):
    print("*********************dkhlt praitratement")

        # Vérifier si le format de date est "d-m-y" et le convertir en "d/m/y"
    if '-' in dateS:
        dateS = dateS.replace('-', '/')
    if '-' in dateE:
        dateE = dateE.replace('-', '/')

    #data
    data = constructionData(request,dateS,dateE)

    data = data.drop('WKT', axis=1)
        #encodage
    code = {'21450':1,'0004 // 0003':2,'0003 / 0004':3,'21446 // 21450-121340 / 21454':4,'21518':5
            ,'21497-121340':6,'21499-121340':7,'11498':8,'21454 // 21446 // 21450':9
            ,'20049 // 20058':10,'7001 // 8001':11,'0010':12,'21496-121340 // 21497-129401':13,'21497-15045':14,'0011':15}
    data['LCCCODE'] = data['LCCCODE'].map(code)

    data['DATE'] = pd.to_datetime(data['DATE'])
    #data['Year'] = data['DATE'].dt.year
    data['Month'] = data['DATE'].dt.month
    data['Day'] = data['DATE'].dt.day
    data.drop(columns=['DATE'])
    
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    print(len(data))
    return data


#prediction part###############################################################################

import os
import joblib as jl
'''


# Liste pour stocker tous les modèles chargés


# Parcourir tous les fichiers dans le répertoire


'''
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from scipy.stats import mode
from sklearn.preprocessing import StandardScaler
import logging
logger = logging.getLogger(__name__)

def make_prediction(request,dateS,dateE):
    if request.method == 'POST':
        # Charger les données du formulaire
        data = pretraitement(request,dateS,dateE)
        print(data.columns)
        #data = data.drop(columns=['Year'])
        #print(data.columns)
        data = data.drop(columns=['DATE'])
        print(data.columns)
        # Parcourir les colonnes pour vérifier le type de chaque colonne
        for col in data.columns:
            if data[col].dtype == 'datetime64[ns]':
                print(f"La colonne '{col}' est de type 'Timestamp' ou 'datetime'.")

        liste_modeles = []
        #current_directory = os.path.dirname(__file__)  # Chemin du répertoire contenant views.py
        #chemin_repertoire = os.path.join(current_directory, 'IAmodels')
        if len(data) == 0:
            logger.error(f"No data found for date range {dateS} to {dateE}")
            raise ValueError("No data available for the given date range")
        scaler = StandardScaler()
        data = scaler.fit_transform(data)
        #for i, fichier in enumerate(os.listdir(chemin_repertoire)):
                #if fichier.endswith('.pkl'):  # Vérifiez si le fichier est un modèle (.pkl)
                    #chemin_modele = os.path.join(chemin_repertoire, f"sous_model{i}.pkl")
        modele = jl.load('static/DTmodelee.pkl')
        #liste_modeles.append(modele)

        #predictions = []
        #for model in liste_modeles:
        pred_sortie = modele.predict(data)
                #predictions.append(pred_sortie)
        return pred_sortie
    # Convertir les prédictions en un tableau numpy
        #predictions_array = np.array(predictions)

    # Calculer le mode (vote majoritaire) pour chaque tuple de données
        #VotePredictions = mode(predictions_array, axis=0)[0]



        #return VotePredictions

    

import json
from shapely import wkt
from shapely.geometry import mapping

def generation_carte_risque(request,dateS,dateE):

        print("dkhlt l genertion carte risque")
        print(dateE)
        print(dateS)

        dataAvecGeo = constructionData(request,dateS,dateE)
        dataPretraiter = pretraitement(request,dateS,dateE)
        dataPretraiter['pred'] = make_prediction(request,dateS,dateE)
            

    # Filtrer les lignes où la prédiction de l'ensemble est égale à 1
        fireprediction = dataPretraiter[dataPretraiter['pred'] == 1]

        dataPretriterPred=fireprediction.drop(columns=['pred'])

        datasansgeo = dataAvecGeo.drop('WKT', axis=1)

        code = {'21450':1,'0004 // 0003':2,'0003 / 0004':3,'21446 // 21450-121340 / 21454':4,'21518':5
            ,'21497-121340':6,'21499-121340':7,'11498':8,'21454 // 21446 // 21450':9
            ,'20049 // 20058':10,'7001 // 8001':11,'0010':12,'21496-121340 // 21497-129401':13,'21497-15045':14,'0011':15}
        datasansgeo['LCCCODE'] = datasansgeo['LCCCODE'].map(code)

        merged_df = pd.merge(datasansgeo, dataPretriterPred, how='inner', on=list(datasansgeo.columns), indicator=True)

    # Filtrer les positions des tuples de Data1 ayant une intersection avec Data2
        positions_correspondantes = merged_df[merged_df['_merge'] == 'both'].index.tolist()

    # Extraire les géométries correspondantes de Data1
        geometries_correspondantes = dataAvecGeo.iloc[positions_correspondantes]['WKT'].tolist()

    # Convertir les données WKT en GeoJSON en utilisant shapely.wkt
        geometries_geojson = []
        for wkt_str in geometries_correspondantes:
                geometry = wkt.loads(wkt_str)
                geometries_geojson.append(mapping(geometry))

    # Créer un dictionnaire avec les données GeoJSON à sauvegarder
        donnees_geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": geojson,
                        "properties": {
                            "name": "Nom de la géométrie"
                        }
                    } for geojson in geometries_geojson  
                ]
            }
        json_data = json.dumps(donnees_geojson)

    # Ajouter le préfixe personnalisé
        json_data_with_prefix = "var polygone = " + json_data

    # Écrire la chaîne résultante dans le fichier
        with open('static/donnees.geojson', 'w') as f:
            f.write(json_data_with_prefix)

        #reponse = set_geometry_from_api(donnees_geojson)
        #print(reponse)
        return  json_data_with_prefix      


# Sauvegarder les données GeoJSON dans un fichier .geojson dams le server
        #with open('/content/donnees.geojson', 'w') as f:
            #json.dump(donnees_geojson, f)
