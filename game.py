# game.py
import random
from word_data import word_list, get_same_category_words

def weighted_imposter_count(players):
    options = [1, 2, 3, 4, 5, 6, 7, 8]
    weights = [40, 18, 13, 8, 1, 10, 10, 0]
    count = random.choices(options, weights=weights, k=1)[0]
    return min(count, players)

def create_game(players, difficulty):
    # Filter words by difficulty
    eligible = [w for w in word_list if w[1] <= difficulty]
    secret_word, _ = random.choice(eligible)

    imposters_count = weighted_imposter_count(players)

    roles = [secret_word] * players
    imposters = random.sample(range(players), imposters_count)

    same_cat_words = get_same_category_words(secret_word, difficulty)

    for i in imposters:
        roles[i] = random.choice(same_cat_words)

    random.shuffle(roles)  # shuffle roles so imposters aren't predictable

    starting_player = random.randint(0, players - 1)

    return {
        "players": players,
        "difficulty": difficulty,
        "secret_word": secret_word,
        "roles": roles,
        "imposters": imposters,
        "imposters_remaining": imposters_count,
        "current_player": starting_player
    }


