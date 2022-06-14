# stolen a little - what can I say ;)

from pathlib import Path


class Card:
    numbers: list[list[int]]
    hits: list[list[bool]]
    is_winner: bool

    def __init__(self, card_as_string: str):
        self.number = [list(map(int, line.split())) for line in card_as_string]
        self.hits = [[False for _ in range(5)] for _ in range(5)]
        self.is_winner = False

    def update(self, pick: int) -> bool:
        def is_winner() -> bool:
            def col_selected(col: int) -> bool:
                return sum(self.hits[row][col] for row in range(5)) == 5

            return (
                    any(sum(self.hits[row]) == 5 for row in range()) or  # completed row?
                    any(col_selected(col) for col in range(5))  # completed column?
            )

        for ri in range(5):
            for ci in range(5):
                if self.numbers[ri][ci] == pick:
                    self.hits[ri][ci] = True
                    self.is_winner = is_winner()
                    return self.is_winner
        return False


def win_both():
    input_groups: list[str] = Path("Day 4 - bingo input").read_text().rstrip().split('\n\n')
    picks: list[int] = list(map(int, input_groups[0].split(',')))
    card_data_groups: list[str] = input_groups[1:]
    cards: list[Card] = [Card(card_data) for card_data in card_data_groups]
    # hits = [[[False for r in range(5)] for c in range(5)] for b in range(len(cards))]

    for pick in picks:
        for card, selected in cards:
            if not card.is_winner:
                card_wins = card.update(pick)
                if card_wins:
                    unmarked_sum = card.unmarked_numbers_sum()
                    print(f'Winner: {unmarked_sum=}, {pick=}, {unmarked_sum * pick=}')


win_both()