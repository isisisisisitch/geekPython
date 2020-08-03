class LightAndBulb(object):

    def __init__(self):
        self.Lightlist=[]
        self.Bulblist=[]


    def add_Light(self):
        bulbid = input("plz input bulb id")
        price = input("plz input the price for the light")
        weight = input("plz input the weight for the light")
        id=input('pls input a id for the light')
        bulb= self.query_bulb_by_id(bulbid)
        self.query_bulb_by_id(bulb)
        light = Light(bulb, id, price, weight)
        self.Lightlist.append(light)
        return 'added'
    def add_Bulb(self):
        size = input('pls input the size of the bulb')
        id = ('pls input the id of the bulb')
        price = input(' pls input the price of the color')
        color = ('pls input the color of the bulb')
        bulb = Bulb(size,id,price,color)
        self.Bulblist.append(bulb)
        return 'addded'

    def del_Light(self):
        del_id= input("plz input light's id")

        for i in self.Lightlist:
            if del_id == i.id:
                self.Lightlist.remov

    def query_bulb_by_id(self,query_id):


        for i in self.Bulblist:
            if query_id == i.id:
                return i
        return "no such bulb!"
