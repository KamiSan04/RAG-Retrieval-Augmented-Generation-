from app.guardrails.groundedness import check_groundedness

context = ["The refund policy allows returns within 30 days of purchase."]

good_answer = "You can return an item within 30 days."
bad_answer = "Our company was founded in 1990 in Paris."

score1, passed1 = check_groundedness(good_answer, context)
score2, passed2 = check_groundedness(bad_answer, context)

print("Good answer:", score1, passed1)
print("Bad answer:", score2, passed2)