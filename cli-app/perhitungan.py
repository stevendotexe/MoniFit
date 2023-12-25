# current mode: weight loss

def bmr(gender, weight, height, age, activity_level): # bmr untuk menghitung jumlah kalori yang dibutuhkan
    height = height/100
    if gender == 'l':
        return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * activity_level
    else:
        return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * activity_level
        
def bmi(weight, height):
    return(weight / ((height/100)*height) * 100)

def rda(gender, weight, height, age, activity_level):
    # adjusted for weight loss
    bmrr = bmr(gender, weight, height, age, activity_level) 
    carbs_rda = (bmrr * .5)
    protein_rda = (bmrr * 0.25)
    fat_rda = (bmrr * 0.25)
    
    return carbs_rda, fat_rda, protein_rda

