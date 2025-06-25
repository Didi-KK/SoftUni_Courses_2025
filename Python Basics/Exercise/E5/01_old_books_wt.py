book_title = input()

book_found = False
book_count = 0

while True:
    data_entry = input()
    
    if data_entry == 'No More Books':
        break
    
    if data_entry == book_title:
        book_found = True
        break
    
    book_count += 1

if book_found:
    print(f'You checked {book_count} books and found it.')

else:
    print(f'The book you search is not here!\nYou checked {book_count} books.')
