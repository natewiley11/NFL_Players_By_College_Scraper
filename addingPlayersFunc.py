


def addPlayersFromCollege(complete_colleges_list, college, team, ratings):
    for player in complete_colleges_list[college]:
        #player[2] = position of player
        #player[0] = player name
        try:
            if ratings[player[0]] > 80:
                
                #WR
                if player[2] == 'Wide Receiver':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    elif player[2]+' 3' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 3'] = (player[0],ratings[player[0]])
                    else:
                        #321
                        if team[player[2]+' 3'][1] < team[player[2]+' 2'][1] < team[player[2]][1] :
                            if team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        #231
                        elif team[player[2]+' 2'][1] < team[player[2]+' 3'][1] < team[player[2]][1] :
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        #132
                        elif team[player[2]][1] < team[player[2]+' 3'][1] < team[player[2]+' 2'][1] :
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                        #123
                        elif team[player[2]][1] < team[player[2]+' 2'][1] < team[player[2]+' 3'][1] :
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                        #312
                        elif team[player[2]+' 3'][1] < team[player[2]][1] < team[player[2]+' 2'][1] :
                            if team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                        #213
                        elif team[player[2]+' 2'][1] < team[player[2]][1] < team[player[2]+' 3'][1] :
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                    
                #RB
                elif player[2] == 'Running Back':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                
                #OT
                elif player[2] == 'Offensive Tackle':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])    
                #G
                elif player[2] == 'Guard':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])

                #DE
                elif player[2] == 'Defensive End':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])

                #DT
                elif player[2] == 'Defensive Tackle':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            

                #CB
                elif player[2] == 'Cornerback':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    elif player[2]+' 3' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 3'] = (player[0],ratings[player[0]])
                    else:
                        #321
                        if team[player[2]+' 3'][1] < team[player[2]+' 2'][1] < team[player[2]][1] :
                            if team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        #231
                        elif team[player[2]+' 2'][1] < team[player[2]+' 3'][1] < team[player[2]][1] :
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        #132
                        elif team[player[2]][1] < team[player[2]+' 3'][1] < team[player[2]+' 2'][1] :
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                        #123
                        elif team[player[2]][1] < team[player[2]+' 2'][1] < team[player[2]+' 3'][1] :
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                        #312
                        elif team[player[2]+' 3'][1] < team[player[2]][1] < team[player[2]+' 2'][1] :
                            if team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                        #213
                        elif team[player[2]+' 2'][1] < team[player[2]][1] < team[player[2]+' 3'][1] :
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 3'][1] < ratings[player[0]]:
                                team[player[2]+' 3'] = (player[0],ratings[player[0]])

                #S
                elif player[2] == 'Safety':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])

                #LB
                elif player[2] == 'Linebacker':
                    if player[2] not in team:
                        #add immediate
                        team[player[2]] = (player[0],ratings[player[0]])
                    elif player[2]+' 2' not in team:
                        #add immediate because no player 2
                        team[player[2]+' 2'] = (player[0],ratings[player[0]])
                    else:
                        if team[player[2]+' 2'][1] < team[player[2]][1]:
                            if team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])
                            elif team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                        else:
                            if team[player[2]][1] < ratings[player[0]]:
                                team[player[2]] = (player[0],ratings[player[0]])
                            elif team[player[2]+' 2'][1] < ratings[player[0]]:
                                team[player[2]+' 2'] = (player[0],ratings[player[0]])

                #others with one position
                elif player[2] in team:
                    if team[player[2]][1] < ratings[player[0]]:
                        team[player[2]] = (player[0],ratings[player[0]])
                elif player[2] not in team:
                    team[player[2]] = (player[0],ratings[player[0]])
                else:
                    print('?')
                    print(player[2])
                
        except:
            pass #player not good enough to get a rating
    return team
