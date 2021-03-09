import tkinter as tk
import json
import requests

MAIN_FONT = "Terminal"
BUTTON_FONT_SIZE = 10
window_x = 600
window_y = 800


def StartWindow():
    global startWindow
    global mainWindow
    global summonerString
    global APIString
    global errorMessage

    #WINDOW SETTINGS
    startWindow = tk.Tk()
    startWindow.geometry('600x240')
    startWindow.resizable(False, False)
    startWindow.configure(background='gray12')
    startWindow.title("League Account Grabber")

    summonerString = tk.StringVar(startWindow)
    APIString = tk.StringVar(startWindow)
    errorMessage = ""
    #TK ELEMENTS
    title = tk.Label(text="League Of Legends Account Grabber 2.0", font=(MAIN_FONT, 22), bg="gray11", fg="white").pack(padx=2, pady=2)
    subtitle = tk.Label(text="By: Finn", font=(MAIN_FONT, 15), bg="gray11", fg="white").pack(padx=2, pady=2)

    summonerNameTitle = tk.Label(text="Summoner Name", font=(MAIN_FONT, 14), bg="gray11", fg="orange", width=32).pack(padx=2, pady=1)
    inputSummonerName = tk.Entry(font=(MAIN_FONT, 20), width=20, textvariable=summonerString).pack(pady=5)

    apiKeyTitle = tk.Label(text="API Key", font=(MAIN_FONT, 14), bg="gray11", fg="orange", width=32).pack(padx=2, pady=1)
    inputAPI = tk.Entry(font=(MAIN_FONT, 20), width=20, textvariable=APIString).pack(pady=5)

    confirmButton = tk.Button(text="Confirm", font=(MAIN_FONT, 13), width=15,command=MainWindow).pack(padx=5, pady=5)

    # MAIN LOOP
    startWindow.mainloop()

def MainWindow():
    global startWindow
    global mainWindow
    global summonerString
    global APIString

    global accountName
    global accountSummonerLevel
    global accountId
    global encryptedId
    global accountPuuid

    global SpectatorGame
    global ChampionListMasterys
    global ChampionList
    global MatchHistory
    global RankedInfo

    summonerName = summonerString.get()
    APIKey = APIString.get()

    def parse(link):
        jsonlink = requests.get(link)
        parseinfo = jsonlink.json()
        return parseinfo



    # ACCOUNT INFORMATION
    # Get Account Info
    accountInfo = parse(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}')
    accountId = accountInfo['accountId']
    encryptedId = accountInfo['id']
    accountPuuid = accountInfo['puuid']
    accountName = accountInfo['name']
    accountSummonerLevel = accountInfo['summonerLevel']

    # CHAMPION MASTERYS
    championMasterys = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')

    # JSON DATA FROM API
    SpectatorGame = parse(f'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encryptedId}?api_key={APIKey}')
    ChampionList = parse(f'http://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion.json')
    ChampRot = parse(f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}')
    ChampMastery = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
    ChampionListMasterys = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
    Gamemodes = parse(f'http://static.developer.riotgames.com/docs/lol/gameModes.json')
    RankedInfo = parse(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedId}?api_key={APIKey}')
    MatchHistory = parse(f'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={APIKey}')

    startWindow.destroy()

    # MAIN WINDOW Settings
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
    getCurrentGameInfo = tk.Button(text="Current Game Info", font=(MAIN_FONT, BUTTON_FONT_SIZE),width=18, height=2, command=CurrentGameInfo).pack(in_=top_buttonlayer,side=tk.LEFT,padx=1, pady=2)
    getMasteryInfo = tk.Button(text="Masterys", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2, command=ChampionMasterys).pack(in_=top_buttonlayer, side=tk.LEFT, padx=1, pady=2)
    getRankedInfo = tk.Button(text="Ranked Info", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2, command=GetRankedInfo).pack(in_=top_buttonlayer, side=tk.RIGHT,padx=1, pady=2)
    getMatchHistory = tk.Button(text="Match History", font=(MAIN_FONT, BUTTON_FONT_SIZE),width=18, height=2, command=GameHistory).pack(in_=top_buttonlayer, side=tk.RIGHT, padx=1,pady=2)
    logout = tk.Button(text="Log Out", font=(MAIN_FONT, BUTTON_FONT_SIZE), width=18, height=2, command=Logout).pack(in_=middle_buttonlayer, side=tk.RIGHT, padx=1, pady=2)

    mainWindow.mainloop()

def reset_all():
    global mainFrame
    global mainWindow


    mainFrame.destroy()
    mainFrame = tk.Frame(mainWindow)
    mainFrame = tk.Frame(mainWindow, bg="gray11")
    mainFrame.pack()

def Logout():
    global mainWindow
    mainWindow.destroy()
    StartWindow()

def AccountInfo():
    # Globals
    global mainFrame
    global mainWindow

    global accountName
    global accountSummonerLevel
    global accountId
    global encryptedId
    global accountPuuid

    # RESETS WINDOW
    reset_all()

    # TK Elements
    accountInfo = tk.Label(mainFrame,text="Account Info", font=(MAIN_FONT, 24), bg="gray15", fg="white", width=45).pack(padx=2, pady=3)
    summonerName = tk.Label(mainFrame,text=accountName, font=(MAIN_FONT, 22), fg="firebrick1", bg="gray14", width=22).pack(padx=2, pady=3)
    summonerLevel = tk.Label(mainFrame, text=f"Summoner Level: {accountSummonerLevel}", font=(MAIN_FONT, 15), width=22, fg="goldenrod1", bg="gray12").pack(padx=2, pady=3)
    summonerID = tk.Label(mainFrame, text=f"Account ID: {accountId}", font=(MAIN_FONT, 11), width=60, fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)
    encryptedID = tk.Label(mainFrame, text=f"Encrypted ID: {encryptedId}", font=(MAIN_FONT, 11), width=60,fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)
    puuid = tk.Label(mainFrame, text=f"PUUID: {accountPuuid}", font=(MAIN_FONT, 7), width=90,fg="SpringGreen2", bg="gray12").pack(padx=2, pady=3)

def ChampionMasterys():
    # Globals
    global mainFrame
    global mainWindow

    global ChampionListMasterys
    global ChampionList

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Champion Masterys", font=(MAIN_FONT, 24), bg="gray15", fg="white",width=45).pack(padx=2, pady=3)

    # League Champion Mastery Data
    for items in ChampionListMasterys:
        # Convert Champion Id's into Champ Name
        for x in items:
            if x.lower() == 'championid':
                for y in ChampionList['data']:
                    if items[x] == int(ChampionList['data'][y]['key']):
                        items[x] = ChampionList['data'][y]['name']

        tk.Label(mainFrame, text=f"Champion: {items['championId']}", font=(MAIN_FONT, 10), bg="gray12", fg="CadetBlue1").pack(pady=2)

def CurrentGameInfo():
    # Globals
    global mainFrame
    global mainWindow
    global SpectatorGame

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Game Info", font=(MAIN_FONT, 24), bg="gray15", fg="white",width=45).pack(padx=2, pady=3)

    try:
        gameID = tk.Label(mainFrame, text=f"Game ID: {SpectatorGame['gameId']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown2",width=40).pack(padx=2, pady=1)
        mapID = tk.Label(mainFrame, text=f"Map ID: {SpectatorGame['mapId']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown3",width=40).pack(padx=2, pady=1)
        gamemode = tk.Label(mainFrame, text=f"Gamemode: {SpectatorGame['gameMode']}", font=(MAIN_FONT, 10), bg="gray14", fg="brown3",width=40).pack(padx=2, pady=1)
        gametype = tk.Label(mainFrame, text=f"Game Type: {SpectatorGame['gameType']}", font=(MAIN_FONT, 10),bg="gray14", fg="brown3", width=40).pack(padx=2, pady=1)
        gameTimer = tk.Label(mainFrame, text=f"Game Length: {round((SpectatorGame['gameLength'] / 60) + 3)} Min (WIP)", font=(MAIN_FONT, 10),bg="gray14", fg="brown3", width=40).pack(padx=2, pady=1)

        tk.Label(mainFrame, text=f"Players In Game", font=(MAIN_FONT, 15), bg="gray14",fg="wheat2", width=150).pack(padx=2, pady=3)

        # TEAM 1
        player1 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][0]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player2 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][1]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player3 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][2]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player4 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][3]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)
        player4 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][4]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="SteelBlue2").pack(padx=2,pady=2)

        # TEAM 2
        player5 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][5]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player6 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][6]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player7 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][7]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player8 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][8]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
        player9 = tk.Label(mainFrame, text=f"{SpectatorGame['participants'][9]['summonerName']}", font=(MAIN_FONT, 11), bg="gray14", fg="IndianRed1").pack(padx=2,pady=2)
    except:
        tk.Label(mainFrame, text="No Game Found (Is Player In Game?)", font=(MAIN_FONT, 20), bg="gray15", fg="red").pack(padx=2, pady=4)

def GetRankedInfo():
    # Globals
    global mainFrame
    global mainWindow
    global RankedInfo

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Ranked Information", font=(MAIN_FONT, 24), bg="gray15", fg="white",width=45).pack(padx=2, pady=3)
    rankColor = "white"

    if RankedInfo[0]['tier'] == 'iron':
        rankColor = 'gray56'
    elif RankedInfo[0]['tier'] == 'bronze':
        rankColor = 'goldenrod3'
    elif RankedInfo[0]['tier'] == 'silver':
        rankColor = 'azure2'
    elif RankedInfo[0]['tier'] == 'gold':
        rankColor = 'gold'
    elif RankedInfo[0]['tier'] == 'platinum':
        rankColor = 'DarkSeaGreen1'
    elif RankedInfo[0]['tier'] == 'diamond':
        rankColor = 'turquoise1'
    elif RankedInfo[0]['tier'] == 'master':
        rankColor = 'azure2'
    else:
        rankColor = 'DarkSlateGray1'

    newPlayer = tk.Label(mainFrame, text=f"Queue Type: {RankedInfo[0]['queueType']}", font=(MAIN_FONT, 16), bg="gray14", fg="white").pack(padx=2, pady=2)
    rank = tk.Label(mainFrame, text=f"{RankedInfo[0]['tier']} {RankedInfo[0]['rank']}", font=(MAIN_FONT, 20), bg="gray14", fg=rankColor).pack(padx=2,pady=2)
    wins = tk.Label(mainFrame, text=f"Wins: {RankedInfo[0]['wins']}", font=(MAIN_FONT, 15), bg="gray14", fg="green").pack(padx=2, pady=2)
    losses = tk.Label(mainFrame, text=f"Losses: {RankedInfo[0]['losses']}", font=(MAIN_FONT, 15), bg="gray14", fg="red").pack(padx=2, pady=2)
    streak = tk.Label(mainFrame, text=f"On A Roll?: {RankedInfo[0]['hotStreak']}", font=(MAIN_FONT, 15), bg="gray14", fg="white").pack(padx=2, pady=2)
    newPlayer = tk.Label(mainFrame, text=f"New Player?: {RankedInfo[0]['freshBlood']}", font=(MAIN_FONT, 15), bg="gray14", fg="white").pack(padx=2, pady=2)

def GameHistory():
    # Globals
    global mainFrame
    global mainWindow
    global MatchHistory

    # RESETS WINDOW
    reset_all()

    # TK Elements
    title = tk.Label(mainFrame, text="Game History", font=(MAIN_FONT, 22), bg="gray12", fg="white",width=45).pack(padx=2, pady=3)

    for items in MatchHistory['matches']:
        tk.Label(mainFrame, text=f"Champion ID: {items['champion']} | {items['role']} | Lane: {items['lane']}", font=(MAIN_FONT, 14), bg="gray14", fg="tomato", width=50).pack(pady=2)

# INIT Start Window
StartWindow()