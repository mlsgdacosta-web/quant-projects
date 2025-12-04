from collections import deque

class SimpleOrderBook:
    def __init__(self):
        self.bids = []  # list of (price, size)
        self.asks = []

    def top_of_book(self):
        bid = max(self.bids)[0] if self.bids else None
        ask = min(self.asks)[0] if self.asks else None
        return bid, ask

    def add_bid(self, price, size):
        self.bids.append((price, size))

    def add_ask(self, price, size):
        self.asks.append((price, size))
