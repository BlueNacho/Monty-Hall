import random


def montyHall():
    switch = select_strategy()
    times = select_times()
    wins = 0

    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    for _ in range(times):
        available_doors = [0, 1, 2]

        # Jugador selecciona una puerta
        contestant = random.randint(0, 2)
        contestant_first = contestant
        available_doors.remove(contestant_first)

        # Monty descarta una puerta
        for door in available_doors:
            if doors[door] == 'goat':
                monty = door

        # Si el jugador decide cambiar de puerta
        if (switch):
            available_doors.remove(monty)
            contestant = available_doors[0]

        if doors[contestant] == 'car':
            wins += 1

    if times == 1:
        if switch:
            return {'contestant_door': contestant_first + 1,
                    'car_door': doors.index('car') + 1,
                    'monty_door': monty + 1,
                    'switched_door': contestant + 1,
                    'winner': doors[contestant] == 'car'
                    }
        else:
            return {'contestant_door': contestant_first + 1,
                    'car_door': doors.index('car') + 1,
                    'monty_door': monty + 1,
                    'switched_door': 'ninguna',
                    'winner': doors[contestant] == 'car'
                    }
    else:
        return {'times': times,
                'wins': wins
                }


def select_strategy():
    switch = True
    error = True

    while error == True:
        selected = input(
            'Seleccione su estrategia \n 1. Quedarse en la puerta \n 2. Cambiarse de puerta \n > ')

        if selected in ['1', '2']:
            error = False

    if selected == '1':
        switch = False

    return switch


def select_times():
    times = 0
    error = True

    while error == True:
        selected = input(
            'Seleccione la cantidad de veces que se ejecutara la simulacion \n 1. Una vez \n 2. 1.000 \n 3. 10.000 \n 4. 100.000\n > ')

        if selected in ['1', '2', '3', '4']:
            error = False

    if selected == '1':
        times = 1
    elif selected == '2':
        times = 1000
    elif selected == '3':
        times = 10000
    elif selected == '4':
        times = 100000

    return times


results = montyHall()

if len(results) == 5:
    winner = "gano" if results['winner'] else "perdio"

    print(f"Puerta elegida por el participante: {results['contestant_door']}")
    print(f"Puerta del auto: {results['car_door']}")
    print(f"Puerta elegida por Monty: {results['monty_door']}")
    print(f"Puerta cambiada: {results['switched_door']}")
    print(f"Resultado del concurso: {winner}")
else:
    frecuency = results['wins'] / results['times']
    win_rate = 100 * frecuency
    
    print(f"Casos posibles: {results['times']}")
    print(f"Casos favorables: {results['wins']}")
    print(f"Frecuencia relativa: {round(frecuency, 2)}")
    print(f"Porcentaje de ganadas: {round(win_rate, 1)}%")