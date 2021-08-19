import json
import datetime
def max_and_min_sum():
    list_1 = [1,2,3,4,5]
    list_2 = [3,4,5,6,7]
    min_sum_result = min(list_1)+min(list_2)
    max_sum_result = max(list_1)+max(list_2)
    print(f'Max sum result is {max_sum_result}')
    print(f'Min sum reseult is {min_sum_result}')


exception_list = []
list_1 = [1,2,3,0,4]
list_2 = [2,4,0,5,0]
for i in range(0,len(list_1)):
    try:
        print(list_1[i]/list_2[i]) #1 will be divided by 2 || 2 will be divided by 4 || 3 will be divided by 0
    except Exception as ex:
        ex_msg = ex.args[0]
        msg = f'list_1 value {list_1[i]} was divided by {list_2[i]} and exception occured was {ex_msg}'
        exception_list.append(msg)

try:
    with open('foo.txt','r') as f:
        print(f.readlines())
        with open('too.txt','r') as f1:
            print(f1.readlines())
except Exception as ex:
    exception_list.append(ex)
    print('Sorry file cannot be opened please refer to logs')






def create_log(exception_list):
    try:    
        with open('mylog.log','a') as f:
            f.write("\n")
            f.write(f'Log has been created on {datetime.datetime.now()}')
            f.write("\n")
            f.write("------------------------------------------------------------------------------")
            f.write("\n")
            numbering = 1
            for ex in exception_list:
                f.write(f"{numbering}. {ex}")
                f.write("\n")
                numbering=numbering+1
            f.write("------------------------------------------------------------------------------")
            print('log has been created')
    except Exception as ex:
        print(ex.args[0])

create_log(exception_list)