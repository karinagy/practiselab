def check_relation(net, first, second):

    graph = {}
    # создаем граф связей между пользователями
    for connection in net:
        user1, user2 = connection
        if user1 not in graph:
            graph[user1] = set()
        if user2 not in graph:
            graph[user2] = set()
        graph[user1].add(user2)
        graph[user2].add(user1)

    # выполняем поиск в ширину (BFS) для проверки наличия связи между двумя пользователями
    visited = set()
    queue = [first]
    while queue:
        user = queue.pop(0)
        if user == second:
            return True
        visited.add(user)
        for friend in graph[user]:
            if friend not in visited:
                queue.append(friend)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа")  # is True
    assert check_relation(net, "Маша", "Петя")  # is True
    # assert check_relation(net, "Ваня", "Дима")  # is False
    # assert check_relation(net, "Лёша", "Настя")  # is False
    assert check_relation(net, "Стёпа", "Маша")  # is True
    # assert check_relation(net, "Лена", "Маша")  # is False
    assert check_relation(net, "Вова", "Лена")  # is True
