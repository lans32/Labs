from random import randint
import os
#from time import time
#open("Results.txt","w").close()
results = [""]*10
while True:
    #ntime = time()
    # - open memory
    try:
        file = open("memory.txt","r")
        lie = file.readlines()
        file.close()
    except:
        open("memory.txt","w").close()
        lie = []
    
    try:
        file = open("memory2.txt","r")
        lie2 = file.readlines()
        file.close()
    except:
        open("memory2.txt","w").close()
        lie2 = []
    
    field = ["000","000","000"]
    def in_field(x,y,symbol):
        global field
        field[y] = field[y][:x]+symbol+field[y][x+1:]
    
    turns = []
    turns2 = []
    turn = 0
    end = 0
    
    while end != 1:
        if end == 0:
            nlies = []
            nbest = ["00",0]
            best_num = 0
            for i in range(0,len(lie2),5):
                find = 1
                for c in range(3):
                    if lie2[i+c][:-1] != field[c]:
                        find = 0
                
                if find == 1:
                    try:
                        if nbest[1] < int(lie2[i+4]):
                            nbest = [lie2[i+3][:-1],int(lie2[i+4])]
                            best_num = i+4
                        nlies += [[lie2[i+3][:-1],int(lie2[i+4]),i+4]]
                    except:
                        if nbest[1] < int(lie2[i+4][:-1]):
                            nbest = [lie2[i+3][:-1],int(lie2[i+4][:-1])]
                            best_num = i+4
                        nlies += [[lie2[i+3][:-1],int(lie2[i+4][:-1]),i+4]]
            
            if nbest[1] > 50:
                in_field(int(nbest[0][0]),int(nbest[0][1]),"1")
                turns2 += [best_num]
            else:
                if len(nlies) < 9-turn*2:
                    # - random "0"
                    num = randint(1,9-turn*2)
                    nnum = 0
                    for i in range(3):
                        for c in range(3):
                            if field[i][c] == "0":
                                nnum += 1
                            if nnum == num:
                                nx = c
                                ny = i
                                nnum += 1
                    find = -1
                    for i in range(len(nlies)):
                        if nlies[i][0] == str(nx)+str(ny):
                            find = i
                            
                    if find == -1: # - if turn is unique
                        # - write in memory
                        file = open("memory2.txt","a")
                        file.write(field[0]+"\n"+field[1]+"\n"+field[2]+"\n"+str(nx)+str(ny)+"\n50\n")
                        file.close()
                        file = open("memory2.txt","r")
                        lie2 = file.readlines()
                        file.close()
                        turns2 += [len(lie2)-1]
                    else:
                        turns2 += [nlies[find][2]]
                    in_field(nx,ny,"1")
                else:
                    best_nlies = []
                    for i in range(len(nlies)):
                        if nlies[i][1] == nbest[1]:
                            best_nlies += [nlies[i]]
                    if len(best_nlies)-1 != 0:
                        num = randint(0,len(best_nlies)-1)
                    else:
                        num = 0
                    in_field(int(best_nlies[num][0][0]),int(best_nlies[num][0][1]),"1")
                    turns2 += [best_nlies[num][2]]
            
        if field[0] == "111" or field[1] == "111" or field[2] == "111" or (field[0][0] == "1" and field[1][0] == "1" and field[2][0] == "1") or (field[0][1] == "1" and field[1][1] == "1" and field[2][1] == "1") or (field[0][2] == "1" and field[1][2] == "1" and field[2][2] == "1")  or  (field[0][0] == "1" and field[1][1] == "1" and field[2][2] == "1") or (field[0][2] == "1" and field[1][1] == "1" and field[2][0] == "1"):
            file = open("memory.txt","r")
            lie = file.readlines()
            file.close()
            for i in range(len(turns)):
                if i != len(turns)-1:
                    if int(lie[turns[i]]) != 1:
                        lie[turns[i]] = str(int(lie[turns[i]])-1)+"\n"
                else:
                    lie[turns[i]] = "0\n"
            file = open("memory.txt","w")
            for i in range(len(lie)):
                file.write(lie[i])
            file.close()
            turns = []
            
            file = open("memory2.txt","r")
            lie2 = file.readlines()
            file.close()
            for i in range(len(turns2)):
                if i != len(turns2)-1:
                    if int(lie2[turns2[i]]) != 99:
                        lie2[turns2[i]] = str(int(lie2[turns2[i]])+1)+"\n"
                else:
                    lie2[turns2[i]] = "100\n"
            file = open("memory2.txt","w")
            for i in range(len(lie2)):
                file.write(lie2[i])
            file.close()
            turns2 = []
            turn = -1
            results = ["FIRST WIN"]+results[:-1]
            #file = open("Results.txt","a")
            #file.write("FIRST\n")
            #file.close()
            end = 1
        
        if turn == 4 and end == 0:
            file = open("memory.txt","r")
            lie = file.readlines()
            file.close()
            for i in range(len(turns)):
                if int(lie[turns[i]]) != 99:
                    lie[turns[i]] = str(int(lie[turns[i]])+1)+"\n"
                    
            file = open("memory.txt","w")
            for i in range(len(lie)):
                file.write(lie[i])
            file.close()
            turns = []
            
            file = open("memory2.txt","r")
            lie2 = file.readlines()
            file.close()
            for i in range(len(turns2)):
                if i != len(turns2)-1:
                    if int(lie2[turns2[i]]) != 1:
                        lie2[turns2[i]] = str(int(lie2[turns2[i]])-1)+"\n"
            
            file = open("memory2.txt","w")
            for i in range(len(lie2)):
                file.write(lie2[i])
            file.close()
            turns2 = []        
            turn = -1
            results = ["DRAFT"]+results[:-1]
            #file = open("Results.txt","a")
            #file.write("DRAFT\n")
            #file.close()
            end = 1
        
        if end == 0:
            nlies = []
            nbest = ["00",0]
            best_num = 0
            for i in range(0,len(lie),5):
                find = 1
                for c in range(3):
                    if lie[i+c][:-1] != field[c]:
                        find = 0
                
                if find == 1:
                    try:
                        if nbest[1] < int(lie[i+4]):
                            nbest = [lie[i+3][:-1],int(lie[i+4])]
                            best_num = i+4
                        nlies += [[lie[i+3][:-1],int(lie[i+4]),i+4]]
                    except:
                        if nbest[1] < int(lie[i+4][:-1]):
                            nbest = [lie[i+3][:-1],int(lie[i+4][:-1])]
                            best_num = i+4
                        nlies += [[lie[i+3][:-1],int(lie[i+4][:-1]),i+4]]
            
            if nbest[1] > 50:
                in_field(int(nbest[0][0]),int(nbest[0][1]),"2")
                turns += [best_num]
            else:
                if len(nlies) < 8-turn*2:
                    # - random "0"
                    num = randint(1,8-turn*2)
                    nnum = 0
                    for i in range(3):
                        for c in range(3):
                            if field[i][c] == "0":
                                nnum += 1
                            if nnum == num:
                                nx = c
                                ny = i
                                nnum += 1
                    find = -1
                    for i in range(len(nlies)):
                        if nlies[i][0] == str(nx)+str(ny):
                            find = i
                            
                    if find == -1: # - if turn is unique
                        # - write in memory
                        file = open("memory.txt","a")
                        file.write(field[0]+"\n"+field[1]+"\n"+field[2]+"\n"+str(nx)+str(ny)+"\n50\n")
                        file.close()
                        file = open("memory.txt","r")
                        lie = file.readlines()
                        file.close()
                        turns += [len(lie)-1]
                    else:
                        turns += [nlies[find][2]]
                    in_field(nx,ny,"2")
                else:
                    best_nlies = []
                    for i in range(len(nlies)):
                        if nlies[i][1] == nbest[1]:
                            best_nlies += [nlies[i]]
                    if len(best_nlies)-1 != 0:
                        num = randint(0,len(best_nlies)-1)
                    else:
                        num = 0
                    in_field(int(best_nlies[num][0][0]),int(best_nlies[num][0][1]),"2")
                    turns += [best_nlies[num][2]]
            
            if field[0] == "222" or field[1] == "222" or field[2] == "222" or (field[0][0] == "2" and field[1][0] == "2" and field[2][0] == "2") or (field[0][1] == "2" and field[1][1] == "2" and field[2][1] == "2") or (field[0][2] == "2" and field[1][2] == "2" and field[2][2] == "2")  or  (field[0][0] == "2" and field[1][1] == "2" and field[2][2] == "2") or (field[0][2] == "2" and field[1][1] == "2" and field[2][0] == "2"):
                file = open("memory.txt","r")
                lie = file.readlines()
                file.close()
                for i in range(len(turns)):
                    if i != len(turns)-1:
                        if int(lie[turns[i]]) != 99:
                            lie[turns[i]] = str(int(lie[turns[i]])+1)+"\n"
                    else:
                        lie[turns[i]] = "100\n"
                file = open("memory.txt","w")
                for i in range(len(lie)):
                    file.write(lie[i])
                file.close()
                
                file = open("memory2.txt","r")
                lie2 = file.readlines()
                file.close()
                for i in range(len(turns2)):
                    if i != len(turns2)-1:
                        if int(lie2[turns2[i]]) != 1:
                            lie2[turns2[i]] = str(int(lie2[turns2[i]])-1)+"\n"
                    else:
                        lie2[turns2[i]] = "0\n"
                file = open("memory2.txt","w")
                for i in range(len(lie2)):
                    file.write(lie2[i])
                file.close()
                turns2 = []            
                turns = []
                turn = -1
                results = ["SECOND WIN"]+results[:-1]
                end = 1
                #file = open("Results.txt","a")
                #file.write("SECOND\n")
                #file.close()
        turn += 1
    os.system("cls")
    print("__________")
    for i in range(len(results)):
        print(results[i])
    #print(str((time()-ntime)//0.01*0.01))