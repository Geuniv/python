class Service:
    secret = "영구는 배꼽이 두 개다."

    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s 입니다." % (a, b, result))


pey = Service()

print(pey.secret)

pey = Service()

pey.sum(1, 1)