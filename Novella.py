# coding=windows-1251

from pyclbr import Class


def Title():
    print("-------------------------------")
    print("�������: ������� ������� .DEMO.")
    print("-------------------------------")

def Introduction():
    print("-------------------------------")
    Author = "����� �������: Julian Loki"
    Programmer = "����������� �����������: Julian Loki"
    Scenary = "����������: Julian Loki, Koledloda"
    LinkForSupport = "������ ��� ���������: www.donationalerts.com/r/ton618"
    print(Author)
    print(Programmer)
    print(Scenary)
    print(LinkForSupport)
    print("-------------------------------")

def InfoMainCharacters():
    Name = "������"
    Age = "16"
    Hobby = "GameDesign"
    MainCharacterInfo = [Name, Age, Hobby]
    

def Story():
    print("-------------------------------")
    print("�����:")
    print("�� - ������. ������� ������� �����, �������� �� ������������. ������� ����� ����� �������� ������ ���������� � ��������� ������������. � ���������� �� ������ ����� �������������� ������������ � ����� �����... ������ ���������� ��������������� ������, ����� ���� ��� ���� ������� ������� � ����� �������� ����� ������.")
    print("-------------------------------")


def Game():
    def Day1():
        print("-------------------------------")
        print("���� 1. 2023 ���.")
        print("1 ��������. ������ ������� ���� ����� ������� ����, � ��������� �� ������ ����� ������.")
        print("��� �� ��������?")
        print("1. ����� �� �����.")
        print("2. ����� �� ���������.")
        print("3. ����� �� �����.")
        while True:
            try:
                action = int(input())
                break
            except ValueError:
                print("�� ����� �� ��")
                
        print("��� ����� ����� ������ �������?")
        pet_name = input()
        if action == 1:
            print("-------------------------------")
            InfoMainCharacters()
            message = f"����� �� �����, � �������, ��� ������� \"{pet_name}\" �����."
            print(message)
            print("�������� ������ �����?")
            print("1. ��")
            print("2. ���")
            print("3. ���� � �����")
            
            while True:
                try:
                    a = int(input())
                    break
                except ValueError:
                    print("������ �������� �� ����������")
                     
            if a == 1:
                print("�, ��� ���������� ������, ������ �� ����� ������� ������ ����� � ���������� ������� � ��������� ^-^")
                print("����� ���� ������ �����������, ������ �������������� ���� ����� �����, ��������, ����� ���� ������ ����.")
                print("*����� � �����*")
            elif a == 2:
                print("���� ������, �� ��� ������ �� �� �����, ���-������ �����...")
                print("� ������ �����������, ������ �������������� ���� ����� �����, ��������, ����� ���� ������ ����.")
                print("*����� � �����*")
            elif a == 3:
                print("��� ������ �� ����� �����.") 
                print("*����� � �����*")
            print("-------------------------------")

        elif action == 2:
            print("-------------------------------")
            print("�� ���� �� ���� ���������. ��� �������?")
            print("1. �������� � ����")
            print("2. ������� ������")
            print("3. ����� ������ �����")
     
            Select = int(input())
            if Select == 1:
                print("�� ������ �������� � ���� ������� ����")
                print("...")
                print("...")
                print("...")
                print("������ ����� 7 ����� � ������� ������ ����. � �����, ��� ��������� ������� ����...")
            elif Select == 2:
                print("� �������� ���� ��, ������ ������ �������, ����� ���� �������� �������� ������� ������ � ���������.") 
                print("*������� ���� ������...*")
                print("��� ������� ������, ������� � ����� �����. Zzz...")
            elif action == 3:
                print("������� �����������, �� ������ ����� �� ����� � ���� ��������, ��� ������� ��������� ����� ������, ������ ����������������.")
            
            print("-------------------------------")
            
        elif action == 3:
            students = ["������", "��������", "���������", "�����", "�����", "���", "����", "����", "���", "������"]
            NormalFormatStudents = ", ".join(students)
            teachers = ["�����", "�����", "����", "������", "������"]
            NormalFormatTeachers = ", ".join(teachers)
            
            print("-------------------------------")
            print("������� � ���� ������� ����, � � �� ���� ���������� ������ ����. ���� �������� ���� � �����������.")
            print("���-�, � �������, ��� ������?")
            def select():
                print("1. ���������� ������ �������� � �� ����������")
                print("2. ���������� ������ ��������������")
                print("3. ���������� ���������� ���")
            
                while True:
                    try:
                        action = int(input())
                        break
                    except ValueError:
                        print("�� ����� �� ��")
                    
                if action == 1:
                    print("-------------------------------")
                    print("������ ���� ��������������:")
                    print(NormalFormatStudents)
                    print("���������� ���� ��������������:")
                    print(len(students))
                    print("-------------------------------")
                elif action == 2:
                    print("-------------------------------")
                    print("������ ���� ��������������:")
                    print(NormalFormatTeachers)
                    print("���������� ���� ��������������:")
                    print(len(teachers))
                    print("-------------------------------")
                elif action == 3:
                    print("-------------------------------")
                    



                    print("-------------------------------")
                select()
            select()
            print("*����� �������� ���*")
            print("���, ���� ���� ��� ����� ����������! � ������������ �� ������ ��������������� � ������ ��������. ����� �� ����� ������� �������� :)")
            print("� �� �����, ��� � �� ��������")
            print("-------------------------------")
            
    def Day2():
        ...
    Day1()
        
def Menu():
    print("1. ������ ����")
    print("2. �����")
    print("3. ������������")
    print("4. ����� �� ����")
        
    while True:
            try:
                Select = int(input())
                break
            except ValueError:
                print("�� ����� �� ��")
                
    if Select == 1:
        Game()
    elif Select == 2:
        Story()
        Menu()
    elif Select == 3:
        Introduction()
        Menu()
    elif Select == 4:
        print("�� �������!")
        exit()
    elif Select != 1 or 2 or 3 or 4:
        print("�� ����� �������������� �����, ���������� ������ 1, 2 ��� 3.")
        Menu()                

Title()
Menu()

