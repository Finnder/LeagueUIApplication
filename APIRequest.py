import json
import requests

summonerName = "scarra"
APIKey = "RGAPI-040826b6-7186-4c2d-9b49-5037713b4f62"

def parse(link):
    jsonlink = requests.get(link)
    parseinfo = jsonlink.json()
    return parseinfo

accountInfo = parse(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}')

#ACCOUNT INFORMATION
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

print(SpectatorGame)