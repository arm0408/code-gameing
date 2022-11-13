import json
import GameData
def score_board():
    with open('text.json','r') as sb:
        sc_data = json.load(sb)
        sorted_sc_data = sorted(sc_data, key=lambda d: d['score'], reverse=True)
        print('================================================================================')
        print('\t\t!!Score board!!')
        for i in range(5):
            print(sorted_sc_data[i]['user'],'\t\t\t\t',sorted_sc_data[i]['score'])
        print('================================================================================')
