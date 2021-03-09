import tkinter as tk
import LeagueApp.APIRequest as leagueAPI

MAIN_FONT = "Terminal"
BUTTON_FONT_SIZE = 10

window_x = 600
window_y = 800

def StartWindow():
    global startWindow
    global mainWindow

    #WINDOW SETTINGS
    startWindow = tk.Tk()
    startWindow.geometry(f"{window_x}x{window_y}")
    startWindow.resizable(False, False)
    startWindow.configure(background='gray12')
    startWindow.title("League Account Grabber")

    #TK ELEMENTS
    title = tk.Label(text="League Of Legends Account Grabber 2.0", font=(MAIN_FONT, 22)).pack(padx=2, pady=2)
    subtitle = tk.Label(text="By: Finn", font=(MAIN_FONT, 17)).pack(padx=2, pady=2)
    inputSummonerName = tk.Entry(font=(MAIN_FONT, 20)).pack(pady=5)
    inputAPI = tk.Entry(font=(MAIN_FONT, 20)).pack(pady=5)
    confirmButton = tk.Button(text="Confirm", font=(MAIN_FONT, 13), command=MainWindow).pack(padx=5, pady=5)

    # MAIN LOOP
    startWindow.mainloop()

def MainWindow():
    global startWindow
    global mainWindow

    startWindow.destroy()

    mainWindow = tk.Tk()
    mainWindow.geometry(f"{window_x}x{window_y}")
    mainWindow.resizable(False, False)
    mainWindow.configure(background='gray11')
    mainWindow.title("League Account Grabber")

    global top_buttonlayer
    top_buttonlayer = tk.Frame(mainWindow, bg="gray13")
    top_buttonlayer.pack(side=tk.BOTTOM, fill=tk.BOTH)

    middle_buttonlayer = tk.Frame(mainWindow, bg="gray13")
    middle_buttonlayer.pack(side=tk.BOTTOM, fill=tk.BOTH)

    global mainFrame
    mainFrame = tk.Frame(mainWindow, bg="gray11")
    mainFrame.pack()

    # BUTTONS
    getCurrentGameInfo = tk.Button(text="Current Game Info", font=(MAIN_FONT, BUTTON_FONT_SIZE),width=18, height=2, command=CurrentGameInfo).pack(in_=top_buttonlayer,side=tk.LEFT,padx=2, pady=2)
    getMasteryInfo = tk.Button(text="Masterys", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2, command=ChampionMasterys).pack(in_=top_buttonlayer, side=tk.LEFT, padx=2, pady=2)
    getFreeChampionRotations = tk.Button(text="Free Champs", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2).pack(in_=top_buttonlayer, side=tk.RIGHT,padx=2, pady=2)
    getAccountInfo = tk.Button(text="Account Info", font=(MAIN_FONT, BUTTON_FONT_SIZE),width=18, height=2, command=AccountInfo).pack(in_=top_buttonlayer, side=tk.RIGHT, padx=2,pady=2)
    logout = tk.Button(text="Log Out", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2).pack(in_=middle_buttonlayer, side=tk.RIGHT, padx=2, pady=2)

    mainWindow.mainloop()

def reset_all():
    global mainFrame
    global mainWindow


    mainFrame.destroy()
    mainFrame = tk.Frame(mainWindow)
    mainFrame = tk.Frame(mainWindow, bg="gray11")
    mainFrame.pack()

def AccountInfo():
    # Globals
    global mainFrame
    global mainWindow

    # RESETS WINDOW
    reset_all()

    # TK Elements
    accountInfo = tk.Label(mainFrame,text="Account Info", font=(MAIN_FONT, 24), bg="gray15", fg="white", width=45).pack(padx=2, pady=3)
    summonerName = tk.Label(mainFrame,text=leagueAPI.accountName, font=(MAIN_FONT, 22), fg="firebrick1", bg="gray14", width=22).pack(padx=2, pady=3)
    summonerLevel = tk.Label(mainFrame, text=f"Summoner Level: {leagueAPI.accountSummonerLevel}", font=(MAIN_FONT, 15), width=22, fg="goldenrod1", bg="gray12").pack(padx=2, pady=3)
    summonerID = tk.Label(mainFrame, text=f"Account ID: {leagueAPI.accountId}", font=(MAIN_FONT, 11), width=60, fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)
    encryptedID = tk.Label(mainFrame, text=f"Encrypted ID: {leagueAPI.encryptedId}", font=(MAIN_FONT, 11), width=60,fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)
    puuid = tk.Label(mainFrame, text=f"PUUID: {leagueAPI.accountPuuid}", font=(MAIN_FONT, 7), width=90,fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)

def ChampionMasterys():
    # Globals
    global mainFrame
    global mainWindow

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Champion Masterys", font=(MAIN_FONT, 24), bg="gray15", fg="white",width=45).pack(padx=2, pady=3)

    # League Champion Mastery Data
    for items in leagueAPI.ChampionListMasterys:
        # Convert Champion Id's into Champ Name
        for x in items:
            if x.lower() == 'championid':
                for y in leagueAPI.ChampionList['data']:
                    if items[x] == int(leagueAPI.ChampionList['data'][y]['key']):
                        items[x] = leagueAPI.ChampionList['data'][y]['name']

        tk.Label(mainFrame, text=f"Champion: {items['championId']}", font=(MAIN_FONT, 10), bg="gray12", fg="CadetBlue1").pack(pady=2)


def CurrentGameInfo():
    # Globals
    global mainFrame
    global mainWindow
    global window_y

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Game Info", font=(MAIN_FONT, 24), bg="gray15", fg="white",width=45).pack(padx=2, pady=3)

    try:
        gameID = tk.Label(mainFrame, text=f"Game ID: {leagueAPI.SpectatorGame['gameId']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown2",width=40).pack(padx=2, pady=1)
        mapID = tk.Label(mainFrame, text=f"Map ID: {leagueAPI.SpectatorGame['mapId']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown3",width=40).pack(padx=2, pady=1)
        gamemode = tk.Label(mainFrame, text=f"Map ID: {leagueAPI.SpectatorGame['gameMode']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown3",width=40).pack(padx=2, pady=1)
        gametype = tk.Label(mainFrame, text=f"Map ID: {leagueAPI.SpectatorGame['gameType']}", font=(MAIN_FONT, 10),bg="gray14", fg="brown3", width=40).pack(padx=2, pady=1)

        tk.Label(mainFrame, text=f"Players In Game", font=(MAIN_FONT, 15), bg="gray14",fg="wheat2", width=150).pack(padx=2, pady=3)

        # TEAM 1
        player1 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][0]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player2 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][1]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player3 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][2]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player4 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][3]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player4 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][4]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)

        # TEAM 2
        player5 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][5]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player6 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][6]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player7 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][7]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player8 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][8]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player9 = tk.Label(mainFrame, text=f"{leagueAPI.SpectatorGame['participants'][9]['summonerName']}", font=(MAIN_FONT, 10), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
    except:
        tk.Label(mainFrame, text="No Game Found (Is Player In Game?)", font=(MAIN_FONT, 20), bg="gray15", fg="red").pack(padx=2, pady=4)

# INIT Start Window
StartWindow()