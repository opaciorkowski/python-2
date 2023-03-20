q1 = input("Jak masz na imię oraz nazwisko?\n")
q2 = {
    "question": "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
    "answer": ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki"]
}
q3 = {
    "question": "W jakich okolicznościach czytasz książki najczęściej?",
    "answer": ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)"]
}
q4 = {
    "question": "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
    "answer": ["chęć poszerzenia wiedzy", "czytanie mnie relaksuje / odpręża", "fakt, że czytanie jest modne"]
}
q5 = {
    "question": "Po książki w jakiej formie sięgasz najczęściej?",
    "answer": ["papierowej (tradycyjnej)", "e-booki (książki elektroniczne) na komputerze",
               "e-booki na tablecie/telefonie"]
}
q6 = {
    "question": "Ile książek czytasz średnio w ciągu roku?",
    "answer": ["0 książek", "żadnej w całości - jedynie fragmenty", "1"]
}
q7 = {
    "question": "Jak często średnio czytasz książki?",
    "answer": ["codziennie", "raz w tygodniu", "raz w miesiącu"]
}
q8 = {
    "question": "Po jakie gatunki książek sięgasz najczęściej?",
    "answer": ["kryminały/thrillery", "romanse", "psychologiczne"]
}
questions = [q2, q3, q4, q5, q6, q7, q8]
answers = []
for i in range(len(questions)):
    print(questions[i]["question"])
    print("1.", questions[i]["answer"][0])
    print("2.", questions[i]["answer"][1])
    print("3.", questions[i]["answer"][2])
    odp = input()
    while odp not in ('1', '2', '3'):
        print("niepoprawna odpowiedź")
        odp = input()
    answers.append(odp)

print("pytanie: Jak masz na imię oraz nazwisko?")
print("odpowiedz:", q1)
print("=======================================================")
for i in range(len(answers)):
    print("pytanie:", questions[i]["question"])
    print("odpowiedz:", questions[i]["answer"][int(answers[i]) - 1])
    print("=======================================================")
