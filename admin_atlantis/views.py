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
    context = {
        'active_page': 'charts' 
    }
    return render(request, 'charts/charts.html',context)

@login_required(login_url='/accounts/login/')
def sparkline(request):
    context = {
        'active_page': 'charts' 
    }
    return render(request, 'charts/sparkline.html',context) 

# Maps
@login_required(login_url='/accounts/login/')
def maps(request):
    context = {
        'active_page': 'maps' 
    }
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

def constructionData(request,dateS,dateE):
    periods = [(datetime(dateS), datetime(dateE))]
    date_list = []
    for start_date, end_date in periods:
        current_date = start_date
        while current_date <= end_date:
            date_list.append(current_date)
            current_date += timedelta(days=1)

    date_df = pd.DataFrame(date_list, columns=['Date'])

    file_path = 'C:/Users/Dell/Downloads/dataBaseStaticc.csv'
    polygons_df = pd.read_csv(file_path)
    polygons_df['geometry'] = polygons_df['WKT'].apply(wkt.loads)
    polygons_df = gpd.GeoDataFrame(polygons_df, geometry='geometry')
    df1 = pd.merge(polygons_df.assign(key=0), date_df.assign(key=0), on='key').drop('key', axis=1)

    df2 = pd.read_csv('C:/Users/Dell/Downloads/meteo2023.csv')

    df1['Date'] = pd.to_datetime(df1['Date'])
    df2['Date'] = pd.to_datetime(df2['DATE'])

    intersection = pd.merge(df1, df2, on='Date', how='inner')
    
    df1 = pd.read_csv('C:/Users/Dell/Downloads/asiimodifier.csv')
    df2 = pd.read_csv('C:/Users/Dell/Downloads/ndvimodifier.csv')
    df3 = pd.read_csv('C:/Users/Dell/Downloads/rainmodifier.csv')
    df4 = pd.read_csv('C:/Users/Dell/Downloads/vhimodifier.csv')
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

# Supprimer les colonnes spécifiées
    intersection.drop(columns=colonnes_a_supprimer, inplace=True)

    context = {
        'active_page': 'dataBase',
        'intersection': intersection
    }
    return render(request, 'dataBase/dataBase.html', context)
#predection
@login_required(login_url='/accounts/login/')
def predection(request):
    context = {
        'active_page': 'Predection' 
    }
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        # Faites quelque chose avec la valeur récupérée, comme l'afficher
        print("Date sélectionnée :", startDate)
        endDate = request.POST.get('endDate')
        # Faites quelque chose avec la valeur récupérée, comme l'afficher
        print("Date sélectionnée :", endDate)
        constructionData(request,startDate,endDate)
        return render(request, 'dataBase/Predection.html',context)  
    else:
        # Gérer la méthode GET (ou autre) si nécessaire
        return render(request, 'dataBase/Predection.html',context)  
    
      