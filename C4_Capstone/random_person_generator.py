import random
from pathlib import Path
from typing import Tuple

data_folder_path = str(Path(__file__).parent.absolute()) + "/data/"

def get_raw_database(file: str) -> [str]:
    # Reads file and returns list of raw string lines
    try:
        with open(file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
          raise FileNotFoundError(f"File ({file}) was not found.")


def read_name_database(file: str) -> [str]:
    # Reads file and returns a clean list of names/surnames
    raw_data = get_raw_database(file)

    names = []
    for line in raw_data:
        split_line = line.split()
        if len(split_line)  > 0:
            names.append(split_line[0])

    return names

def choose_name_from_file(file_path):
    capitalized_name = random.choice(read_name_database(file_path))
    return capitalized_name

def format_name(name: str) -> str:
    formatted_name = name[0] + name[1:].lower()
    return formatted_name

def choose_and_format_name_from_file(file_path):
    capitalized_name = choose_name_from_file(file_path)
    return format_name(capitalized_name)

def male_first_name() -> str:
    # Iterates through dist.male.first and randomly selects a name.
    file_path = data_folder_path + "dist.male.first"

    return choose_and_format_name_from_file(file_path)


def female_first_name() -> str:
    # Iterates through dist.female.first and randomly selects a name.
    file_path = data_folder_path + "dist.female.first"

    return choose_and_format_name_from_file(file_path)

def surname() -> str:
    # Iterates through dist.all.last and randomly selects a name.
    file_path = data_folder_path + "dist.all.last"

    return choose_and_format_name_from_file(file_path)

def generate_random_name() -> Tuple[str, str, str]:
    # Generates a random first and last name.
    # Returns a tuple with (sex, first_name, last_name)

    sex = random.choice(["male", "female"])

    if sex == "male":
        first = male_first_name()
    else:
        first = female_first_name()

    last = surname()

    return sex, first, last

def random_age(min_age=1, max_age=100) -> int:
  # Generates a random integer which represents age.
  # The default keyword arguments are min and max which represents the minimum and maximum age limits respectively.
  # The function should use a try/except statement to verify that the input is not outside of the range 1-100.
  # If the exception is triggered the function should return the following message:
  # "Enter in min greater than 0 and a max equal or less than one hundred"
    if min_age < 1 or max_age > 100:
        return "Enter in min  greater than 0 and a max equal or less than one hundred"

    age = random.randint(min_age, max_age)

    return age

def random_email_service() -> str:
    # Generates a random email service provider such as aol, gmail, outlook, yahoo, icloud, or yandex.
    possible_providers = ["aol", "gmail", "outlook", "yahoo", "icloud", "yandex"]
    return random.choice(possible_providers)

def random_phone_number() -> str:
    # Generates a random phone number using the following syntax: ###-###-####. The very first digit should not be 0.
    number = ""
    number += str(random.randint(1, 9))
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    number += "-"
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    number += "-"
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    number += str(random.randint(0, 9))
    return number

def create_occupation(age: int) -> str:
    # Returns a random occupation such as cook, actor, programmer, doctor, dentist, uber driver, photographer, or astronaut.
    # If the person's age is less than 4, the job will default ‘NA’, and if the person's age is less than 18 then the job will default to ‘student.’

    if age < 4:
        return "NA"
    if age < 18:
        return "Student"

    file_path = data_folder_path + "occupation"

    raw_data = get_raw_database(file_path)

    return random.choice(raw_data).strip()

def create_person():
    # Builds a dictionary of a random person and returns it. Here’s an example of such a dictionary
    # {'first_name': 'Pasquale', 'last_name': 'Stommes', 'email': 'pasquale.stommes@outlook.com', 'sex': 'male', 'age': 3, 'job': 'NA', 'phone': '343-58-515'}

    sex, first, last = generate_random_name()
    age = random_age()
    email_provider = random_email_service()
    phone = random_phone_number()
    job = create_occupation(age)

    email = f"{first.lower()}.{last.lower()}@{email_provider}.com"

    # noinspection PyDictCreation
    person = {}
    person["first_name"] = first
    person["last_name"] = last
    person["email"] = email
    person["phone"] = phone
    person["age"] = age
    person["sex"] = sex
    person["job"] = job

    return person


