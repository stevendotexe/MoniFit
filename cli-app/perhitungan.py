def bmr(gender, weight, height, age, activity_level): # bmr untuk menghitung jumlah kalori yang dibutuhkan
    if gender == 'l':
        return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * activity_level
    else:
        return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * activity_level
        
def bmi(weight, height):
    return weight / (height * height)

def rda(gender, weight, height, age, activity_level):
    bmr = bmr(gender, weight, height, age, activity_level)
    fat_rda = (bmr * 0.25) / 9  
    protein_rda = weight * 0.8

    return fat_rda, protein_rda

