import random

def get_heart_data():
    return random.randint(60, 120), (random.randint(100, 150), random.randint(60, 100))

def simulate_motion():
    return random.choice([True] * 9 + [False])