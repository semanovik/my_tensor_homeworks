input_user = input("Введите имя в формате ИФО: ")
name_input = input_user.split()[0]
surname_input = input_user.split()[1]
patronymic_input = " "

format_input = input('Введите формат: ')

if len(input_user.split()) == 3:
    patronymic_input = input_user.split()[2]


class Name:

    def __init__(self, name, surname, patronymic):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.patronymic = patronymic.capitalize()

    def brief_name(self):
        print(f'{self.surname} {self.name}')

    def initials(self):
        if self.patronymic == ' ':
            print(f'{self.surname} {self.name[0]}.')
        else:
            print(f'{self.surname} {self.name[0]}.{self.patronymic[0]}.')

    def strfname(self, format_name):

        if '%И' in format_name:
            format_name = format_name.replace('%И', self.name)
        if '%и.' in format_name:
            format_name = format_name.replace('%и.', self.name[0]+'.')
        if '%Ф' in format_name:
            format_name = format_name.replace('%Ф', self.surname)
        if '%ф.' in format_name:
            format_name = format_name.replace('%ф.', self.surname[0]+'.')
        if '%О' in format_name:
            format_name = format_name.replace('%О', self.patronymic)
        if '%о.' in format_name:
            format_name = format_name.replace('%о.', self.patronymic[0]+'.')

        print(format_name)


guy = Name(name_input, surname_input, patronymic_input)
guy.brief_name()
guy.initials()

guy.strfname(format_input)
