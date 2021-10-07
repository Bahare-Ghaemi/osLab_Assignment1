weight = int(input("enter your weight (KG) : "))
height = float(input("enter your height (m) : "))

BMI = weight / (height*height)

# def test(BMI):
#     return {
#         BMI<18.5: 'You\'r Underweight',
#         18.5<=BMI<24.9: 'You\'r Normal',
#         25<=BMI<29.9: 'You\'r Overweight',
#         30<=BMI<34.9: 'You\'r Obese',
#         35<BMI: 'You\'r Extremly Obese',
#     }.get(BMI, f'{BMI} is not a grade!') 

def BMI_switch(BMI):
    if BMI<18.5:
        print('You\'r Underweight') 
    elif 18.5<=BMI<24.9:
        print('You\'r Normal')
    elif 25<=BMI<29.9:
        print('You\'r Overweight')
    elif 30<=BMI<34.9:
        print('You\'r Obese')
    elif 35<BMI:
        print('You\'r Extremly Obese')


BMI_switch(BMI)