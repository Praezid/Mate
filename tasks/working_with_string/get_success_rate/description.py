description_declare_variables = """We have improved our program to collect statistics from webinars.
Now, after collecting statistics, it sends data to the server in the form of line 111001010111011,
where 1 - a student who understood the topic, and 0 - respectively, no.
It would be useful to understand what percentage of the group learned the material, it will show how effective the webinar was.
Create a get_success_rate function that takes a statistical string and returns the percentage of students
who understood the material by rounding to the nearest whole number (use rounding to get the result).
Examples:
    -get_success_rate ('11100') == 60
    -get_success_rate ('1100') == 50
    -get_success_rate ('000000') == 0
    -get_success_rate ('11111') == 100
    -get_success_rate ('') == 0"""
