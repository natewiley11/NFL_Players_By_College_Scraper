#!/usr/bin/env python3

#author : Nathaniel Wiley

'''
    *********************************
        RUN FROM TERMINAL OR CMD
    *********************************
'''

from __future__ import print_function
import sys
import subprocess
import pkg_resources


#install missing libraries
required = {'bs4' , 'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import bs4 as bs
import urllib.request
import re
import string
import sys
import json
import pathlib
import datetime
import colorama
from colorama import Fore
from colorama import Style
from addingPlayersFunc import addPlayersFromCollege

def getListOfPlayers(letter):
    if letter == 'a':
        link = 'http://www.espn.com/nfl/college'
    else:
        link = 'http://www.espn.com/nfl/college/_/letter/'+letter.lower()
        
    req = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(req, 'html.parser')
    
    colleges = {}
    players = []
    player_info = ()
    table_row = soup.find('tr')
    college_name = table_row.find('td').text
    page_complete = True
    
    while page_complete:
        if table_row['class'] == ['stathead']:
            if table_row.find('td').text != college_name: 
                colleges[college_name] = players
                players = []
                college_name = table_row.find('td').text
            college_name = table_row.find('td').text
        elif table_row['class'] == ['colhead']:
            pass
            #skip because just headings
        else:
            children = table_row.find_all('a')
            position = table_row.find_all('td')
            if table_row.find('td').text != 'No active players.':
                player_info = (children[0].text , children[1].text , position[2].text)
                players.append(player_info)   
        
        
        #get next row
        table_row = table_row.next_sibling
       
        if table_row == None:
            page_complete = False
            colleges[college_name] = players
            players = []
    return colleges

def updatePlayers():
    alphabet = list(string.ascii_lowercase)
    complete_colleges_list = {}
    print('Loading...')
    for letter in alphabet:
        letter_data = getListOfPlayers(letter)
        for college in letter_data:
            #moving individual letter data to the grand dict
            complete_colleges_list[college] = letter_data[college]
            
    with open("players.json", "w") as outfile: 
        json.dump(complete_colleges_list, outfile)

def getPlayers():
    players_json_file = open('players.json')
    complete_colleges_list = json.load(players_json_file)
    players_json_file.close()

    return complete_colleges_list
    
def getRatings():
    with open('allRatingsFinal.csv', 'r') as data:
        ratings = {}

        #removing duplicate ratings for the same player
        for row in data:
            player = row.split(',')
            if player[5] == 'ovr':
                continue
            if player[1] not in ratings:
                ratings[player[1]] = int(player[5])
    return ratings

def getFileDate():
    fname = pathlib.Path('players.json')
    if not fname.exists():
        return
    last_update = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
    print('Last update :',last_update.strftime("%b %d %Y"))


def pretty_print(complete_colleges_list , college , ratings):
    colorama.init()
    for player in complete_colleges_list[college]:
        print(Fore.BLUE,'-'*78,Style.RESET_ALL)
        #create scraper to determine if relevant player, rating > 80
        try:
            if ratings[player[0]] > 80:
                print(Style.BRIGHT, Fore.RED,' '*2,player[0],
                                      ' '*(20-len(player[0])),' | '
                                      ,player[1],' '*(20-len(player[1])),' | '
                                      ,player[2],'[',ratings[player[0]],']'
                                      , Style.RESET_ALL)
            else:
                print(' '*4,player[0], ' '*(20-len(player[0])),
                      ' | ',player[1], ' '*(20-len(player[1])),' | ',player[2])
        except:
            print(' '*4,player[0], ' '*(20-len(player[0])),
                      ' | ',player[1], ' '*(20-len(player[1])),' | ',player[2])

def main():
    getFileDate()
    #update player data user decision
    if input('Update (y/n) ? ').lower() == 'y':
        print('Updating player data...')
        updatePlayers()
        
    #get player data from json file
    try:
        complete_colleges_list = getPlayers()
    except:
        print('Run update players function before trying to access data')

    #get Madden 21 final ratings data from csv file
    ratings = getRatings()

    team ={}
    for t in complete_colleges_list:
        team = addPlayersFromCollege(complete_colleges_list, t, team, ratings)
    for i in sorted (team.keys()) : 
        print(i,team[i])
    #main loop 
    while True:
        college = input('\nCollege (q to quit) : ')
        if college in complete_colleges_list:
            pretty_print(complete_colleges_list , college , ratings)
        elif college == 'q':
            sys.exit()
        else:
            print('College invalid')

if __name__=='__main__':
    main()

