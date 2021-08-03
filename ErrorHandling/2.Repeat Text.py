def repeat_text(text, times):
    return text * times

try:
    text = input()
    times = int(input())
    print(repeat_text(text, times))
except ValueError:
    print("Variable times must be an integer")