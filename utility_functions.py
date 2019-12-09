"""
Created on Sun Dec  1 14:05:32 2019

@author: Loic
"""

import pandas
import sys
import matplotlib.pyplot as plt

def normalize(data, maximum, minimum):
    #Cast numerator as float to return float
    return (float(data - minimum)/(maximum-minimum))

#From stackoverflow
def prepend_file(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def process_file(filename, output_plots=0, labeled=1):

    """
    :param filename:
    :return Min Gyro Z, Max Gyro Z, Index of Min Accel Y, Index of Max Accel Y, Min Gyro X
    """

    falling_score = 'no_label'
    landing_score = 'no_label'
    list_start = 0

    if(labeled):
        output_values = pandas.read_csv(filename, header=0, nrows=0)
        falling_score = str(output_values.columns[0])
        landing_score = str(output_values.columns[1])
        list_start = 1

    data = pandas.read_csv(filename, header=list_start)
    accel_x = list(data.accel_x)
    accel_y = list(data.accel_y)
    accel_z = list(data.accel_z)
    gyro_x = list(data.gyro_x)
    gyro_y = list(data.gyro_y)
    gyro_z = list(data.gyro_z)
    
    #Output Accel_y Gyro_x, Gyro_z

    # Turn literals into ints
    for i in range(0, len(accel_x)):
        accel_x[i] = int(accel_x[i])
        accel_y[i] = int(accel_y[i])
        accel_z[i] = int(accel_z[i])
        gyro_x[i] = int(gyro_x[i])
        gyro_y[i] = int(gyro_y[i])
        gyro_z[i] = int(gyro_z[i])

    # Plot Data

    if(output_plots):
        #a = plt.figure(1)
        #plt.plot(accel_x)
        #plt.title("Accel X")
        

        b = plt.figure(2)
        plt.plot(accel_y)
        plt.title("Accel Y")
        plt.xlabel('Sample Number')
        plt.ylabel('Reading')
        b.savefig('static/accel_y.png')
        b.clf()
        
        #c = plt.figure(3)
        #plt.plot(accel_z)
        #plt.title("Accel Z")
    
        d = plt.figure(4)
        plt.plot(gyro_x)
        plt.title("Gyro X")
        plt.xlabel('Sample Number')
        plt.ylabel('Reading')
        d.savefig('static/gyro_x.png')
        d.clf()

        #e = plt.figure(5)
        #plt.plot(gyro_y)
        #plt.title("Gyro Y")
    
        f = plt.figure(6)
        plt.plot(gyro_z)
        plt.title("Gyro Z")
        plt.xlabel('Sample Number')
        plt.ylabel('Reading')
        f.savefig('static/gyro_z.png')
        f.clf()


    # Extract Features, return to caller function

    # Min/Max Gyro Z
    mingz = 100000
    maxgz = -100000
    for i in range(0, len(gyro_z)):
        if (gyro_z[i] > maxgz):
            maxgz = gyro_z[i]
        if (gyro_z[i] < mingz):
            mingz = gyro_z[i]

    # Difference of Min/Max Index of Accel Y
    miniay = 0
    maxiay = 0
    minay = 100000
    maxay = -100000
    for i in range(0, len(accel_y)):
        if (accel_y[i] > maxay):
            maxay = accel_y[i]
            maxiay = i
        if (accel_y[i] < minay):
            minay = accel_y[i]
            miniay = i

    diff_minmaxay = maxiay - miniay

    # Min Gyro X
    mingx = 100000
    for i in range(0, len(gyro_x)):
        if (gyro_x[i] < mingx):
            mingx = gyro_x[i]

    ret = [mingz, maxgz, diff_minmaxay, mingx, falling_score, landing_score]
    return ret

def main(args):
    if (len(args) != 1):
        print("Usage: utility_functions <file>")
        print("Exiting.")
        exit(-1)
    print(process_file(args[0]))

if __name__ == '__main__':
    main(sys.argv[1:])