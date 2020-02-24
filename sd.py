import math

set = [1,2,3,4,4,5]
set_mean = 3.17

def sample_sd(data):
    sum1 = []
    length = len(data)
    mean = sum(data)/length
    for i in data:
        sum1.append((i-mean)*(i-mean))
    return math.sqrt((sum(sum1))/(length-1))

def population_sd(data):
    sum1 = []
    length = len(data)
    mean = sum(data)/length
    for i in data:
        sum1.append((i-mean)*(i-mean))
    return math.sqrt((sum(sum1))/length)

def calculate_mean(data):
    length = len(data)
    return sum(data)/length

def cv(sd, mean):
    return (sd / mean)* 100

def run_stats(data, sample_pop):
    sample_standard_dev = sample_sd(data)
    population_standard_dev = population_sd(data)
    the_mean = calculate_mean(data)
    sample_cv = cv(sample_standard_dev, the_mean)
    population_cv = cv(population_standard_dev, the_mean)
    if sample_pop == 'sample':
        return [("Standard-deviation" + "=", sample_standard_dev),( "Mean" + "=", the_mean), ("Coefficient of Variation" + "=", sample_cv)]
    elif sample_pop == 'population':
        return [("Standard-deviation" + "=", population_standard_dev),( "Mean" + "=", the_mean), ("Coefficient of Variation" + "=", population_cv)]
    else:
        return ("Set second variable as 'sample' or 'population'.")
        
    

        
