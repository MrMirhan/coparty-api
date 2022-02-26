#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.basket = list()

    def add(self, item):
        self.basket.append(item)
    
    def total(self):
        return sum([item.price for item in self.basket])
    
    def __len__(self):
        return len(self.basket)



if __name__ == '__main__':
    n = [
        "bike 150",
        "headphones 20"
    ]
    items = []
    for _ in range(len(n)):
        name, price = n[_].split(" ")
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = [
        "2",
        "bike 1000",
        "headphones 100",
        "8",
        "total",
        "add bike",
        "len",
        "total",
        "add headphones",
        "add headphones",
        "len",
        "total"
    ]
    for _ in range(len(q)):
        line = q[_].split(" ")
        command, params = line[0], line[1:]
        if command == "len":
            print(len(cart))
        elif command == "total":
            print(cart.total())
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
