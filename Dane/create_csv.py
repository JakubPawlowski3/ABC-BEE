import pandas as pd
import numpy as np



# producenci=np.array([[100,250,313],[125,231,120],[200,121,425]])
# klienci=np.array([[230,120,205],[425,200,200],[110,100,100]])
# cena=np.array([[4,4,2],[3,2,2],[3,3,1]])
# dystans = np.array([[100, 120, 65], [80, 45, 18], [55, 25, 35]])

# producenci = np.array([[74 ,79 ,52 ,66 ,59 ,69 ,76 ,28 ,44 ,53 ,75 ,77 ,58 ,41 ,22 ,36],
# [43 ,75 ,80 ,54 ,69 ,62 ,72 ,49 ,33 ,36 ,76 ,38 ,71 ,65 ,21 ,56],
# [27 ,43 ,78 ,42 ,23 ,49 ,34 ,51 ,53 ,42 ,58 ,35 ,30 ,26 ,39 ,73],
# [37 ,63 ,73 ,22 ,71 ,68 ,71 ,26 ,77 ,44 ,49 ,80 ,47 ,37 ,58 ,76],
# [47 ,65 ,33 ,32 ,56 ,28 ,47 ,70 ,31 ,56 ,79 ,50 ,68 ,28 ,34 ,32],
# [39 ,55 ,74 ,32 ,32 ,78 ,38 ,47 ,73 ,78 ,22 ,66 ,54 ,70 ,33 ,44],
# [68 ,69 ,27 ,70 ,77 ,62 ,55 ,35 ,49 ,44 ,48 ,44 ,26 ,63 ,28 ,65],
# [48 ,75 ,38 ,66 ,69 ,74 ,63 ,47 ,32 ,68 ,55 ,64 ,48 ,80 ,66 ,50],
# [40 ,60 ,21 ,51 ,25 ,48 ,53 ,33 ,26 ,40 ,34 ,49 ,34 ,38 ,53 ,37],
# [32 ,74 ,55 ,71 ,45 ,74 ,42 ,73 ,68 ,40 ,23 ,67 ,45 ,52 ,27 ,49],
# [58 ,23 ,21 ,60 ,58 ,45 ,39 ,66 ,48 ,59 ,57 ,59 ,27 ,77 ,62 ,70],
# [62 ,70 ,50 ,78 ,26 ,53 ,44 ,54 ,79 ,38 ,75 ,41 ,77 ,35 ,61 ,25],
# [48 ,54 ,46 ,56 ,77 ,56 ,55 ,53 ,52 ,27 ,67 ,53 ,60 ,28 ,72 ,25],
# [74 ,65 ,61 ,79 ,74 ,34 ,78 ,32 ,46 ,32 ,26 ,21 ,71 ,39 ,55 ,69],
# [48 ,21 ,59 ,22 ,24 ,25 ,79 ,80 ,21 ,62 ,68 ,27 ,37 ,53 ,63 ,37],
# [37, 75, 42, 46, 51, 73, 72, 28, 29, 39, 41, 66, 34, 29, 32, 37]])

# klienci = np.array([[13 ,20 , 6 ,20 ,20 , 5 ,12 ,16 ,18 ,16 ,17 ,13 ,12 , 9 ,16 , 5],
# [10 , 9 ,18 ,10 ,19 ,16 , 5 ,14 , 9 ,15 , 7 ,15 ,20 ,18 ,11 , 8],
# [15 ,16 ,18 ,11 ,15 ,12 , 7 ,12 ,16 ,11 ,12 ,19 ,11 ,15 , 7 , 5],
# [11 ,20 , 9 ,15 ,11 ,16 ,16 ,14 ,13 , 6 ,15 , 5 ,19 ,10 , 5 ,20],
# [10 ,12 ,20 ,12 , 8 ,20 ,14 ,12 ,17 ,12 ,18 ,12 ,20 , 9 ,13 ,17],
# [20 ,18 ,11 , 5 ,10 ,14 ,18 ,19 ,17 ,12 ,16 ,10 ,16 , 5 , 8 ,10],
# [18 ,18 ,15 ,11 ,15 ,14 ,14 ,19 ,17 ,20 ,13 , 7 ,14 , 5 ,16 ,19],
# [15 , 7 ,12 ,13 ,10 ,20 ,18 ,13 , 7 , 6 ,12 , 9 ,11 ,14 , 9 ,17],
# [18 ,20 , 7 ,16 ,17 ,11 , 8 , 9 , 7 ,15 ,11 ,15 ,18 , 7 ,20 ,11],
# [19 ,11 ,15 ,17 , 5 ,13 ,12 ,15 ,11 ,19 ,13 ,10 , 9 ,19 ,18 ,11],
# [8 ,20 ,14 ,18 , 7 ,10 ,11 , 5 ,14 ,10 , 6 ,18 ,13 ,14 , 6 ,13],
# [15 , 6 ,18 ,13 ,10 ,16 ,13 ,16 , 8 , 7 ,15 ,11 ,13 ,16 ,12 ,17],
# [19 , 9 ,15 ,12 ,15 ,11 ,12 , 7 ,10 ,16 ,11 ,12 , 5 ,15 ,15 , 6],
#  [7 ,13 ,11 ,17 ,10 ,14 ,16 ,20 , 5 ,15 ,17 ,11 , 7 ,17 ,17 ,16],
#  [9 ,10 ,13 , 6 , 8 ,11 , 5 ,19 ,13 ,18 ,20 ,10 , 6 ,16 ,14 ,11],
# [12 , 7 ,11 , 5 ,16 ,11 ,10 ,10 , 6 ,20 ,17 , 6 , 5 ,16 , 7 , 5]])


# ceny = np.array([[5 ,3 ,9 ,1 ,9 ,0 ,8 ,3 ,7 ,0 ,3 ,3 ,2 ,5 ,5 ,7],
# [3 ,0 ,7 ,7 ,4 ,6 ,7 ,8 ,7 ,8 ,0 ,9 ,4 ,5 ,3 ,0],
# [0 ,1 ,0 ,4 ,0 ,7 ,6 ,8 ,2 ,1 ,2 ,5 ,4 ,0 ,4 ,7],
# [7 ,5 ,0 ,4 ,7 ,6 ,3 ,7 ,4 ,3 ,3 ,0 ,4 ,3 ,0 ,2],
# [3 ,7 ,4 ,9 ,1 ,4 ,1 ,2 ,3 ,7 ,4 ,0 ,5 ,8 ,6 ,3],
# [5 ,5 ,5 ,0 ,9 ,6 ,0 ,1 ,4 ,8 ,5 ,7 ,4 ,9 ,5 ,0],
# [8 ,9 ,5 ,9 ,1 ,7 ,7 ,8 ,1 ,0 ,5 ,3 ,3 ,9 ,7 ,6],
# [7 ,5 ,0 ,6 ,0 ,6 ,6 ,1 ,4 ,4 ,4 ,7 ,0 ,9 ,6 ,8],
# [9 ,5 ,8 ,2 ,8 ,4 ,5 ,0 ,4 ,0 ,7 ,2 ,7 ,3 ,6 ,2],
# [5 ,0 ,6 ,6 ,3 ,0 ,6 ,4 ,8 ,1 ,3 ,7 ,0 ,7 ,1 ,1],
# [8 ,2 ,6 ,6 ,2 ,6 ,6 ,8 ,2 ,5 ,1 ,7 ,9 ,1 ,9 ,2],
# [6 ,3 ,9 ,2 ,0 ,9 ,8 ,4 ,3 ,6 ,2 ,0 ,4 ,1 ,8 ,3],
# [9 ,6 ,5 ,2 ,8 ,8 ,6 ,9 ,8 ,9 ,9 ,7 ,6 ,7 ,7 ,8],
# [2 ,8 ,2 ,5 ,9 ,0 ,2 ,5 ,9 ,8 ,3 ,0 ,3 ,6 ,0 ,5],
# [4 ,7 ,1 ,8 ,5 ,0 ,2 ,3 ,0 ,0 ,6 ,0 ,7 ,9 ,0 ,1],
# [5, 9, 4, 9, 9, 1, 5, 8, 0, 4, 1, 3, 7, 6, 6, 3]])

# dystanse = np.array([[15 ,20 ,26 ,20 ,13 ,27 ,22 ,15 ,16 ,22 ,24 ,20 ,22 ,11 ,28 ,24],
# [12 ,17 ,22 ,15 ,15 ,20 ,19 ,27 ,29 ,11 ,27 ,14 ,22 ,19 ,20 ,22],
# [15 ,26 ,18 ,29 ,18 ,14 ,19 ,26 ,24 ,26 ,19 ,12 ,27 ,23 ,16 ,14],
# [16 ,29 ,23 ,28 ,11 ,15 ,26 ,29 ,17 ,21 ,18 ,19 ,10 ,26 ,19 ,12],
# [11 ,25 ,22 ,29 ,11 ,27 ,13 ,22 ,22 ,22 ,20 ,29 ,14 ,28 ,12 ,10],
# [10 ,24 ,17 ,23 ,30 ,13 ,29 ,22 ,21 ,25 ,16 ,15 ,22 ,16 ,15 ,26],
# [17 ,25 ,29 ,20 ,17 ,14 ,21 ,15 ,16 ,16 ,26 ,24 ,27 ,15 ,16 ,14],
# [13 ,26 ,28 ,29 ,12 ,26 ,21 ,30 ,19 ,22 ,21 ,25 ,12 ,28 ,17 ,29],
# [12 ,25 ,17 ,27 ,18 ,28 ,29 ,25 ,13 ,15 ,16 ,23 ,14 ,25 ,11 ,30],
# [28 ,20 ,24 ,28 ,22 ,11 ,22 ,29 ,26 ,21 ,27 ,25 ,28 ,21 ,25 ,15],
# [30 ,15 ,20 ,24 ,29 ,15 ,22 ,24 ,19 ,27 ,28 ,29 ,21 ,22 ,23 ,25],
# [23 ,18 ,16 ,11 ,18 ,13 ,13 ,29 ,16 ,15 ,16 ,24 ,11 ,22 ,19 ,28],
# [16 ,28 ,22 ,13 ,18 ,17 ,10 ,11 ,23 ,23 ,23 ,11 ,16 ,13 ,24 ,30],
# [29 ,18 ,16 ,25 ,25 ,19 ,12 ,10 ,28 ,20 ,24 ,25 ,12 ,11 ,30 ,23],
# [27 ,24 ,28 ,12 ,10 ,15 ,28 ,28 ,28 ,17 ,25 ,22 ,23 ,18 ,24 ,13],
# [21, 11, 29, 16, 30, 20, 18, 12, 18, 26, 25, 19, 13, 18, 26, 11]])


def generate(products, producents, clients, zakres_d, zakres_g):
    producenci = np.random.randint(zakres_d, zakres_g, size = (producents, products))
    klienci = np.random.randint(zakres_d/2, zakres_g/2, size = (clients, products))
    ceny = np.random.uniform(0, 10, size = (producents, products))
    dystans = np.random.uniform(0, 30, size=(producents, clients))
    return producenci, klienci, ceny, dystans
producenci, klienci, ceny, dystanse = generate(50, 50, 50, 2, 40)
print(f"{producenci}\n")
print(f"{klienci}\n")
print(f"{ceny}\n")
print(f"{dystanse}\n")
data = {
    'producenci': producenci.flatten(),
    'klienci': klienci.flatten(),
    'cena': ceny.flatten(),
    'dystans': dystanse.flatten()
}

df = pd.DataFrame(data)
df.to_csv('Dataframe')
value = pd.read_csv('Dataframe')