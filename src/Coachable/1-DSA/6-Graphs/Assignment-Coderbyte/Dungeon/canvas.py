import collections

from graph import Monster, Treasure, Dungeon, Player


# a(3) -> b(4) -> c(5) -> treasure
def create_dungeon() -> Dungeon:
    a = Monster("a", 3)
    b = Monster("b", 4)
    c = Monster("c", 5)
    treasure = Treasure()
    a.append_monster(b)
    b.append_monster(c)
    c.append_treasure(treasure)

    return Dungeon(a)


# a(3) -> b(4)  c(5) -> treasure
def create_dungeon2() -> Dungeon:
    a = Monster("a", 3)
    b = Monster("b", 4)
    c = Monster("c", 5)
    treasure = Treasure()
    a.append_monster(b)
    c.append_treasure(treasure)

    return Dungeon(a)


# a(1) -> b(4)
#   |      |
#   v      v
# c(2) -> d(1) -> treasure
def create_dungeon3():
    a = Monster("a", 1)
    b = Monster("b", 4)
    c = Monster("c", 2)
    d = Monster("d", 1)
    treasure = Treasure()
    a.append_monster(b)
    a.append_monster(c)
    b.append_monster(d)
    c.append_monster(d)
    d.append_treasure(treasure)

    return Dungeon(a)


# a(1) -> b(4) -> e(1)
#   |      |
#   v      v
# c(2) -> d(1) -> treasure
def create_dungeon4():
    a = Monster("a", 1)
    b = Monster("b", 4)
    c = Monster("c", 2)
    d = Monster("d", 1)
    e = Monster("e", 1)
    treasure = Treasure()
    a.append_monster(b)
    a.append_monster(c)
    b.append_monster(d)
    c.append_monster(d)
    b.append_monster(e)
    d.append_treasure(treasure)

    return Dungeon(a)


# a(1) -> b(5) -> e(1)
#   |      |       |
#   v      v       v
# c(2) -> d(7) -> f(2) -> treasure
# optimal -> a -> b -> e -> f
def create_dungeon5():
    a = Monster("a", 1)
    b = Monster("b", 5)
    c = Monster("c", 2)
    d = Monster("d", 7)
    e = Monster("e", 1)
    f = Monster("f", 2)
    treasure = Treasure()
    a.append_monster(b)
    a.append_monster(c)
    b.append_monster(e)
    b.append_monster(d)
    c.append_monster(d)
    d.append_monster(f)
    e.append_monster(f)
    f.append_treasure(treasure)

    return Dungeon(a)


# a(1) -> b(5) -> e(1) ------
#   |      |       |        |
#   v      v       v        v
# c(2) -> d(7) -> f(2) -> treasure
# optimal -> a -> b -> e -> f
def create_dungeon6():
    a = Monster("a", 1)
    b = Monster("b", 5)
    c = Monster("c", 2)
    d = Monster("d", 7)
    e = Monster("e", 1)
    f = Monster("f", 2)
    treasure = Treasure()
    a.append_monster(b)
    a.append_monster(c)
    b.append_monster(e)
    b.append_monster(d)
    c.append_monster(d)
    d.append_monster(f)
    e.append_monster(f)
    e.append_treasure(treasure)
    f.append_treasure(treasure)

    return Dungeon(a)


d1 = create_dungeon()  # True
d2 = create_dungeon2()  # False
d3 = create_dungeon3()  # True
d4 = create_dungeon4()  # False
d5 = create_dungeon5()  # True
d6 = create_dungeon6()  # True

# print(d1.all_paths_lead_to_treasure())
# print(d2.all_paths_lead_to_treasure())
# print(d3.all_paths_lead_to_treasure())
# print(d4.all_paths_lead_to_treasure())
# print(d5.all_paths_lead_to_treasure())
# print(d6.all_paths_lead_to_treasure())


# print(d1.get_all_paths())
# print(d2.get_all_paths())
# print(d3.get_all_paths())
# print(d4.get_all_paths())

# print(d3.find_optimal_path())


print(d1.probability_player_will_make_it(Player(12)), 1.0)  # 1.0
print(d1.probability_player_will_make_it(Player(11)), 0.0)  # 0.0
print(d2.probability_player_will_make_it(Player(100)), 0.0)  # 0.0
print(d3.probability_player_will_make_it(Player(1)), 0.0)  # 0.0
print(d3.probability_player_will_make_it(Player(5)), 0.5)  # 0.5
print(d3.probability_player_will_make_it(Player(100)), 1.0)  # 1.0
print(d4.probability_player_will_make_it(Player(1)), 0.0)  # 0.0
print(d4.probability_player_will_make_it(Player(5)), 0.5)  # 0.5
print(d4.probability_player_will_make_it(Player(100)), 0.75)  # 0.75
