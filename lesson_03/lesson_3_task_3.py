from address import Address
from mailing import Mailing

to_address = Address(117534, "Москва", "Чертановская", 51, 45)
from_address = Address(664020, "Иркутск", "Волгоградская", 110, 70)
mailing = Mailing(to_address, from_address, 35, 98445301)

print(mailing)