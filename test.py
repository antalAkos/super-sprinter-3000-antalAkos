
def open_csv():
    with open("story.csv", "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        return table


def write_csv(table):
    with open("story.csv", "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")


table = open_csv()
print(len(table))
print(table)
for index, sublist in enumerate(table):
    if table[index][0] == sublist[0]:
        table = table.remove(sublist)
write_csv(table)

