import datetime
import random


class AutoSalon:
    # Car: Manufacturer's name. Graduation year. Model. Cost. Potential sale price.

    def __init__(self, car_fabbric_name, made_year, model, price_for_diller, price_for_client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.car_fabbric_name = car_fabbric_name
        self.made_year = made_year
        self.model = model
        self.price_for_diller = price_for_diller
        self.price_for_client = price_for_client

    def getInfoAutoSalon(self):
        return f'{self.car_fabbric_name}\n' \
               f'{self.model}, {self.made_year}\n' \
               f'diller price: {self.price_for_diller}\n' \
               f'client price: {self.price_for_client}\n' \
               f'expect profit: {self.price_for_client - self.price_for_diller}\n'

    @staticmethod
    def add_Auto():
        add_auto = AutoSalon(input('car_fabbric_name'), input('made_year'), input('model'), int(input('price_for_diller')), int(input('price_for_client')))
        return auto_lst.append(add_auto)

    @staticmethod
    def del_Auto():
        del_auto = input('model auto for delete: ')
        for i in auto_lst:
            if i.model == del_auto:
                auto_lst.remove(i)


class Employees:
    def __init__(self,firstname,lastname,position,tel,email,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.tel = tel
        self.email = email

    def getInfoEmployees(self):
        return f'{self.firstname} {self.lastname}\n' \
               f'{self.position},{self.email},{self.tel}\n'

    @staticmethod
    def add_Employees():
        employees_add = Employees(input('name'), input('lastname'), input('position'), input('tel'), input('email'))
        return employees_lst.append(employees_add)

    @staticmethod
    def del_Employees():
        del_choise_lastname = input('lastname for del: ')
        for i in employees_lst:
            if i.lastname == del_choise_lastname:
                employees_lst.remove(i)


class Sale(AutoSalon,Employees):
    # Sales: Employee. Car. Date of sale. Actual selling price.
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.data = datetime.datetime(random.randrange(2020,2023),random.randrange(1,12),random.randrange(1,30)).strftime("%d/%m/%Y")
    def getInfo(self):
        return f'Who sell: {self.firstname} {self.lastname}\n' \
               f'Position: {self.position}\n' \
               f'Model: {self.model}\n' \
               f'End price: {self.price_for_client}\n' \
               f'Date: {self.data}\n'

    def __lt__(self, other):
        if self.data < other.data:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.data > other.data:
            return True
        else:
            return False

    @staticmethod
    def add_Sales():
        add_salers = input('Who sell "firstname" :')
        add_automodel = input('Model')
        for i in employees_lst:
            if i.firstname == add_salers:
                for ii in auto_lst:
                    if ii.model == add_automodel:
                        res = Sale(**i.__dict__,**ii.__dict__)
                        return sell_lst.append(res)

    @staticmethod
    def del_Sales():
        print('to delete a sale, you need to specify the date of the sale')
        day, month, year = int(input('day: ')), int(input('month: ')), int(input('year: '))
        search_date = datetime.datetime(year, month, day)
        for i in sell_lst:
            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
            if my_dt == search_date:
                # lst.append(f'date: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                print(f'date: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                who_sell = input('Lastname who sold car: ')
                del_auto = input('model auto for delete: ')
                for ii in sell_lst:
                    if ii.lastname == who_sell and ii.model == del_auto:
                        return sell_lst.remove(ii)
        else:
            print(f'"{day}/{month}/{year}" The seller worked very poorly')

    @staticmethod
    def filter():
        while True:
            choise = input(f'\n===this is UI==\nComplete information about the company\'s employees(1)\nFull information about cars(2)\n'
                           f'Complete sales information(3)\nAll sales for a specific date(4)\nAll sales for a specific time period(5)\n'
                           f'All sales of a specific employee(6)\nThe name of the best-selling car during the specified time period(7)\n'
                           f'Information about the most successful seller for the specified time period(8)\n'
                           f'Total profit for the specified time period(9)\n'
                           f'Total profit for ALLTIME time period(10)\n'
                           f'Add employees(12)\n'
                           f'Del employees(13)\n'
                           f'Add Auto(14)\n'
                           f'Del Auto(15)\n'
                           f'Add sell info(16)\n'
                           f'Del sell info(17)\n'
                           f'exit(11)\n'
                           f'choise (1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17 or 11 - for exit)?: ')

            if choise == '1':
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                print(('---this info all about Employees---').upper())
                if save_or_write == '1':
                    for i in employees_lst:
                        print(Employees.getInfoEmployees(i))
                elif save_or_write == '2':
                    with open('auto_salon_info.txt', 'a+') as file:
                        file.write((f'\n---this info all about Employees---\n').upper())
                    for i in employees_lst:
                        with open('auto_salon_info.txt','a+') as file:
                            file.write(f'{Employees.getInfoEmployees(i)}\n')
                            file.close()
            elif choise == '2':
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---This info all about Auto---').upper())
                    for i in auto_lst:
                        print(AutoSalon.getInfoAutoSalon(i))
                elif save_or_write == '2':
                    with open('auto_salon_info.txt', 'a+') as file:
                        file.write((f'\n---This info all about Auto---\n').upper())
                        for i in auto_lst:
                            file.write(f'{AutoSalon.getInfoAutoSalon(i)}\n')
                        file.close()
            elif choise == '3':
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---This info all about Sale---').upper())
                    for i in sell_lst:
                        print(Sale.getInfo(i))
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write((f'\n---This info all about Sale---\n').upper())
                        for i in sell_lst:
                            file.write(f'{Sale.getInfo(i)}\n')
                        file.close()
            elif choise == '4':
                # All sales for a specific date
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('All sales per last date').upper())
                    day, month, year = int(input('day: ')), int(input('month: ')), int(input('year: '))
                    search_date = datetime.datetime(year, month, day)
                    for i in sell_lst:
                        my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                        if my_dt == search_date:
                            print(f'date: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                    else:
                        print(f'"{day}/{month}/{year}" The seller worked very poorly')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write(f'\n---All sales per last date---\n'.upper())
                        day, month, year = int(input('day: ')), int(input('month: ')), int(input('year: '))
                        search_date = datetime.datetime(year, month, day)
                        for i in sell_lst:
                            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                            if my_dt == search_date:
                                file.write(f'date: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                        else:
                            file.write(f'"{search_date}" The seller worked very poorly')
                            file.close()
            elif choise == '5':
                # All sales for a specific time period
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---All sales for a certain period---').upper())
                    day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(input('year_from: '))
                    #day_from, month_from, year_from = 1,1,2022#TEST
                    date_from = datetime.datetime(year_from, month_from, day_from)
                    day_until, month_until, year_until = int(input('day_until: ')), int(input('month_until: ')), int(input('year_until: '))
                    #day_until, month_until, year_until = 30,12,2022#TEST
                    date_until = datetime.datetime(year_until, month_until, day_until)
                    count = 0
                    for i in sell_lst:
                        my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                        if date_from < my_dt < date_until:
                            count +=1
                            print(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                        else:
                            continue
                    print(f'Results found "{count}"')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write(f'\n---All sales for a certain period---\n'.upper())
                        day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(
                            input('year_from: '))
                        # day_from, month_from, year_from = 1,1,2022#TEST
                        date_from = datetime.datetime(year_from, month_from, day_from)

                        day_until, month_until, year_until = int(input('day_until: ')), int(
                            input('month_until: ')), int(input('year_until: '))
                        # day_until, month_until, year_until = 30,12,2022#TEST
                        date_until = datetime.datetime(year_until, month_until, day_until)
                        count = 0
                        for i in sell_lst:
                            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                            if date_from < my_dt < date_until:
                                count += 1
                                #print(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                                file.write(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                            else:
                                continue
                        file.write(f'Results found "{count}"')
                        file.close()
            elif choise == '6':
                # All sales of a specific employee
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---all sales of a specific employee---').upper())
                    lastname_employees = input('lastname employees: ')
                    if lastname_employees == '':
                        print('not found')
                    else:
                        iteration = [f'{i.position}: {i.firstname} {i.lastname}\n'
                                      f'date: {i.data} sell: {i.car_fabbric_name} {i.model}\n'
                                      f'price: {i.price_for_client}\n' for i in sell_lst if lastname_employees in i.lastname ]
                        if len(iteration)>0:
                            for i in [i for i in iteration]:
                                print(i)
                        else:
                            print(f'"{lastname_employees}" not found')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write(f'\n---all sales of a specific employee---\n'.upper())
                        lastname_employees = input('lastname employees: ')
                        if lastname_employees == '':
                            file.write('not found')
                        else:
                            iteration = [f'{i.position}: {i.firstname} {i.lastname}\n'
                                         f'date: {i.data} sell: {i.car_fabbric_name} {i.model}\n'
                                         f'price: {i.price_for_client}\n' for i in sell_lst if
                                         lastname_employees in i.lastname]
                            if len(iteration) > 0:
                                for i in [i for i in iteration]:
                                    print(i)
                            else:
                                file.write(f'"{lastname_employees}" not found')
                        file.close()
            elif choise == '7':
                '''Назва автомобіля, що найбільше продається за вказаний період часу'''
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---The name of the best-selling car during the specified time period---').upper())
                    day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(input('year_from: '))
                    #day_from, month_from, year_from = 1,1,2022#TEST
                    date_from = datetime.datetime(year_from, month_from, day_from)
                    day_until, month_until, year_until = int(input('day_until: ')), int(input('month_until: ')), int(input('year_until: '))
                    #day_until, month_until, year_until = 30,12,2022#TEST
                    date_until = datetime.datetime(year_until, month_until, day_until)
                    lst_for_search_result_date = []
                    count = 0
                    for i in sell_lst:
                        my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                        if date_from < my_dt < date_until:
                            count += 1
                            print(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                            lst_for_search_result_date.append(i)
                        else:
                            continue
                    #####
                    lst_repeat_lastname = [i.model for i in lst_for_search_result_date]
                    lst_count = []
                    for i in lst_repeat_lastname:
                        lst_count.append(lst_repeat_lastname.count(i))
                    index_best_seller = lst_count.index(max(lst_count))
                    best_auto_seller = lst_repeat_lastname[index_best_seller]
                    count = 0
                    for i in lst_for_search_result_date:
                        if i.model == best_auto_seller:
                            count += 1
                    print((f'\nFrom {date_from.date()} to {date_until.date()}\n"{best_auto_seller}" the best seller!\n'
                          f'Sold "{count}" auto {best_auto_seller}\n').upper())
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write(f'\n---The name of the best-selling car during the specified time period---\n'.upper())
                        day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(input('year_from: '))
                        #day_from, month_from, year_from = 1, 1, 2022  # TEST
                        date_from = datetime.datetime(year_from, month_from, day_from)
                        day_until, month_until, year_until = int(input('day_until: ')), int(input('month_until: ')), int(input('year_until: '))
                        #day_until, month_until, year_until = 30, 12, 2022  # TEST
                        date_until = datetime.datetime(year_until, month_until, day_until)
                        lst_for_search_result_date = []
                        count = 0
                        for i in sell_lst:
                            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                            if date_from < my_dt < date_until:
                                count += 1
                                file.write(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                                lst_for_search_result_date.append(i)
                            else:
                                continue
                        #####
                        lst_repeat_lastname = [i.model for i in lst_for_search_result_date]
                        lst_count = []
                        for i in lst_repeat_lastname:
                            lst_count.append(lst_repeat_lastname.count(i))
                        index_best_seller = lst_count.index(max(lst_count))
                        best_auto_seller = lst_repeat_lastname[index_best_seller]
                        count = 0
                        for i in lst_for_search_result_date:
                            if i.model == best_auto_seller:
                                count += 1
                        file.write((f'\nFrom {date_from.date()} to {date_until.date()}\n"{best_auto_seller}" the best seller!\n'
                                  f'Sold "{count}" auto {best_auto_seller}\n').upper())
                        file.close()
            elif choise == '8':
                # Information about the most successful seller for the specified time period
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---Information about the most successful seller for the specified time period---').upper())
                    day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(input('year_from: '))
                    #day_from, month_from, year_from = 1,1,2022#TEST
                    date_from = datetime.datetime(year_from, month_from, day_from)
                    day_until, month_until, year_until = int(input('day_until: ')), int(input('month_until: ')), int(input('year_until: '))
                    #day_until, month_until, year_until = 30,12,2022#TEST
                    date_until = datetime.datetime(year_until, month_until, day_until)
                    lst_for_search_result_date = []
                    count = 0
                    for i in sell_lst:
                        my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                        if date_from < my_dt < date_until:
                            count += 1
                            print(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                            lst_for_search_result_date.append(i)
                        else:
                            continue
                    #####
                    lst_repeat_lastname = [i.lastname for i in lst_for_search_result_date]
                    lst_count = []
                    for i in lst_repeat_lastname:
                        lst_count.append(lst_repeat_lastname.count(i))
                    index_best_seller = lst_count.index(max(lst_count))
                    best_employees = lst_repeat_lastname[index_best_seller]
                    count = 0
                    for i in lst_for_search_result_date:
                        if i.lastname == best_employees:
                            count += i.price_for_client
                    print(f'\n#From "{day_from}/{month_from}/{year_from}" to "{day_until}/{month_until}/{year_until}"\n'
                                   f'"{best_employees}" the best seller!\n'
                                   f'Sold for {count}$\n')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt','a+') as file:
                        file.write(f'\n---Information about the most successful seller for the specified time period---\n'.upper())
                        day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(
                            input('year_from: '))
                        # day_from, month_from, year_from = 1,1,2022#TEST
                        date_from = datetime.datetime(year_from, month_from, day_from)

                        day_until, month_until, year_until = int(input('day_until: ')), int(
                            input('month_until: ')), int(input('year_until: '))
                        # day_until, month_until, year_until = 30,12,2022#TEST
                        date_until = datetime.datetime(year_until, month_until, day_until)
                        lst_for_search_result_date = []
                        count = 0
                        for i in sell_lst:
                            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                            if date_from < my_dt < date_until:
                                count += 1
                                file.write(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                                lst_for_search_result_date.append(i)
                            else:
                                continue
                        #####
                        lst_repeat_lastname = [i.lastname for i in lst_for_search_result_date]
                        lst_count = []
                        for i in lst_repeat_lastname:
                            lst_count.append(lst_repeat_lastname.count(i))
                        index_best_seller = lst_count.index(max(lst_count))
                        best_employees = lst_repeat_lastname[index_best_seller]
                        count = 0
                        for i in lst_for_search_result_date:
                            if i.lastname == best_employees:
                                count += i.price_for_client
                        file.write(f'\n#From "{day_from}/{month_from}/{year_from}" to "{day_until}/{month_until}/{year_until}"\n'
                                   f'"{best_employees}" the best seller!\n'
                                   f'Sold for {count}$\n')
                        file.close()
            elif choise == '9':
                # Total profit for the specified period of time
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---Total profit for the specified time period---').upper())
                    day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(input('year_from: '))
                    #day_from, month_from, year_from = 1,1,2022#TEST
                    date_from = datetime.datetime(year_from, month_from, day_from)
                    day_until, month_until, year_until = int(input('day_until: ')), int(input('month_until: ')), int(input('year_until: '))
                    #day_until, month_until, year_until = 30,12,2022#TEST
                    date_until = datetime.datetime(year_until, month_until, day_until)
                    lst_for_search_result_date = []
                    count = 0
                    for i in sell_lst:
                        my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                        if date_from < my_dt < date_until:
                            count += 1
                            print(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                            lst_for_search_result_date.append(i)
                        else:
                            continue
                    diller_pay = sum([i.price_for_diller for i in lst_for_search_result_date])
                    client_pay = sum([i.price_for_client for i in lst_for_search_result_date])
                    dirty_profit = client_pay - diller_pay
                    print(f'dirty profit from {date_from.date()} to {date_until.date()}: {dirty_profit}$')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt', 'a+') as file:
                        file.write(f'\n---Total profit for the specified time period---\n'.upper())
                        day_from, month_from, year_from = int(input('day_from: ')), int(input('month_from: ')), int(
                            input('year_from: '))
                        # day_from, month_from, year_from = 1,1,2022#TEST
                        date_from = datetime.datetime(year_from, month_from, day_from)

                        day_until, month_until, year_until = int(input('day_until: ')), int(
                            input('month_until: ')), int(input('year_until: '))
                        # day_until, month_until, year_until = 30,12,2022#TEST
                        date_until = datetime.datetime(year_until, month_until, day_until)
                        lst_for_search_result_date = []
                        count = 0
                        for i in sell_lst:
                            my_dt = datetime.datetime.strptime(i.data, "%d/%m/%Y")
                            if date_from < my_dt < date_until:
                                count += 1
                                file.write(f'\ndate: {i.data}\n{i.position} - {i.lastname}\n{i.model} - {i.price_for_client}\n')
                                lst_for_search_result_date.append(i)
                            else:
                                continue
                        diller_pay = sum([i.price_for_diller for i in lst_for_search_result_date])
                        client_pay = sum([i.price_for_client for i in lst_for_search_result_date])
                        dirty_profit = client_pay - diller_pay
                        file.write(f'dirty profit from {date_from.date()} to {date_until.date()}: {dirty_profit}$')
                        file.close()
            elif choise == '10':
                '''Сумарний прибуток за ALLTIME період часу'''
                save_or_write = input('print info(1), save in file(2):\nchoise 1 or 2?: ')
                if save_or_write == '1':
                    print(('---Total profit for ALLTIME time period---').upper())
                    diller_pay = sum([i.price_for_diller for i in sell_lst])
                    client_pay = sum([i.price_for_client for i in sell_lst])
                    dirty_profit = client_pay - diller_pay
                    print(f'dirty profit: {dirty_profit}$')
                elif save_or_write == '2':
                    with open('auto_salon_info.txt', 'a+') as file:
                        file.write(f'\n\n---Total profit for ALLTIME time period---\n'.upper())
                        diller_pay = sum([i.price_for_diller for i in sell_lst])
                        client_pay = sum([i.price_for_client for i in sell_lst])
                        dirty_profit = client_pay - diller_pay
                        file.write(f'dirty profit: {dirty_profit}$')
                        file.close()
            elif choise == '11':
                print('end program')
                '''turkey dismiss real middle fresh (system soda hurt mango fiber green erupt)'''
                #print(f'the report ended on {datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")}')
                with open('auto_salon_info.txt', 'a+') as file:
                    file.write(f'\nend program {datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")}')
                    file.close()
                break
            elif choise == '12':
                Employees.add_Employees()
            elif choise == '13':
                Employees.del_Employees()
            elif choise == '14':
                AutoSalon.add_Auto()
            elif choise == '15':
                AutoSalon.del_Auto()
            elif choise == '16':
                Sale.add_Sales()
            elif choise == '17':
                Sale.del_Sales()
            else:
                file.write(f'\nsomething wrong\nend program {datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")}')
                file.close()


# Car: Manufacturer's name. Graduation year. Model. Cost. Potential sale price.
auto1 = AutoSalon(car_fabbric_name='vw',made_year=2023,model='passat',price_for_diller=50_000,price_for_client=57_000)
auto2 = AutoSalon('tesla',2022,'model x',90_000,103_000)
auto3 = AutoSalon('mersedes',2021,'e400',73_000,79_000)
auto4 = AutoSalon('toyota',2020,'land cruiser',90_000,99_000)
auto5 = AutoSalon('audi',2019,'q7',130_000,147_000)
auto6 = AutoSalon('audi',2021,'q5',75_000,77_500)
auto7 = AutoSalon('audi',2023,'q3',70_000,73_000)
auto8 = AutoSalon('audi',2022,'q2',53_000,59_000)
auto9 = AutoSalon('audi',2023,'sq7',133_000,139_000)
auto10 = AutoSalon('audi',2019,'sq5',71_000,79_000)
auto11 = AutoSalon('audi',2019,'sq2',55_000,59_000)
# Full information about cars.
auto_lst = [auto1,auto2,auto3,auto4,auto5,
            auto6,auto7,auto8,auto9,auto10,auto11]

# Employee: surname first name. Position. Contact phone number. Email.
employees1 = Employees('Bogdan','Shevchenko','seller','+30123756789','bgd@test.com')
employees2 = Employees('Mark','Regf','manager','+30008302731','mark@test.com')
employees3 = Employees('Marta','Gonzalez','saler','+31109922731','mrt@salon.com')
employees4 = Employees('Max','Emm','seller','+30751002731','memm@salon.com')

'''Complete information about the company's employees.'''
employees_lst = [employees1,employees2,employees3,employees4]

# for test
# Sales: Employee. Car. Date of sale. Actual selling price.
sell_1 = Sale(**auto2.__dict__,**employees4.__dict__)
sell_2 = Sale(**auto1.__dict__,**employees2.__dict__)
sell_3 = Sale(**auto11.__dict__,**employees4.__dict__)
sell_4 = Sale(**auto3.__dict__,**employees2.__dict__)
sell_5 = Sale(**auto4.__dict__,**employees1.__dict__)
sell_6 = Sale(**auto5.__dict__,**employees1.__dict__)
sell_7 = Sale(**auto6.__dict__,**employees3.__dict__)
sell_8 = Sale(**auto7.__dict__,**employees3.__dict__)
sell_9 = Sale(**auto8.__dict__,**employees2.__dict__)
sell_10 = Sale(**auto9.__dict__,**employees2.__dict__)
sell_11 = Sale(**auto10.__dict__,**employees2.__dict__)
sell_12= Sale(**auto11.__dict__,**employees4.__dict__)
sell_13 = Sale(**auto5.__dict__,**employees1.__dict__)
sell_14 = Sale(**auto6.__dict__,**employees1.__dict__)
sell_15 = Sale(**auto3.__dict__,**employees1.__dict__)
sell_16 = Sale(**auto7.__dict__,**employees2.__dict__)
sell_17 = Sale(**auto10.__dict__,**employees3.__dict__)
sell_18 = Sale(**auto4.__dict__,**employees3.__dict__)
sell_19 = Sale(**auto5.__dict__,**employees4.__dict__)
sell_20 = Sale(**auto3.__dict__,**employees1.__dict__)
sell_21 = Sale(**auto8.__dict__,**employees4.__dict__)
sell_22 = Sale(**auto9.__dict__,**employees1.__dict__)


# Full information about the sale
sell_lst = [
    sell_1,sell_2,sell_3,sell_4,sell_5,sell_6,sell_7,sell_8,
    sell_9,sell_10,sell_11,sell_12,sell_13,sell_14,sell_15,sell_16,
    sell_17,sell_18,sell_19,sell_20,sell_21,sell_22
]
