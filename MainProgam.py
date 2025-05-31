import os
import pyfiglet
# from TampilkanMenu.MenuASN import PanelAparat
# from TampilkanMenu.MenuAdmin import PanelAdmin
# from TampilkanMenu.MenuKades import PanelKades
# from FormLogin.LoginAdmin import LoginAdmin
# from FormLogin.LoginASN import LoginAparat
# from FormLogin.LoginKades import LoginKades 
# from db.DBKon import koneksi as conn
from FormLogin.LoginAwal import LOGIN

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Selamat Datang di SIMANDESA"))
    LOGIN()
main()