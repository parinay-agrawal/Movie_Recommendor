

def find_all_items(user):
    return

import numpy as np
def find_similarity(user1, user2, users):
    arr1 = np.mean(user1, axis = 0)[1]
    arr2 = np.mean(user2, axis = 0)[1]
    v1 = np.zeros(users)
    v2 = np.zeros(users)
    for i in user1:
        v1[i[0]] = i[1] - arr1
    for i in user2:
        v2[i[0]] = i[1] - arr2
    #v1 = v1 - np.mean(v1)
    pro = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    sim = pro/(norm1*norm2)
    return sim

from operator import itemgetter
def select_min20(user_list, k):
    temp = sorted(user_list, key=itemgetter(1))
    return temp[:k]

def search_table(user1, user2):
    return

def predict(user1, user2):
    v = search_table(user1, user2)
    if v > 0:
        return v
    max_sim = matrix[user1]
    sigma_sim = 0.0
    mean_rating = 0.0
    for i in max_sim:
        if i[0] == user2 or i[0] == user1:
            continue
        v = search_table(i[0], user2)
        if v > 0:
            mean_rating += v*i[1]
            sigma_sim += i[1]
    if(sigma_sim < 0.00000001):
        return -1
    else:
        return mean_rating/sigma_sim
    
    
    
        

users = 10
matrix = []
for i in range(users):
    v1 = find_all_items(i)
    min_v = []
    for j in range(users):
        v2 = find_all_items(j)
        sim = find_similarity(v1, v2, users)
        min_v.append([j,sim])
    min_v = select_min20(min_v)
    matrix.append(min_v)
        