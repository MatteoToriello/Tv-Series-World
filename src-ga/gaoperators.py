import random
import pandas as pd

keywords=["fight", "enemy", "zombie", "superhero", "criminal", "killer", "monster",
          "vampire", "vigilante", "drug", "war", "hero", "police", "werewolf", "story",
          "anthology", "battle", "century", "supernatural", "angel", "dark", "demon",
          "actor","young", "princess", "magic", "samurai", "thief", "diabolic",
          "crime", "murder", "american", "dream", "detective", "supervillain",
          "villain", "italian", "secret", "space", "blood", "lycan", "teen",
          "wolf", "love", "hate", "future", "travel"]
consiglia_genre=dict()
import random
import pandas as pd
import time

keywords=["fight", "enemy", "zombie", "superhero", "criminal", "killer", "monster",
          "vampire", "vigilante", "drug", "war", "hero", "police", "werewolf", "story",
          "anthology", "battle", "century", "supernatural", "angel", "dark", "demon",
          "actor","young", "princess", "magic", "samurai", "thief", "diabolic",
          "crime", "murder", "american", "dream", "detective", "supervillain",
          "villain", "italian", "secret", "space", "blood", "lycan", "teen",
          "wolf", "love", "hate", "future", "travel", "ninja", "china", "japan"]
consiglia_genre=dict()
consiglia_genre["Adventure"]=["Fantasy", "Sci-Fi", "Action", "Thriller"]
consiglia_genre["Drama"]=["Crime", "Thriller"]
consiglia_genre["Horror"]=["Thriller", "Mistery", "Crime"]
consiglia_genre["Romance"]=["Animation", "Family", "Music", "Musical"]
consiglia_genre["Fantasy"]=["Action", "Mistery", "Thriller", "Adventure"]
consiglia_genre["Crime"]=["Drama", "Thriller", "Mistery"]
consiglia_genre["Sci-Fi"]=["Adventure", "Mistery"]
consiglia_genre["Mystery"]=["Thriller", "Fantasy", "Crime"]
consiglia_genre["Comedy"]=["Family", "Talk-Show", "Animation"]
consiglia_genre["Action"]=["Adventure","War", "Western"]
consiglia_genre["Family"]=["Comedy", "Documentary", "Talk-Show",
                           "Sport", "Music", "Musical", "Romance", "Animation"]
consiglia_genre["Short"]=["News", "Animation", "Sport", "Game-Show", "Reality-TV"]
consiglia_genre["News"]=["Biography", "Documentary", "Family", "History"]
consiglia_genre["Biography"]=["History", "Documentary"]
consiglia_genre["History"]=["Biography", "Documentary"]
consiglia_genre["Thriller"]=["Horror", "Drama", "Crime"]
consiglia_genre["Talk-Show"]=["Comedy", "Short", "Game-Show", "Reality-TV"]
consiglia_genre["Sport"]=["Game-Show", "Short"]
consiglia_genre["Music"]=["Musical", "Animation", "Romance"]
consiglia_genre["War"]=["Action", "History"]
consiglia_genre["Western"]=["Action", "History"]
consiglia_genre["Game-Show"]=["Talk-Show", "Sport", "Reality-TV"]
consiglia_genre["Reality-TV"]=["Talk-Show", "Comedy"]
consiglia_genre["Musical"]=["Music", "Animation", "Family"]
consiglia_genre["Documentary"]=["History", "Biography"]
consiglia_genre["Animation"]=["Music","Family", "Fantasy", "Musical"]
tempo=time.time()



def carica_serie_utente(lista_serie):
    to_return=[]
    generi=[]
    inp=""
    while inp!="esci":
        inp=input('''Dimmi una serie tv:
                  Scrivi esci per smettere di inserire serie ''')
        inp=inp.lower()
        aggiungi=cerca_serie(lista_serie, inp)
        if aggiungi in to_return:
            print("Serie già selezionata")
        elif aggiungi!=None:
            to_return.append(aggiungi)
            generi_aggiungi=aggiungi[4].split(", ")
            if generi_aggiungi[0] not in generi:
                generi.append(generi_aggiungi[0])
            if generi_aggiungi[1] not in generi:
                generi.append(generi_aggiungi[1])
            if generi_aggiungi[-1] not in generi:
                generi.append(generi_aggiungi[-1])
        elif aggiungi==None:
            if inp=="esci":
                break
            print("Serie non trovata...")
    return to_return, generi

def cerca_serie(lista_serie, inp):
    
    for i in range(len(lista_serie.Series_Title)):
        if lista_serie.Series_Title[i].lower()==inp:
            aggiungi=[lista_serie.Series_Title[i], lista_serie.Runtime_of_Series[i], lista_serie.Certificate[i], lista_serie.Runtime_of_Episodes[i], lista_serie.Genre[i], lista_serie.IMDB_Rating[i], lista_serie.Star1[i], lista_serie.Star2[i], lista_serie.Overview[i]]
            
            return aggiungi
        
    return None


def caricamentoDati():
    dat= pd.read_csv("series_data.csv")
    return dat

def prepara_dataset(lista_serie, generi):
    data_pronto=[]
    for i in range(len(lista_serie)):
        genre=lista_serie.Genre[i].split(", ")
        if genre[0] in generi:
            data_pronto.append([lista_serie.Series_Title[i], lista_serie.Runtime_of_Series[i], lista_serie.Certificate[i], lista_serie.Runtime_of_Episodes[i], lista_serie.Genre[i], lista_serie.IMDB_Rating[i], lista_serie.Star1[i], lista_serie.Star2[i], lista_serie.Overview[i]])
        elif len(genre)>1:
            if genre[1] in generi:
                data_pronto.append([lista_serie.Series_Title[i], lista_serie.Runtime_of_Series[i], lista_serie.Certificate[i], lista_serie.Runtime_of_Episodes[i], lista_serie.Genre[i], lista_serie.IMDB_Rating[i], lista_serie.Star1[i], lista_serie.Star2[i], lista_serie.Overview[i]])
            elif len(genre)==3:
                if genre[2] in generi:
                    data_pronto.append([lista_serie.Series_Title[i], lista_serie.Runtime_of_Series[i], lista_serie.Certificate[i], lista_serie.Runtime_of_Episodes[i], lista_serie.Genre[i], lista_serie.IMDB_Rating[i], lista_serie.Star1[i], lista_serie.Star2[i], lista_serie.Overview[i]])        
    return data_pronto

def inizializza(lista_serie, lista_utente):
    lunghezza=random.randrange(3,15)
    n=0
    lista=[]
    lista_non_codificata=[]
    lista_codificata=[]
    while n<lunghezza:
        preso=0
        i=random.randint(0, len(lista_serie)-1)
        for j in lista_utente:
            if lista_serie[i][0]==j[0]:
                preso=1
        if preso==1:
            continue
        lista_non_codificata.append(lista_serie[i])
        lista.append(lista_serie[i])
        n+=1
    lista_codificata=codifica(lista)
    return lista_non_codificata, lista_codificata
        

def codifica(lista):
    to_return=[]
    for i in range(len(lista)):
        contenitore=[]
        for j in range(len(lista)):
            contenitore.append(random.randint(0,1))

        to_return.append(contenitore)
    return to_return

def fitness(lista_utente, lista_non_codificata, lista_codificata):
    lista_fit=[]
    global keywords
    for z in range(len(lista_codificata)):
        fit=0
        for i in range(len(lista_non_codificata)):
            first=False
            if lista_codificata[z][i]!=0:
                for j in range(len(lista_utente)):
                    if lista_non_codificata[i][5]>=lista_utente[j][5] and first==False:
                                    fit+=0.3
                                    first=True
                    for k in keywords:
                        if k in lista_non_codificata[i][-1].lower() and k in lista_utente[j][-1].lower():
                            fit+=0.5
                    genere_consiglio=lista_non_codificata[i][4].split(", ")
                    genere_utente=lista_utente[j][4].split(", ")
                    for x in genere_consiglio:
                        for y in genere_utente:
                            if x not in consiglia_genre[y]:
                                fit=0
        lista_fit.append([lista_codificata[z], fit])
    return lista_fit



def take_second(elem):
    return elem[1]

def twoTournament(lista_fit):
    to_return=[]
    a=[]
    for j in range(len(lista_fit)):
        if len(lista_fit)>1:
            a=random.choices(lista_fit, k=2)
            if a[0] in lista_fit:
                lista_fit.remove(a[0])
            if a[1] in lista_fit:
                lista_fit.remove(a[1])
            a=sorted(a, key=take_second)
            to_return.append(a[-1][0])
        elif len(lista_fit)==1:
            to_return.append(lista_fit[0][0])
            break
    return to_return


def crossover(math_pool):
    lista_crossover=math_pool
    to_return=[]
    val=[0,1]
    prob=[.2,.8]
    for i in range(0,len(lista_crossover),2):
        cross_prob=random.choices(val, prob)
        
        if cross_prob[0]==1:
            if i+1<=len(lista_crossover)-1:
                taglio=random.randint(1, len(lista_crossover[i]))
                to_return.append(lista_crossover[i][0:taglio]+lista_crossover[i+1][taglio:len(lista_crossover[i+1])])
                to_return.append(lista_crossover[i+1][0:taglio]+lista_crossover[i][taglio:len(lista_crossover[i])])
    return to_return

def mutation_inv(lista_codificata):
    val=[0,1]
    prob=[.99, .01]
    for i in range(len(lista_codificata)):
        inversion_prob=random.choices(val,prob)
        if inversion_prob==1:
            iniz=random.randint(0, len(lista_codificata))
            var=iniz+1
            fin=random.randint(var, len(lista_codificata))
            for j in range(iniz, fin):
                if lista_codificata[i][j]==1:
                    lista_codificata[i][j]=0
                else:
                    lista_codificata[i][j]=1
        
            
     
    return lista_codificata

def stop(lista_fit):
    global tempo
    if len(lista_fit)<=2 or time.time()-tempo>0.5:
        return True
    else:
        return False
    
    

def stampa_result(lista_utente, lista_non_codificata, codifica_finale):
    for i in lista_utente:
        print(i[:-1])
        print("\n")
    for i in range(len(codifica_finale)):
        if codifica_finale[i]==1:
            print(lista_non_codificata[i])
    return "Spero che queste serie siano di tuo gradimento! A presto!"

def trova_result(lista_fit):
    massimo=lista_fit[0][1]
    best=lista_fit[0][0]
    for i in range(len(lista_fit)):
        if massimo<=lista_fit[i][1]:
            massimo=lista_fit[i][1]
            best=lista_fit[i][0]
    return best
