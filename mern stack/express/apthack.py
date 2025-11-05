import bcrypt

# Assuming this is your input JSON (truncated here for brevity, use full JSON)
input_data = {
    "_id": "67530d22abb6de12ea2623b8",
    "course": "66a0d1633001b8b3a2adf81e",
    "technology": "66a0d5973001b8b3a2ae5f4a",
    "module": "66a0d6873001b8b3a2ae765a",
    "module_name": "Aptitude",
    "topic": "66a0d8da3001b8b3a2ae9d7b",
    "level": "easy",
    "test_name": "Averages_MT_E2",
    "test_description": "Averages_MT_E",
    "questions": [
        {
            "_id": "66d986b6f5c98aa0edb1e2b1",
            "question": "What is the average of first 20 multiple of 3?",
            "level": "easy",
            "option1": "200",
            "option2": "31.5",
            "option3": "21.5",
            "option4": "300",
            "answer": "$2a$10$czzEPDywqqf6qeaeRGdxmeRGG6AyKwOWdIhxU25ylKCInQxjqWoV2"
        },
        {
            "_id": "66d98678f5c98aa0edb1d9c3",
            "question": "The average age of 24 students in a class is 10. If the teacher's age is inclueded, the average increased by one. What is the age of the teacher?",
            "level": "easy",
            "option1": "30 yrs",
            "option2": "40 yrs",
            "option3": "25 yrs",
            "option4": "35 yrs",
            "answer": "$2a$10$NO5ODxYXGOZjYSrgi6m2ze/AxXz33pHVtb7W7ksZEV/6dSbKzGoAq"
        },
        {
            "_id": "66d98682f5c98aa0edb1db45",
            "question": "The average of seven consecutive integers is 20. The largest of these numbers is?",
            "level": "easy",
            "option1": "23",
            "option2": "22",
            "option3": "20",
            "option4": "24",
            "answer": "$2a$10$JJfhIldnrVOdXZSusnwYJ.w5WSRFhgl.eup8q1MeghC8q.3CwWKTu"
        },
        {
            "_id": "66d98685f5c98aa0edb1dbb7",
            "question": "What is the average of the first 12 multiples of 7 ?",
            "level": "easy",
            "option1": "38.5",
            "option2": "54.5",
            "option3": "45.5",
            "option4": "35.8",
            "answer": "$2a$10$zimwmg9bPFhMKOu2DmNBG.CkVOv9hoGrfWuzJv6N7xODCAinYSaRS"
        },
        {
            "_id": "66d98683f5c98aa0edb1db86",
            "question": "The average weight of 8 persons increases by 1.5 kg. If a person weighing 65 kg is replaced by a new person, what could be the weight of the new person ?",
            "level": "easy",
            "option1": "53 kg",
            "option2": "77 kg",
            "option3": "84 kg",
            "option4": "Data Inadequate",
            "answer": "$2a$10$vxxiLw6JAebmo.c0IhiEY.gdcXW2lMoDURdBkfQ1iOjJDBw69BroC"
        },
        {
            "_id": "675f16a3e22b98b5f14c0d89",
            "question": "Find the average of first 40 natural numbers.",
            "level": "easy",
            "option1": "40",
            "option2": "35",
            "option3": "30.6",
            "option4": "20.5",
            "answer": "$2a$10$ucNmhW9MW90HNMxngV0pnOc8ClmWwZIlTulbw.EIDQESGVSyIvODG"
        },
        {
            "_id": "66d98681f5c98aa0edb1db1f",
            "question": "The average of even numbers from 1 to 20 is ?",
            "level": "easy",
            "option1": "12",
            "option2": "10",
            "option3": "11.5",
            "option4": "11",
            "answer": "$2a$10$7n6ICfBqXkHZCKSTwoBzJuFuW.m3tsvUuNGJjnBPvskUAvl.OQoES"
        },
        {
            "_id": "675f16a3e22b98b5f14c0d32",
            "question": "The temperatures (in Fahrenheit) on Monday, Tuesday and Wednesday in a week are 90, 94 and 98 respectively. Find the average temperature for the three days mentioned.",
            "level": "easy",
            "option1": "96",
            "option2": "92",
            "option3": "93",
            "option4": "94",
            "answer": "$2a$10$abrlsHeuhKctjREJsCDrN.LiHmhJFHuFcTpzCJjm/oxLUskiwemR2"
        },
        {
            "_id": "66d98683f5c98aa0edb1db79",
            "question": "The average weight of 6 persons is increased by 3.5 kg. When one of them who weighs 54 kg is replaced by another man the weight of the new man is ?",
            "level": "easy",
            "option1": "65 kg",
            "option2": "75 kg",
            "option3": "60 kg",
            "option4": "70 kg",
            "answer": "$2a$10$7bZpqr8OjRiX37cXqWFAA.esP1Nyut5daRHqiOYgOtFy7A6pKq8XG"
        },
        {
            "_id": "675f16a3e22b98b5f14c0ced",
            "question": "The average of a number and its reciprocal is 1. What is the value of the average of the fifth power and the reciprocal of the fifth power of the number?",
            "level": "easy",
            "option1": "2.5",
            "option2": "2",
            "option3": "1.5",
            "option4": "1",
            "answer": "$2a$10$ChR9yYViB4/ayA7Gtri93Oe/fKwZ05SgOF.Bk7.aS9ZnW0nN7sFUy"
        },
        {
            "_id": "66d986b0f5c98aa0edb1e1ae",
            "question": "Find the average of first 40 natural numbers.",
            "level": "easy",
            "option1": "40",
            "option2": "35",
            "option3": "30.6",
            "option4": "20.5",
            "answer": "$2a$10$H0raKT2vg.1HH9TIRYl/ces5wQdn8D1yp/fKb5mpLDvPPO7F.22na"
        },
        {
            "_id": "675f16a3e22b98b5f14c0cf9",
            "question": "The average of n numbers is a. If each number is increased by 20%, then the new average will be:",
            "level": "easy",
            "option1": "6a/5",
            "option2": "6a/5n",
            "option3": "5a/6",
            "option4": "5a/6n",
            "answer": "$2a$10$YyRI8Nsw64gnb5Ci6n1dWufF6cXIvSOiSbVxAgpY.fQiY0wBSlAY."
        },
        {
            "_id": "66d9867af5c98aa0edb1da08",
            "question": "The average of 7 consecutive odd numbers is given as 9. Find the smallest of these numbers.",
            "level": "easy",
            "option1": "1",
            "option2": "5",
            "option3": "3",
            "option4": "7",
            "answer": "$2a$10$HUTrmMfLd6I1LSjAGXxsSuTJLja3mcS1FgpUxqnAk4yIrtfGTFk92"
        },
        {
            "_id": "66d9867df5c98aa0edb1da8c",
            "question": "The average runs scored by a batsman in 20 matches is 40. In the next 10 matches, the batsman scored average of 13 runs. Find his average in all the 30 matches.",
            "level": "easy",
            "option1": "31",
            "option2": "29",
            "option3": "30",
            "option4": "28",
            "answer": "$2a$10$d/OE5bloI/sNedX3JJ3iQ.UcXogud7a6jKpwANO6AA5lym0HnxKUO"
        },
        {
            "_id": "66d986bcf5c98aa0edb1e360",
            "question": "The temperatures on Monday,Tuesday and Wednesday in a week are 90, 94 and 98 respectively. Find the average temperature for the three days mentioned.",
            "level": "easy",
            "option1": "96",
            "option2": "92",
            "option3": "93",
            "option4": "94",
            "answer": "$2a$10$HbGK5SbkHrSeNtVo0gRWs.kRfY74YT5YPRjMG2FwbHrJ8S25nMnFu"
        },
        {
            "_id": "66d9867bf5c98aa0edb1da30",
            "question": "The height of 5 boys is recorded as 146 cm, 154 cm, 164 cm, 148 cm and 158 cm. What is the average height of all these boys?",
            "level": "easy",
            "option1": "154 cm",
            "option2": "158 cm",
            "option3": "152 cm",
            "option4": "156 cm",
            "answer": "$2a$10$21Rh4GZ4Bgi4Hh04/SMJt.MNpgR65D7kScZcAelv5W53c3DxlmEt2"
        },
        {
            "_id": "66d9867ff5c98aa0edb1dadd",
            "question": "The average of 10 numbers is 5. What will be the new average, if each of the numbers is multiplied by 4 ?",
            "level": "easy",
            "option1": "40",
            "option2": "20",
            "option3": "9",
            "option4": "14",
            "answer": "$2a$10$06aqZfDX1fhsOyWNB5WEyOopfNoQjWKznPVSQErn8Oyu7/GjsXL0y"
        },
        {
            "_id": "66d98679f5c98aa0edb1d9ee",
            "question": "The average of 5 consecutive numbers is given 17. Find the largest number.",
            "level": "easy",
            "option1": "21",
            "option2": "20",
            "option3": "19",
            "option4": "18",
            "answer": "$2a$10$hYzSWiqRp9IOo62iv6VhGOzOOTsUb/OVbdXC2HnkN/ZwACQ8yYKnK"
        },
        {
            "_id": "66d986bbf5c98aa0edb1e346",
            "question": "The average weight of a class of 29 students is 40 kg. If the weight of the teacher be included, the average rises by 500 gm. What is the weight of the teacher?",
            "level": "easy",
            "option1": "50.5 kg",
            "option2": "40.5 kg",
            "option3": "45 kg",
            "option4": "55 kg",
            "answer": "$2a$10$.9qTST1zg6S4IsG/oyjBdORBW9EOzEZMk4xLD29XZuU/XOViMbJM."
        },
        {
            "_id": "675f16a3e22b98b5f14c0d1a",
            "question": "The average of 64, 36, 44, 56 and x is 50. Find the value of x.",
            "level": "easy",
            "option1": "20",
            "option2": "30",
            "option3": "50",
            "option4": "40",
            "answer": "$2a$10$Mk/FO5zhs7WA8bjJCiS2KuDxtqeHZqQulJYRLw44gzU51/UuBd8HW"
        }
    ],
    "timings": {
        "_id": "688dcc8ea4bd0a7d91ef7a8a",
        "Aptitude": {
            "easy": 60,
            "medium": 75,
            "hard": 90
        },
        "Reasoning": {
            "easy": 60,
            "medium": 75,
            "hard": 90
        },
        "Verbal Ability": {
            "easy": 40,
            "medium": 50,
            "hard": 60
        }
    },
    "minimum_duration": 0.6
}

# Helper to find correct option using bcrypt
def find_correct_option(question_data):
    options = [
        ("option1", question_data["option1"]),
        ("option2", question_data["option2"]),
        ("option3", question_data["option3"]),
        ("option4", question_data["option4"])
    ]
    answer_hash = question_data["answer"]
    for key, value in options:
        if bcrypt.checkpw(value.strip().encode(), answer_hash.encode()):
            return key, value
    return "Unknown", None

# Process all questions
results = []
for q in input_data["questions"]:
    correct_option, answer_text = find_correct_option(q)
    results.append({
        "question": q["question"].replace("\r\n", " ").strip(),
        "correct_option": correct_option,
        "answer_text": answer_text
    })

# Output results
for idx, item in enumerate(results, 1):
    print(f"Q{idx}: {item['question']}")
    print(f"   Correct: {item['correct_option']} -> {item['answer_text']}\n")