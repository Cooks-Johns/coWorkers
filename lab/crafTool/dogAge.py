
class DogAge:
    ppl_years = int(input("Enter the dogs age in human years: "))
    print()

    dog_age = 7 * ppl_years

    print('Your dog is', ppl_years, 'years old in human years and ', end='')
    print(dog_age, 'yrs old in dog years.')