"""
..............................
. @Name:    Brute Force Tool .
. @Author:  f1nl0wt3ch       .
. @Date:    31.01.2021       .
..............................

"""
import csv
import random
import requests
import argparse
import sys

REQUEST_CUSTOM_HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'cache-control': 'no-cache',
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'origin': 'https://kanataweed.net/',
    'Accept': 'application/json'
}

class ReviewerInfo:
    def __init__(self, firstname, lastname, email, rating, review, comment_post_id):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.rating = rating
        self.review = review
        self.comment_post_id = comment_post_id

    def __iter__(self):
        return iter([self.firstname, self.lastname, self.email, self.rating, self.review, self.comment_post_id])


# Get all lines from file
def _get_all_lines_from_file(file_uri):
    with open(file_uri) as file:
        content = file.readlines()
        return content


# Get data from each line using index and splitter
def _extract_data_from_line_by_index(line, index, split_by):
    word_arr = line.split(split_by)
    return word_arr[index]


# Get all reviews from file
def _get_all_reviews_from_file(file_uri):
    count = 0
    for line in _get_all_lines_from_file(file_uri):
        if len(line.strip()) != 0:
            count += 1
            sys.stdout.write(str(count) + "." + line)


# Get random review
def _get_random_line_from_file(file_uri):
    content = _get_all_lines_from_file(file_uri)
    lines = [line for line in content if len(line.strip()) != 0]
    random_number = _generate_a_random_number_between_two_numbers(0, len(lines) - 1)
    return lines[random_number]


# Print all expected data
def _print_expected_data_from_file(file_uri):
    count = 0
    for line in _get_all_lines_from_file(file_uri):
        if len(line.strip()) != 0:
            count += 1
            sys.stdout.write(_extract_data_from_line_by_index(line, 0, ",").title() + "\n")


# Generate a random rating
def _generate_a_random_number_between_two_numbers(a, b):
    return random.randint(a, b)


# Generate all needed data into a csv file
def _generate_needed_data_into_file(output, number):
    reviewers = []
    for x in range(number):
        last_name = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/lastname.txt")
        first_name = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/firstname.txt")
        domain = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/domains.txt")
        review = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/thanh-review1.txt")
        rating = _generate_a_random_number_between_two_numbers(4, 5)
        email = first_name.strip() + "." + last_name.strip() + "@" + domain.strip()
        comment_post_id = _generate_a_random_number_between_two_numbers(350, 500)
        person_info = ReviewerInfo(first_name, last_name, email.lower(), rating, review, comment_post_id)
        reviewers.append(person_info)
    try:
        with open(output, "w") as file:
            writer = csv.writer(file)
            for reviewer in reviewers:
                writer.writerow(reviewer.__iter__())
    except BaseException as e:
        print("BaseException: ", output)
    else:
        print(str(len(reviewers)) + " lines has been loaded successfully!")

# Create a spam to specific target
def _create_a_single_spam_to_target(target_url, posted_data: ReviewerInfo):
    try:
        jsonPayload={
            "rating": str(posted_data.rating),
            "comment": posted_data.review,
            "author": posted_data.lastname+" "+posted_data.firstname,
            "email": posted_data.email,
            "comment_parent": "0",
            "comment_post_ID": str(posted_data.comment_post_id),
            "wp-comment-cookies-consent": "yes",
            "submit": "Submit",
        }
        response = requests.post(target_url, headers=REQUEST_CUSTOM_HEADER, data=jsonPayload)
        print("-----------------------------------------------------------------------------")
        print("Comment Post ID: ", str(posted_data.comment_post_id))
        print("Status Code: "+str(response.status_code))
        if response.status_code == 302:
            print("Status: OK")
        else:
            print("Status: ERROR")
    except Exception as e:
        print(e)


# Create spams based on a number and target url
def _create_multiple_spam_by_target_and_number(target_url, number):
    for x in range(number):
        last_name = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/lastname.txt")
        first_name = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/firstname.txt")
        domain = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/domains.txt")
        review = _get_random_line_from_file("/Users/Dinh.Thinh/Downloads/thanh-review1.txt")
        rating = _generate_a_random_number_between_two_numbers(4, 5)
        email = first_name.strip() + "." + last_name.strip() + "@" + domain.strip()
        comment_post_id = str(_generate_a_random_number_between_two_numbers(350, 500))
        person_info = ReviewerInfo(first_name, last_name, email.lower(), rating, review, comment_post_id)
        _create_a_single_spam_to_target(target_url, person_info)
    print("----------------------------------------------------")
    print("Task was completed.")
    print("Thank you for using the tool!!!")

def _initialize_arguments():
    parser = argparse.ArgumentParser("f1nl0wt3ch Simple Spam")
    parser.add_argument("-H", "--host", type=str, help=" ==> Target Url That You Want To Send A Spam.")
    parser.add_argument("-N", "--number", type=int, help=" ==> Number Of Spam You Want To Send.")
    args = parser.parse_args()
    return args


def start():
    try:
        # curl --data-urlencode "rating=5&comment=I have used kanataweed for over 3 months now and never had a problem with the service or quality of the weed.  The drivers are very courteous and polite.  I would totally recommend Farmers Link to any and all my friends.  Best service in Scarborough in my opinion.&author=Levy Rayna&email=levi.reyna@gmail.com&wp-comment-cookies-consent=yes&submit=Submit&comment_post_ID=621&comment_parent=0" -X POST https://kanataweed.net/wp-comments-post.php
        args = _initialize_arguments()
        # _print_expected_data_from_file(file_uri=args.path)
        # _generate_needed_data_into_file("/Users/Dinh.Thinh/Downloads/kanataweed.csv", 150)
        _create_multiple_spam_by_target_and_number(target_url=args.host, number=args.number)
        return True
    except Exception as e:
        print(str(e))
        exit(0)


if __name__ == '__main__':
    start()
