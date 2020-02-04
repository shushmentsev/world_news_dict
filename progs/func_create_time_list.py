#Создание списка: [время начала фразы, время конца фразы, фраза]

#Была проблема с кодировкой. Поэтому использую данную библиотеку:
import io

def create_time_list(sub_path):
    
    #Создание списка из строк файла субтитров:
    my_list = []
    
    with io.open(sub_path, encoding = 'utf-8') as file:
        for line in file:
            my_list.append(line)

    #
    time_list = [[],[],[]]
    
    for i in range(len(my_list)):

        if "-->" in my_list[i]:

            temp_list = my_list[i].split(" ")
            time_list[0].append(temp_list[0])
            time_list[1].append(temp_list[2].replace("\n", ""))

            s = ""
            x = i + 1
            
            while ("\n" != my_list[x]):

                s = s + my_list[x]
                x = x + 1

            #Форматирование строки:
            s = s.replace("\n", " ")
            s = s.lower()
            #c
            s = s.strip(" ")
            time_list[2].append(s)

    return time_list


#Удаление символов перехода на новую строку из списка:
#for i in range(my_list.count("\n")):
    #my_list.remove("\n")

#Вывод списка:
#for i in range(len(my_list)):
    #print(my_list[i])

#Удаление лишних переносов строк:
#for i in range(my_list.count("\n")):
    #my_list.remove("\n")
