import selenium
import sys # to permit the exit of the app (sys.exit)
import time # to permit the pause : time.sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ---------------------------- Lancement du navigateur et connection au site :----------------------------

# importation des drivers pour le navigateur 
driver = webdriver.Edge(executable_path=r'C:\Users\makoo\Downloads\MicrosoftWebDriver') # to open the edge browser

# specification du site web à visiter
driver.get("your_website");
# agrandir la fenêtre
driver.maximize_window();
# temps d'attente avant d'executer la prochaine instruction (chargement du site)
time.sleep(2)
# sélection de l'élément sur la page et clic sur cette élément (connection field)
driver.find_element_by_xpath("//input[@id='user_login']").send_keys("your_user"); # send le login
time.sleep(1) # temps de pause 1 sec
driver.find_element_by_xpath("//input[@id='user_pass']").send_keys("your_pass"); # send le pass
driver.find_element_by_xpath("//input[@id='wp-submit']").click();

#----------------------------------------------- CHOIX -----------------------------------------------

# Fonctions des choix : 
def physique():
    driver.find_element_by_xpath("//a[@href='https://www.cours.jlrichter.fr/lycee/premiere-s/']").click()
    # input pour la partie sécurisée
    choice2 = input("Voulez vous accéder à la partie sécurisée ? (Y or N) ")
    if choice2 == "Y" or choice2 == "y":
        driver.find_element_by_xpath("//a[@href='https://www.cours.jlrichter.fr/lycee/premiere-s/mon-annee-de-1e-s/']").click()
    else:
        driver.back()
        menu()


def nsi():
    driver.find_element_by_xpath("//a[@href='https://www.cours.jlrichter.fr/lycee/1e-nsi/']").click()
    # input pour la partie sécurisée
    choice2 = input("Voulez vous accedéder à la partie sécurisée ? (Y or N) ")
    if choice2 == "Y" or choice2 == "y":
        driver.find_element_by_xpath("//a[@href='https://www.cours.jlrichter.fr/lycee/1e-nsi/mon-annee-de-1e-nsi/']").click()
        menu()    
    else:
        driver.back()
        menu()

# Fonction du menu :
def menu():
    print("********MENU PRINCIPAL**********")
    print()

    choice = input("""
                A: Physique Chimie
                B: NSI
                C: Sortir du programme

                Veuillez entrer votre choix : """)

    if choice == "A" or choice =="a":
        physique()
    elif choice == "B" or choice =="b":
        nsi()
    elif choice == "C" or choice =="c": 
        driver.close()
        sys.exit()


menu()
