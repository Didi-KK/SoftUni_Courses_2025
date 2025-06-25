book_title = input()
data_entry = input()

book_found = False
book_count = 0

while data_entry != 'No More Books':
    
    if data_entry == book_title:
        book_found = True
        break
    
    data_entry = input()
    book_count += 1

if book_found:
    print(f'You checked {book_count} books and found it.')

else:
    print(f'The book you search is not here!\nYou checked {book_count} books.')
