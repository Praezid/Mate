def get_tips_rating(amount: int) -> str:
    # write your code here
    if amount > 50:
        return 'excellent'
    if 20 < amount <= 50:
        return 'great'
    if 10 < amount <= 20:
        return 'good'
    if 0 < amount <= 10:
        return 'poor'
    if amount == 0:
        return 'terrible'
