from C4_Capstone.random_person_generator import female_first_name, male_first_name, surname, generate_random_name, \
    random_age, random_email_service, random_phone_number, create_occupation, create_person, read_name_database, get_raw_database
import unittest
from unittest.mock import patch, MagicMock, mock_open

import re

fake_male_first_file = "JAMES          3.318  3.318      1\n" + \
                        "JOHN           3.271  6.589      2\n" + \
                        "ROBERT         3.143  9.732      3\n"

fake_female_first_file = "MARY           2.629  2.629      1\n" +\
                         "PATRICIA       1.073  3.702      2\n" +\
                         "LINDA          1.035  4.736      3\n"

fake_all_last_file = "SMITH          1.006  1.006      1\n" +\
                     "JOHNSON        0.810  1.816      2\n" +\
                     "WILLIAMS       0.699  2.515      3\n"

fake_occupation_file = "Physicist\nProduction or Plant Engineer\nStructural Engineer\n"


class MyTestCase(unittest.TestCase):

    def test_get_raw_database(self):
        mocked_open = mock_open(read_data=fake_male_first_file)

        with patch('C4_Capstone.random_person_generator.open', mocked_open):
            result = get_raw_database("test")

        expected_result = ["JAMES          3.318  3.318      1\n",
                           "JOHN           3.271  6.589      2\n",
                           "ROBERT         3.143  9.732      3\n"]

        self.assertEqual(expected_result, result)

    def test_fail_read_database(self):
        with self.assertRaises(FileNotFoundError):
            read_name_database("no_file")

    def test_read_name_database(self):
        mocked_open = mock_open(read_data=fake_male_first_file)

        with patch('C4_Capstone.random_person_generator.open', mocked_open):
            result = read_name_database("test")

        expected_result = ["JAMES",
                           "JOHN",
                           "ROBERT"]

        self.assertEqual(expected_result, result)


    def test_male_first_name(self):
        mocked_open = mock_open(read_data=fake_male_first_file)

        for i in range(20):
            with patch('C4_Capstone.random_person_generator.open', mocked_open):
                result = male_first_name()

            possible_results = ["James",
                                "John",
                                "Robert"]

            self.assertIn(result, possible_results)

    def test_female_first_name(self):
        mocked_open = mock_open(read_data=fake_female_first_file)

        for i in range(20):
            with patch('C4_Capstone.random_person_generator.open', mocked_open):
                result = female_first_name()

            possible_results = ["Mary",
                                "Patricia",
                                "Linda"]

            self.assertIn(result, possible_results)

    def test_surname(self):
        mocked_open = mock_open(read_data=fake_all_last_file)

        for i in range(20):
            with patch('C4_Capstone.random_person_generator.open', mocked_open):
                result = surname()

            possible_results = ["Smith",
                                "Johnson",
                                "Williams"]

            self.assertIn(result, possible_results)

    @patch("C4_Capstone.random_person_generator.male_first_name")
    @patch("C4_Capstone.random_person_generator.female_first_name")
    @patch("C4_Capstone.random_person_generator.surname")
    def test_generate_random_name(self, mock_surname, mock_female_name, mock_male_name):
        mock_male_name.return_value = "Robert"
        mock_female_name.return_value = "Linda"
        mock_surname.return_value = "Smith"

        for i in range(10):
            result = generate_random_name()

            possible_results = [("male", "Robert", "Smith"), ("female", "Linda", "Smith")]
            self.assertIn(result, possible_results)


    def test_random_age(self):
        sub_tests = [[1, 100], [50, 51]]
        for test in sub_tests:
            with self.subTest(minimum=test[0], maximum=test[1]):
                for _ in range(100):
                    result = random_age(test[0], test[1])
                    self.assertTrue(test[0] <= result <= test[1])

    def test_random_email_service(self):
        possible_providers = ["aol", "gmail", "outlook", "yahoo", "icloud", "yandex"]

        for _ in range(30):
            result = random_email_service()
            self.assertIn(result, possible_providers)

    def test_random_phone_number(self):
        regex_pattern = r"^[1-9]\d{2}-\d{3}-\d{4}$"

        for _ in range(1000):
            result = random_phone_number()
            self.assertTrue(re.findall(regex_pattern, result) != [])


    def test_occupation_adult(self):
        mocked_open = mock_open(read_data=fake_occupation_file)

        for i in range(20):
            with patch('C4_Capstone.random_person_generator.open', mocked_open):
                result = create_occupation(20)

                possible_results = ["Physicist",
                                    "Production or Plant Engineer",
                                    "Structural Engineer"]

                self.assertIn(result, possible_results)


    def test_occupation_child(self):
        mocked_open = mock_open(read_data=fake_occupation_file)

        with patch('C4_Capstone.random_person_generator.open', mocked_open):
            result = create_occupation(3)

            expected_result = "NA"

            self.assertEqual(result, expected_result)


    def test_occupation_student(self):
        mocked_open = mock_open(read_data=fake_occupation_file)

        with patch('C4_Capstone.random_person_generator.open', mocked_open):
            result = create_occupation(14)

            expected_result = "Student"

            self.assertEqual(result, expected_result)

    @patch("C4_Capstone.random_person_generator.create_occupation")
    @patch("C4_Capstone.random_person_generator.random_phone_number")
    @patch("C4_Capstone.random_person_generator.random_email_service")
    @patch("C4_Capstone.random_person_generator.random_age")
    @patch("C4_Capstone.random_person_generator.generate_random_name")
    def test_create_person(self, mock_name, mock_age, mock_email, mock_phone, mock_occupation):
        mock_name.return_value = ("male", "Robert", "Smith")
        mock_age.return_value = 34
        mock_email.return_value = "gmail"
        mock_phone.return_value = "123"
        mock_occupation.return_value = "Occupation"

        result = create_person()
        expected_result = {'first_name': 'Robert', 'last_name': 'Smith', 'email': 'robert.smith@gmail.com', 'sex': 'male', 'age': 34, 'job': 'Occupation', 'phone': '123'}

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
