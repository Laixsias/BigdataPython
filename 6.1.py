# конечный
# from time import sleep
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#     def running(self):
#         i=0
#         while i<3:
#             print(f'{TrafficLight.__color[i]}')
#             if i==0:
#                 sleep(8)
#             elif i==1:
#                 sleep(6)
#             elif i==2:
#                 sleep(4)
#             i+=1
# TrafficLight = TrafficLight()
# TrafficLight.running()


# бесконечный
class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))
    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)
