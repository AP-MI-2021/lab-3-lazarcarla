def citire_lista():
    l = []
    givenString=input("dati numerele,separate printr-o virgula :")
    numbersAsString=givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def print_menu():
    print("1.Citire lista ")
    print("2.Afisare subsecventa cu cele mai multe numere cu semne alternante")
    print("3.Afisare subsecventa cu cele mai multe numere formate din cifre prime")
    print("4.Afisare subsecventa cu cele mai multe numere formate din cifre pare")
    print("5.Iesire")

def get_longest_alternating_signs(l):
    '''
    determina daca toate numerele au semne alternante in lista
    :param l: lista formata din numere intregi
    :return: True daca lista este formata doar din numere cu semne alternante, sau false in caz contrar
    '''
    if l!=[]:
        if l[0]<0:
            ok=False
        else:
            ok=True
        for i in l[1:]:
            if ok==False and i<0:
                return False
            if ok==True and i>0:
                return False
            ok=not ok
        return True
    return True

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([]) is True
    assert get_longest_alternating_signs([3,4,-6]) is False
    assert get_longest_alternating_signs([4,-5,6,-7]) is True


def cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante(l):
    '''
    determina cea mai lunga subsecventa formata din numere cu semne alternante
    :param l: lista cu elemente intregi
    :return: cea mai lunga subsecventa cu formata din numere cu semne alternante
    '''
    subsecventaMax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if get_longest_alternating_signs(l[i:j + 1]) and len(subsecventaMax) < len(l[i:j + 1]):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante():
    assert cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante([])==[]
    assert cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante([2,-3,4,-7,-7])==[2,-3,4,-7]

def is_prime(x):
    '''
    verificam daca un numar este prim sau nu
    :param x: un numar intreg
    :return: True daca numarul este prim sau false in caz contrar
    '''
    if x<2:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True

def test_is_prime():
    assert is_prime(3) is True
    assert is_prime(4) is False

def get_longest_prime_digits(l):
    '''
    determina daca toate elementele din lista sunt formate din cifre prime
    :param l: lista cu numere intregi
    :return: True daca toate elementele din lista sunt formate din cifre prime, False in caz contrar
    '''
    for x in l:
        if is_prime(x%10)==False:
            return False
            x=x//10
    return True

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([]) is True
    assert get_longest_prime_digits([35,4]) is False
    assert get_longest_prime_digits([3,57])is True

def subsecventa_maxima_cu_elemente_formate_din_cifre_prime(l):
    '''
    determina cea mai lunga subsecventa din lista care are doar numere formate din cifre prime
    :param l: lista cu elemente numere intregi
    :return: subsecventa cea mai lunga formata doar din numere formate doar din cifre prime
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_longest_prime_digits(l[i:j + 1]) and len(subsecventaMax) < len(l[i:j + 1]):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_subsecventa_maxima_cu_elemente_formate_din_cifre_prime():
    assert subsecventa_maxima_cu_elemente_formate_din_cifre_prime([3,35,6,7])==[3,35]
    assert subsecventa_maxima_cu_elemente_formate_din_cifre_prime([4,6])==[]

def get_longest_all_even(l):
    '''
    determina daca toate numerele sunt pare intr-o lista
    :param l: lista cu numerele intregi
    :return: true daca lista este formata doar din numere pare
    '''
    for x in l:
        if x%2!=0:
            return False
    return True

def test_get_longest_all_even():
    assert get_longest_all_even([2,4,6]) is True
    assert get_longest_all_even([2,4,1,13]) is False

def subsecventa_maxima_numere_pare(l):
    '''
    determina cea mai lunga subsecventa formata din numere pare
    :param l: lista cu numere intregi
    :return: subsecventa maxima formata din numere pare
    '''
    subMax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if get_longest_all_even(l[i:j + 1]) and len(subMax) < len(l[i:j + 1]):
                subMax=l[i:j + 1]
    return subMax

def test_subsecventa_maxima_numere_pare():
    assert subsecventa_maxima_numere_pare([2,34,6,5,13])==[2,34,6]
    assert subsecventa_maxima_numere_pare([3,56,4,2,7])==[56,4,2]


def main():
    test_get_longest_alternating_signs()
    test_cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante()
    test_is_prime()
    test_get_longest_prime_digits()
    test_subsecventa_maxima_cu_elemente_formate_din_cifre_prime()
    test_get_longest_all_even()
    test_subsecventa_maxima_numere_pare()
    l=[]
    print_menu()
    while True:

        optiune=input("dati optiune:")
        if optiune=="1":
            l=citire_lista()
        elif optiune=="2":
           print(cea_mai_lunga_subsecventa_cu_numere_cu_semne_alternante(l))

        elif optiune =="3":
            print(subsecventa_maxima_cu_elemente_formate_din_cifre_prime(l))

        elif optiune=="4":
            print(subsecventa_maxima_numere_pare(l))

        else:
            print("optiune gresita ! reincercati!")
main()