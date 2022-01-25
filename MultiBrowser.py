# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:36:52 2021

@author: Moibe
"""

from nordvpn_switcher import initialize_VPN,rotate_VPN
from selenium import webdriver
from selenium.webdriver.common.by import By    
from selenium.common.exceptions import NoSuchElementException  
import time
from random import randint

def check_exists_by_xpath(xpath, driver):
    try:
       driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
            return False
    return True

url = 'https://chaturbate.com/shmoopiebebz_/'
a = {}
browsers = 50
print("Por entrar...")

for i in range(browsers):
    
        azar = randint(1,5)
        print("Obtuvimos...")
        print(azar)
        if azar == 5: 
            print("Cambiaremos de red porque salió 5...")
            rotate_VPN()
    
       
        print("i es igual a...")
        print(i)
        

        print("Lanzando browser")
        a[i]=webdriver.Chrome() 
        print("Obteniendo URL.")
        a[i].get(url)
        
        print("Entramos a la URL")
        #Dale tiempo a que renderee.
        time.sleep(2)
        
        try: 
            
            if check_exists_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[2]", a[i]) is True:
                #Hacemos click en el botón de acepto.
                botonElement = a[i].find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/a[2]").click() 
                print("Elemento encontrado...")
            
            else:
                print("EL ELEMENTO NO EXISTE PQ NOS FUIMOS A UN CAPTCHA...")
                time.sleep(randint(4,18))
                print("Vamos a buscar el captcha.")
                time.sleep(1)
                captcha = a[i].find_element(By.CLASS_NAME, "challenge-form interactive-form").click()
        
        except IndexError as e:
            time.sleep(2)
            print("Llegamos a un except.")
            print(e)
        
# =============================================================================
#         
# =============================================================================
        

        


#initialize_VPN(save=1,area_input=['complete rotation'])

# =============================================================================
# for i in range(browsers) : 
#     
#     try: 
#         #rotate_VPN()
#         for g in range(1,4):
#             
#             indice = g*i
#             
#             print("Lanzando browser")
#             a[indice]=webdriver.Chrome() 
#             print("Obteniendo URL.")
#             a[indice].get(url)
#             time.sleep(2)
#             #Hacemos click en el botón de acepto.
#             # botonElement = a[i].find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/a[2]")   
#             
#             print("Ahora le vamos a dar click a ACEPTO.")
#             #botonElement = a[i].find_element_by_id('close_entrance_terms')
#             if a[i].find_element(By.LINK_TEXT, "ACEPTO") == True:
#                 print("Es TRrue")
#             #botonElement.click()
#             print("Ya le dimos click a ACEPTO!...")
#             
#             a[indice].minimize_window()
#             print(indice)
#             x = len(a)
#             print("Éste es el lenght de a:")
#             print(x)
# 
#     
#     except IndexError as e:
#            time.sleep(2)
#            print("Llegamos a un except.")
#            print(e)
#            
#           
#            
#            for i in range(browsers) : 
#     
#             try: 
#                 print("Cerrando browser")
#                 print(i)
#                 a[i].close()
#                
#          
#             except IndexError as e:
#                    time.sleep(2)
#                    print("Llegamos a un except del cierre.")
#                    print(e)
#                    
#             print("Terminamos con todo el proceso via error, gracias.")
#           
#             
# print("Todos los browsers listos...")
# print("Esperemos 60 segundos...")
# time.sleep(120)
# print("Inicia el cierre de los browsers.")
# 
# for i in range(browsers) : 
#     
#     try: 
#         print("Cerrando browser")
#         print(i)
#         a[i].close()
#        
#  
#     except IndexError as e:
#            time.sleep(2)
#            print("Llegamos a un except del cierre.")
#            print(e)
#            
# print("Terminamos con todo el proceso, gracias.")
# 
# 
# =============================================================================

