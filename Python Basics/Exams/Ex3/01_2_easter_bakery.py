flour_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_pack = int(input())
yeast_packet = int(input())

sugar_kg_price = flour_kg_price * 0.75
eggs_pack_price = flour_kg_price * 1.10
yeast_packet_price = sugar_kg_price * 0.20

expenses = (flour_kg * flour_kg_price + sugar_kg * sugar_kg_price
            + eggs_pack * eggs_pack_price + yeast_packet * yeast_packet_price)
print(f'{expenses:.2f}')