__author__ = 'plevytskyi'


class ToyFactory:

    @classmethod
    def get_factory(cls, type_factory):
        for factory in cls.__subclasses__():
            if factory.__name__ == type_factory:
                return factory()
        raise TypeError('Unknown Factory.')

    def get_cat(self):
        raise NotImplementedError

    def get_bear(self):
        raise NotImplementedError


class WoodenToysFactory(ToyFactory):

    def get_cat(self):
        return WoodenCat()

    def get_bear(self):
        return WoodenBear()


class TeddyToysFactory(ToyFactory):

    def get_cat(self):
        return TeddyCat()

    def get_bear(self):
        return TeddyBear()


class Cat:
    def result(self):
        raise NotImplementedError


class WoodenCat(Cat):
    def result(self):
        print('Wooden cat')


class TeddyCat(Cat):
    def result(self):
        print('Teddy cat')


class Bear:
    def result(self):
        raise NotImplementedError


class WoodenBear(Bear):
    def result(self):
        print('Wooden bear')


class TeddyBear(Bear):
    def result(self):
        print('Teddy bear')


if __name__ =="__main__":
    factory = ToyFactory.get_factory('WoodenToysFactory')
    cat = factory.get_cat()
    bear = factory.get_bear()
    cat.result()
    bear.result()

    factory = ToyFactory.get_factory('TeddyToysFactory')
    cat = factory.get_cat()
    bear = factory.get_bear()
    cat.result()
    bear.result()