from donations.models import Institution, Category


def create_institutions():
    Institution.objects.create(name="Dbam o Zdrowie", description="Pomoc dzieciom z ubogich rodzin.", type=1)
    Institution.objects.create(name="Dla Dzieci",
                               description="Pomoc osobom znajdującym się w trudnej sytuacji życiowej.", type=1)
    Institution.objects.create(name="Bez Domu", description="Pomoc dla osób nie posiadających miejsca zamieszkania.",
                               type=1)
    Institution.objects.create(name="Dzieci z przyszłością",
                               description="Pomoc dla dzieci z ubogich rodzin, w osiągnięciu lepszej przyszłości w nauce i pracy.",
                               type=2)
    Institution.objects.create(name="Zwierzęcy Zakątek", description="Pomoc dla bezdomnych zwierząt,", type=2)
    Institution.objects.create(name="EkoSystem",
                               description="Pomagamy w utylizowaniu starego sprzętu RTV lub AGD, a także pomagamy w przekazywaniu dobrego sprzętu potrzebującym osobom.",
                               type=2)
    Institution.objects.create(name="Pomoc dla Huberta",
                               description="Lokalna zbiórka dla Huberta, który stracił rodziców w wypadku samochodowym.",
                               type=3)
    Institution.objects.create(name="Noclegownia dla Ubogich",
                               description="Lokalna noclegownia dla ubogich prowadzi zbiórkę przedmiotów przed nadchodzącą zimą.",
                               type=3)


def create_categories():
    Category.objects.create(name="ubrania, które nadają się do ponownego użycia")
    Category.objects.create(name="zabawki")
    Category.objects.create(name="książki")
    Category.objects.create(name="artykuły spożywcze")
    Category.objects.create(name="przedmioty AGD lub RTV")
    Category.objects.create(name="artykuły dla zwierząt")
    Category.objects.create(name="inne")


def update_institutions():
    c1 = Category.objects.get(id=1)
    c2 = Category.objects.get(id=2)
    c3 = Category.objects.get(id=3)
    c4 = Category.objects.get(id=4)
    c5 = Category.objects.get(id=5)
    c6 = Category.objects.get(id=6)
    c7 = Category.objects.get(id=7)

    i1 = Institution.objects.get(id=1)
    i2 = Institution.objects.get(id=2)
    i3 = Institution.objects.get(id=3)
    i4 = Institution.objects.get(id=4)
    i5 = Institution.objects.get(id=5)
    i6 = Institution.objects.get(id=6)
    i7 = Institution.objects.get(id=7)
    i8 = Institution.objects.get(id=8)

    i1.categories.add(c1, c2, c3, c4)
    i1.save()

    i2.categories.add(c1, c2, c3, c4)
    i2.save()

    i3.categories.add(c1, c4, c7)
    i3.save()

    i4.categories.add(c3, c5)
    i4.save()

    i5.categories.add(c6)
    i5.save()

    i6.categories.add(c5)
    i6.save()

    i7.categories.add(c1, c4, c5, c7)
    i7.save()

    i8.categories.add(c1, c3, c4, c7)
    i8.save()