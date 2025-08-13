def loading_bar(user_number: int) -> str:
    if user_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loading_bar_percent = user_number // 10
    return f"{user_number}% [{'%' * loading_bar_percent}{'.' * (10 - loading_bar_percent)}]\nStill loading..."
my_number = int(input())
print(loading_bar(my_number))
