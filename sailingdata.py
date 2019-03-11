filename = "data/sailboat.data"

def wind_data(line):
    total_speed = 0
    iterspeed = iter(line)
    next(iterspeed)
    for speed in iterspeed:
        total_speed = total_speed + float(speed)
    print(line, total_speed)

def wind_velocity(line):
    print("Velocity", line)

def run(line):
    print("run", line)

def gybe(line):
    print("gybe", line)

def beat(line):
    print("Beat Angle", line)

def not_found(splitted_line):
    print("Not Found", splitted_line[0])

def switch_demo(splitted_line) :
    switcher = {
        '52°': wind_data,
        '60°': wind_data,
        '75°': wind_data,
        '90°': wind_data,
        '110°': wind_data,
        '120°': wind_data,
        '135°': wind_data,
        '150°': wind_data,
        'Run': run,
        'Gybe': gybe,
        'Beat': beat,
        'Wind': wind_velocity
    }
    # Get the function from switcher dictionary
    func1 = switcher.get(splitted_line[0], not_found)
    # Execute the function
    if func1:
        func1(splitted_line)

with open(filename) as f:
    lines = f.read().splitlines()

for line in lines:
    splitted_line = line.split()
    switch_demo(splitted_line)
