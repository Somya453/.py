Course={
    'php':{'duration': '2 Months', 'fees': 15000},
    'java':{'duration': '5 Months', 'fees': 25000},
    'python':{'duration': '4 Months', 'fees': 20000},
}

print(Course)
print(Course['php'])


for k, v in Course.items():
    print(k, v ['duration'], v['fees'])

    