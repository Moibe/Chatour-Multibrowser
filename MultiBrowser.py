# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:36:52 2021

@author: Moibe
"""

from nordvpn_switcher import initialize_VPN,rotate_VPN
from selenium import webdriver
from selenium.webdriver.common.by import By    
import time

url = 'https://chaturbate.com/missbellary/'
a = {}
browsers = 50
print("Por entrar...")

#initialize_VPN(save=1,area_input=['complete rotation'])

for i in range(browsers) : 
    
    try: 
        #rotate_VPN()
        for g in range(1,4):
            
            indice = g*i
            
            print("Lanzando browser")
            a[indice]=webdriver.Chrome() 
            print("Obteniendo URL.")
            a[indice].get(url)
            time.sleep(4)
            #Hacemos click en el botón de acepto.
            botonElement = a[i].find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/a[2]")           
            botonElement.click()
            
            a[indice].minimize_window()
            print(indice)
            x = len(a)
            print("Éste es el lenght de a:")
            print(x)

    
    except IndexError as e:
           time.sleep(2)
           print("Llegamos a un except.")
           print(e)
           
          
           
           for i in range(browsers) : 
    
            try: 
                print("Cerrando browser")
                print(i)
                a[i].close()
               
         
            except IndexError as e:
                   time.sleep(2)
                   print("Llegamos a un except del cierre.")
                   print(e)
                   
            print("Terminamos con todo el proceso via error, gracias.")
          
            
print("Todos los browsers listos...")
print("Esperemos 60 segundos...")
time.sleep(120)
print("Inicia el cierre de los browsers.")

for i in range(browsers) : 
    
    try: 
        print("Cerrando browser")
        print(i)
        a[i].close()
       
 
    except IndexError as e:
           time.sleep(2)
           print("Llegamos a un except del cierre.")
           print(e)
           
print("Terminamos con todo el proceso, gracias.")



