from datetime import datetime

def time_delta(str_t_2, str_t_1):
    
    t_2 = str_t_2.split(":")
    new_t_2 = t_2[2].split(".")
    t_2 = t_2[0:2] + new_t_2

    t_1 = str_t_1.split(":")
    new_t_1 = t_1[2].split(".")
    t_1 = t_1[0:2] + new_t_1

    t_2 = datetime(10, 10, 10, int(t_2[0]), int(t_2[1]), int(t_2[2]), int(t_2[3]) * 1000)
    
    t_1 = datetime(10, 10, 10, int(t_1[0]), int(t_1[1]), int(t_1[2]), int(t_1[3]) * 1000)

    return t_2 - t_1
