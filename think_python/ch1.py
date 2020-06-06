# ch 1
## 1.3 the first program

def hello_world():
    return "Hello World"

def poop_gun():
    return "the ammo is poop"

def letter_capitalizer(letter):
    return letter.upper()

def describe_exercise(function,description='', **kwargs):
    print(function.__name__)
    print(description)
    result = function(**kwargs)
    print(result)

def add_machine(num1,num2):
    return num1+num2

def main():
    # excercise 1.3
    describe_exercise(hello_world,'Prints the phrase "Hello World"')
    hello_world()

    describe_exercise(poop_gun,'Prints the phrase "the ammo is poop"')
    poop_gun()

    lc_kwargs = {'letter': 'b'}
    describe_exercise(letter_capitalizer,'Prints capitalized letter',**lc_kwargs)

    am_kwargs = {'num1': 3, 'num2': 5}
    am_description = "Prints the sum of {num1} and {num2}".format(**am_kwargs)
    describe_exercise(add_machine,am_description,**am_kwargs)

if __name__ == '__main__':
    main()
