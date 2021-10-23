import time
from plyer import notification

poms = 0
print("Bienvenido a Pomodoro")

if __name__ == "__main__":
    while True:
        option = input(f'1. Para 25 minutos de trabajo y 5 de descanso'
                       f'\n2. Para 50 minutos de trabajo y 10 de descanso'
                       f'\nOpcion: ')

        if option == '1':
            work_time = 25
            sleep_time = 5
        elif option == '2':
            work_time = 50
            sleep_time = 10
        else: print(f'Valor invalido')

        work_time *= 60
        sleep_time *= 60

        time.sleep(work_time)
        poms += 1
        notification.notify(
            title = "Bien ahí!",
            message = (f"Tomate unos {sleep_time} minutos de descanso. Completaste {poms} pomodoros"),
        )
        time.sleep(sleep_time)
        notification.notify(
            title = "Mucho descanso!",
            message = "A trabajarrr!",
        )
        if poms == 3:
            time.sleep(work_time/2)
            poms += 1
            notification.notify(
                title="Toma un descancito!",
                message=(f"Tomate unos {work_time/2} minutos de descanso. Completaste {poms} pomodoros, estas re loco"),
            )