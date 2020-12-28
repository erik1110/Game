import random

def xmas_exchange(buyer_list):
    match_dict = {}
    present_list = [i for i in range(len(buyer_list))]
    for buyer in buyer_list:
        flag = False
        present_list.sort()
        #print("present_list:", present_list)
        buyer_self = buyer_list.index(buyer)
        #print("buyer_self:", buyer_self)
        if buyer_self in present_list:
            flag = True
            present_list.remove(buyer_self)
        try:
            preset_num = random.choice(present_list)
        except:
            raise Exception("剛好有人沒辦法配對，重抽！")
        #print("preset_num:", preset_num)
        present_list.remove(preset_num)
        match_dict[buyer] = preset_num
        if flag:
            present_list.append(buyer_self)
    return match_dict

if __name__=='__main__':
    buyer_list = ["Jing", "Zinny", "Yellow", "Erik", "Witty", "Chu", "Shuo"]
    match_dict = xmas_exchange(buyer_list)
    print(match_dict)
