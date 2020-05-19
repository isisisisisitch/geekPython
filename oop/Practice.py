# import random
# class Home():
#     furniture_number=0
#
#
#     def __init__(self,address,area):
#         self.address=address
#         self.area=area
#         self.free_area=area
#         self.furniture=[]
#
#
#     def add_furniture(self,furniture):
#         if type(furniture)!=Furniture:
#             return False
#         self.furniture.append(f"{furniture.name}'s size:{furniture.size}")
#         self.free_area-=furniture.size
#         print(f"{furniture.name} added, size:{furniture.size}, free_area remaining:{self.free_area} continue")
#
#
#
# class Furniture():
#     def __init__(self,size):
#         # Home.furniture_number+=1
#         self.name=self.getname_furniture()
#         self.size=size
#
#     def getname_furniture(self):
#         pick=random.randint(1,10)
#         if pick<3:
#             return "light"
#         elif pick<5:
#             return "table"
#         elif pick<7:
#             return "chair"
#         elif pick<9:
#             return "electronic device"
#         else:
#             return "bed"
#
#
#
# home=Home("8848 midland area",50)
# while home.free_area>0:
#     furniture=Furniture(random.randint(1,10))
#     if furniture.size>home.free_area:
#         break
#     home.add_furniture(furniture)
# print(f"total furniture added:{home.furniture}")
# print('no free area, over')

class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f' {self.name} takes {self.area} m'


class Home(object):
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.furniture = []
        self.freearea = area

    def __str__(self):
        return (f'address:{self.address} area:{self.area} freearea:{self.freearea}')

    def addFurniture(self, furniture):
        print(f'adding{furniture}')
        if furniture.area > self.freearea:
            print('not enough space to add the furniture in')
            return
        self.furniture.append(furniture.name)
        self.freearea -= furniture.area
        print(f'remaining:{self.freearea}')


bed = Furniture("bed", 4)
chest = Furniture("chest", 2)
table = Furniture("table", 1.5)
House = Home("trt 50", 60)
House.addFurniture(bed)
House.addFurniture(chest)
House.addFurniture(table)

# print(House)
# print(bed)
# print(chest)
# print(table)


