statues_to_print = int(input())

statues_printed = 0
printers = 1
days = 0

while statues_printed < statues_to_print:
    if (statues_to_print - statues_printed) > printers:
        days += 1
        printers += printers
    else:
        days += 1
        statues_printed += printers

print(days)
