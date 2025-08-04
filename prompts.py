truths = [
    "What’s your biggest fear?",
    "Have you ever lied to your best friend?",
    "What is your most embarrassing moment?",
    "Have you ever cheated on a test?"
]

dares = [
    "Do 10 jumping jacks!",
    "Text your crush something random.",
    "Post a silly selfie in the group.",
    "Sing a song loudly!"
]

import random

def get_random_truth():
    return random.choice(truths)

def get_random_dare():
    return random.choice(dares)
