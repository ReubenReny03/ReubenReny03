class item:
    def __init__(self,name,profit,deadline):
        self.name = name
        self.profit = profit
        self.deadline = deadline

def max_profit(arra):
    arra.sort(key=lambda x: x.profit, reverse=True)

def greedy(arra,num):
    timeline = [0]*(num)
    for x in arra:
        print("deadline:",x.deadline)
        varifier = x.deadline
        print(varifier,x.profit)
        if (timeline[varifier-1] == 0):
            print(varifier)
            timeline[varifier-1] = x.profit
            print(timeline)

        else:
            decoy_deadline = x.deadline - 2
            while (decoy_deadline >=0):
                if (timeline[decoy_deadline] == 0):
                    timeline[decoy_deadline] = x.profit
                else:
                    decoy_deadline -=1
            else:
                print("left process")
    print(timeline)
    print(sum(timeline))

arr_of_items = [item("Startup",100,2),item("Startup_Apps",200,2),item("Old_Saved_files",150,2),item("scripts",50,4),item("Win_scripts",80,4)]
print(arr_of_items[0].name)
max_profit(arr_of_items)
greedy(arr_of_items,4)
