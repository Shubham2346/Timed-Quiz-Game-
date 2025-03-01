import time
import threading



def timed_input(prompt, time_limit):
    answer = [None]

    def get_input():
        answer[0] = input(prompt).strip().upper()
    thread = threading.Thread(target=get_input)  
    thread.start()  
    thread.join(timeout=time_limit)  

    if thread.is_alive():  
        print("\n⏰ Time's up! Moving to the next question...")
        return None 
    return answer[0]  


questions = [
    {"question": "How many elements are in the periodic table?", "options": ["A) 200", "B) 156", "C) 118", "D) 110"], "answer": "C"},
    {"question": "Which planet in the Milky Way is the hottest?", "options": ["A) Mercury", "B) Mars", "C) Jupyter", "D) Venus"], "answer": "D"},
    {"question": "How many bones do we have in an ear?", "options": ["A) 0", "B) 3", "C) 5", "D) 1"], "answer": "B"},
    {"question": "Which is the only body part that is fully grown from birth?", "options": ["A) Eyes", "B) Hands", "C) Ears", "D) Nose"], "answer": "A"},
    {"question": " Name the longest river on the Earth?", "options": ["A) Nile", "B) Amazon River", "C) Ganga", "D) Colorado River"], "answer": "A"}
]

def quiz(quest):
    score = 0
    time_limit = 10

    for q in questions:
        print("\n" +q["question"])
        for option in q["options"]:
            print(option)
        
        user = timed_input("Enter Your answer (A, B, C, or D):", time_limit)


        if user is None:  
            continue 

        user = user.strip().upper()

        if user == q["answer"]:  
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.")

    print(f"Your final score: {score}/{len(questions)}")        

quiz(questions)
