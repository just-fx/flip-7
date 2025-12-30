import random


def reset_cards():
    cards = [0]
    for i in range(1, 13):
        for j in range(1, i + 1):
            cards.append(i)
    return cards


if __name__ == "__main__":
    players = 3

    cards = reset_cards()
    player_cards = {player + 1: [] for player in range(players)}
    player = 1
    skipped_players = []
    player_sums = {player + 1: 0 for player in range(players)}

    while True:
        if player not in skipped_players:
            print(f"=======PLAYER {player}=======")
            answer = input("Hit/Stay:")
            if answer.lower().strip() == "stay":
                skipped_players.append(player)

            else:
                drawn_card_index = random.randint(0, len(cards) - 1)
                drawn_card = cards.pop(drawn_card_index)
                player_sums[player] += drawn_card
                print(drawn_card)
                print(f"sum: {player_sums[player]}")
                if drawn_card in player_cards[player]:
                    print("BUSTED 💣")
                    player_sums[player] = 0
                    skipped_players.append(player)
        if len(skipped_players) == players:
            print("GAME OVER!")
            break

        player_cards[player].append(drawn_card)
        player = ((player) % players) + 1

    print(player_sums)
