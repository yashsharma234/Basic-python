# a=12.4
# print(type(a))

def generate_table(n):
    table=""
    for i in range(1,11):
        table+= f"{n}*{i} ={n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
       f.write(table)

