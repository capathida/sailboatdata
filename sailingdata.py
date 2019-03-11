import glob, os

def wind_data(line):
    total_speed_angle = 0
    iterspeed = iter(line)
    next(iterspeed)
    for speed in iterspeed:
        total_speed_angle = total_speed_angle + float(speed)
    #print(line, total_speed_angle)
    return total_speed_angle

def wind_velocity(line):
    #print("Velocity", line) 
    return 0 

def run(line):
    #print("run", line)
    return 0 

def gybe(line):
    #print("gybe", line)
    return 0 

def beat_run(line):
    #print("Beat Angle", line)
    vmg = 0
    iterspeed = iter(line)
    next(iterspeed)
    next(iterspeed)
    for speed in iterspeed:
        vmg = vmg + float(speed)
    #print(line, total_speed_angle)
    return vmg

def not_used(splitted_line):
    #print("Not Used", splitted_line[0])
    return 0

def not_found(splitted_line):
    #print("Not Used", splitted_line[0])
    return 0

def calculator(splitted_line) :
    wind_angle = {
        '52°': wind_data,
        '60°': wind_data,
        '75°': wind_data,
        '90°': wind_data,
        '110°': wind_data,
        '120°': wind_data,
        '135°': wind_data,
        '150°': wind_data
    }
    other_values = {
        #'Run': beat_run,
        'Gybe': gybe,
        #'Beat': beat_run,
        #'Wind': wind_velocity
    }
    # Get the function from wind angle dictionary
    speed_angle = wind_angle.get(splitted_line[0], not_used)
    # Execute the function
    if speed_angle:
        total_speed = speed_angle(splitted_line)

    # Get the function from other values dictionary
    beat_vmg = 0
    if (splitted_line[0] == 'Beat' and splitted_line[1] == 'VMG'):
        beat_vmg = beat_run(splitted_line)
    run_vmg = 0
    if (splitted_line[0] == 'Run' and splitted_line[1] == 'VMG'):
        run_vmg = beat_run(splitted_line)
    other_func = other_values.get(splitted_line[0], not_found)
    # Execute the function
    if other_func:
        other_value = other_func(splitted_line)
    return total_speed/7, beat_vmg/7, run_vmg/7


def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    aggregated_speed = 0
    aggregated_beat_vmg = 0
    aggregated_run_vmg = 0 
    for line in lines:
        splitted_line = line.split()
        speed, beat_vmg, run_vmg = calculator(splitted_line)
        aggregated_speed += speed
        aggregated_beat_vmg += beat_vmg
        aggregated_run_vmg += run_vmg

#print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))
    print("File : %16s, Speed : %5.2f, Beat VMG : % 5.2f, Run VMG : %5.2f" %(filename, aggregated_speed/8, aggregated_beat_vmg, aggregated_run_vmg))

os.chdir("data")
print("BEAT ANGLES: The best course to stear for an upwind course (usually around 45 degrees)")
print("BEAT VMG: The Velocity Made Good, the speed made directly upwind (always less then boat speed)")
print("RUN VMG: The Velocity Made Good, the speed made directly downwind (always less then boat speed)")
print("GYBE ANGLES: the best angle to sail downwind with the best VMG, usually around 150 degrees with little wind and potentially 180 degrees in a lot of wind.")
for file in glob.glob("*.data"):
    main(file)