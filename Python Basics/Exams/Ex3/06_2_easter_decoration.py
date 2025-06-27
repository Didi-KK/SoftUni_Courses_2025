all_clients_expenses = 0
clients = int(input())

for _ in range(clients):
    client_expenses = 0
    clients_products = 0
    command = input()
    while command != 'Finish':
        purchase_type = command
        clients_products += 1

        if purchase_type == 'basket':
            client_expenses += 1.50
        elif purchase_type == 'wreath':
            client_expenses += 3.80
        elif purchase_type == 'chocolate bunny':
            client_expenses += 7.00

        command = input()

    if clients_products % 2 == 0:
        client_expenses *= 0.8

    all_clients_expenses += client_expenses

    print(f'You purchased {clients_products} items for {client_expenses:.2f} leva.')

average_expenses = all_clients_expenses / clients
print(f'Average bill per client is: {average_expenses:.2f} leva.')
