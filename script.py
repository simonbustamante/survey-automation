import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




for _ in range(10):  # Repetir 300 veces
    # Iniciar el driver
    driver = webdriver.Chrome(executable_path='C:/Users/sbustamante/OneDrive - MIC/Documents/UIP/SCRIPT/chromedriver.exe')

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf_16Ywoof_xAjuQ7zjHzXkOdk1DF9cfCzcz8eQ0m3j5lW7pQ/viewform')

    # Rellenar el formulario
    # Localizar el bloque que contiene la pregunta "¿Cuántos años tienes?"
    sleep(random.random() * 5)

    #bloque_pregunta = driver.find_element(By.XPATH, '//*[@id="i1"]/span[1]/p')
    
    #print("HOLA")
    
    # Lista de opciones XPath

    # 1. ¿Cuántos años tienes?
    options_xpath1 = [
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i11"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i14"]/div[3]/div',
        '//*[@id="i17"]/div[3]/div'
    ]
    # 2.       ¿Cuál es tu género?
    options_xpath2 = [
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div'
    ]

    # 3.       ¿Cuánto tiempo has estado empleado/a en tu trabajo actual?
    options_xpath3 = [
        '//*[@id="i37"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i43"]/div[3]/div',
        '//*[@id="i43"]/div[3]/div',
        '//*[@id="i43"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div'
    ]

    option_next1 = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

    # 4.       ¿Has experimentado frustraciones significativas en tu trabajo actual?
    options_xpath4 = [
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div'
    ]
    # 5.       Si tu respuesta fue sí, ¿cuál de las siguientes frustraciones has experimentado? (Selecciona todas las que apliquen)
    options_xpath5 = [
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i33"]/div[3]/div',
        '//*[@id="i36"]/div[3]/div',
        '//*[@id="i39"]/div[3]/div'
    ]

    # 6.       ¿Cómo respondiste a estas frustraciones laborales?
    options_xpath6 = [
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i46"]/div[3]/div',
        '//*[@id="i49"]/div[3]/div',
        '//*[@id="i52"]/div[3]/div',
        '//*[@id="i55"]/div[3]/div'
    ]

    option_next2 = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'
    
    # 7.       ¿Crees que tus frustraciones laborales han contribuido a tu crecimiento personal?

    options_xpath7 = [
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i5"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div',
        '//*[@id="i8"]/div[3]/div'
    ]  

    # 8.       Si la respuesta fue sí, ¿de qué manera(s) crees que estas frustraciones te han ayudado a crecer personalmente? (Seleccione todas las que apliquen) 
    options_xpath8 = [
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i15"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i21"]/div[3]/div',
        '//*[@id="i24"]/div[3]/div',
        '//*[@id="i27"]/div[3]/div',
        '//*[@id="i30"]/div[3]/div',
        
        
    ] 

    # 9.       ¿Has buscado ayuda profesional (por ejemplo, un coach, un mentor, un psicólogo) para lidiar con tus frustraciones laborales y fomentar tu crecimiento personal?

    options_xpath9 = [
        '//*[@id="i37"]/div[3]/div',
        '//*[@id="i37"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div'
    ]  

    # 10.       En una escala de 1 a 10, (Donde 1 es poco y 10 mucho) ¿cuánto crees que has crecido personalmente como resultado de tus experiencias laborales (incluyendo las frustraciones)?

    options_xpath10 = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div'
    ] 

    # 11.	¿Hay algo más que te gustaría agregar sobre cómo las frustraciones laborales han impactado tu crecimiento personal?
    
    comentarios = [""
        #"Creo que las frustraciones laborales me han ayudado a ser más resiliente. Con el tiempo, he aprendido a ver cada desafío como una oportunidad de crecimiento y no como un obstáculo insuperable",
        #"Las frustraciones que he experimentado en el trabajo me han permitido descubrir áreas de mejora en mis habilidades profesionales y personales. En cierto sentido, me han guiado en mi desarrollo personal",
        #"A pesar de que las frustraciones en el trabajo pueden ser desalentadoras, me he dado cuenta de que a veces son necesarias para empujarnos fuera de nuestra zona de confort y motivarnos a superarnos",
        #"Al principio, las frustraciones laborales me afectaron negativamente. Sin embargo, con el tiempo, aprendí a manejarlas y utilizarlas como una motivación para mejorar y crecer como persona y profesional",
        #"Las frustraciones laborales han sido una especie de señal de alerta para mí, indicándome que algo debe cambiar en mi vida, ya sea en la forma en que trabajo o en la forma en que manejo mis relaciones con mis colegas",
        #"Aunque no es fácil admitirlo, creo que las frustraciones laborales han sido necesarias para mi crecimiento personal. Me han obligado a enfrentar mis miedos, mejorar mi capacidad de comunicación y ser más asertivo",
        #"Las frustraciones laborales me han permitido identificar y establecer límites en mi vida laboral. Aprendí a equilibrar mejor mi trabajo y mi vida personal, lo cual es esencial para mi bienestar",
        #"En retrospectiva, las frustraciones laborales me han enseñado mucho sobre la importancia de la adaptabilidad y la paciencia. Ahora soy más resistente a los cambios y me recupero más rápidamente de los contratiempos",
        #"Gracias a las frustraciones laborales, he descubierto la importancia de la autoreflección y la autoevaluación. Me han hecho preguntarme: ¿qué puedo aprender de esto? ¿Cómo puedo mejorar? Esto ha sido muy beneficioso para mi crecimiento personal",
        #"Las frustraciones en el trabajo, aunque desafiantes, me han ayudado a entender que el fracaso no es el fin, sino un paso en el camino hacia el éxito. Me han enseñado a ver las dificultades como oportunidades para aprender y crecer",
        #"Creo que enfrentar frustraciones en el trabajo es parte de la vida profesional. Estos desafíos me han hecho más fuerte, más comprensivo y más capaz de manejar la adversidad. Veo estas experiencias como oportunidades de aprendizaje valiosas que han contribuido a mi crecimiento personal"
    ]

    option_send = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span'

    # Seleccionar aleatoriamente una opción XPath
    random_xpath1 = random.choice(options_xpath1)
    random_xpath2 = random.choice(options_xpath2)
    random_xpath3 = random.choice(options_xpath3)
    random_xpath4 = random.choice(options_xpath4)
    random_xpath5 = random.choice(options_xpath5)
    random_xpath6 = random.choice(options_xpath6)
    random_xpath7 = random.choice(options_xpath7)
    random_xpath8 = random.choice(options_xpath8)
    random_xpath9 = random.choice(options_xpath9)
    random_xpath10 = random.choice(options_xpath10)
    xpath11 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea'

    
    # Hacer clic en la opción seleccionada
    option1 = driver.find_element_by_xpath(random_xpath1)
    sleep(random.random() * 5)
    option1.click()
    option2 = driver.find_element_by_xpath(random_xpath2)
    sleep(random.random() * 5)
    option2.click()
    option3 = driver.find_element_by_xpath(random_xpath3)
    sleep(random.random() * 5)
    option3.click()
    next1 = driver.find_element_by_xpath(option_next1)
    sleep(random.random() * 5)
    next1.click()
    option4 = driver.find_element_by_xpath(random_xpath4)
    sleep(random.random() * 5)
    option4.click()
    if random_xpath4 == '//*[@id="i5"]/div[3]/div':
        option5 = driver.find_element_by_xpath(random_xpath5)
        sleep(random.random() * 5)
        option5.click()  
    sleep(random.random() * 5) 
    option6 = driver.find_element_by_xpath(random_xpath6)
    sleep(random.random() * 5)
    option6.click()

    next2 = driver.find_element_by_xpath(option_next2)
    sleep(random.random() * 5)
    next2.click()
    
    option7 = driver.find_element_by_xpath(random_xpath7)
    sleep(random.random() * 5)
    option7.click()
    sleep(random.random() * 5)

    if random_xpath7 == '//*[@id="i5"]/div[3]/div':
        option8 = driver.find_element_by_xpath(random_xpath8)
        sleep(random.random() * 5)
        option8.click() 


    sleep(random.random() * 5)
    option9 = driver.find_element_by_xpath(random_xpath9)
    sleep(random.random() * 5)
    option9.click()
    
    sleep(random.random() * 5)
    option10 = driver.find_element_by_xpath(random_xpath10)
    sleep(random.random() * 5)
    option10.click()

    sleep(random.random() * 5)
    option11 = driver.find_element_by_xpath(xpath11)
    sleep(random.random() * 5)
    option11.send_keys(comentarios[0])
    
    sleep(random.random() * 5)
    send = driver.find_element_by_xpath(option_send)
    sleep(random.random() * 5)
    send.click()
    sleep(random.random() * 5)
    # Cerrar el driver
    driver.quit()
    

