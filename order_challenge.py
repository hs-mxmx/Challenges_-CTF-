
import requests
from BeautifulSoup import BeautifulSoup


def sort(string):
    string = string.split(", ")
    return ", ".join(sorted(string))

problem_url = "https://www.hackthis.co.uk/levels/coding/1"
login_url = "https://www.hackthis.co.uk/?login"
payload_login = {"username": "USER", "password": "PASS"}

def login_page(url, target_url,payload):
    session = requests.Session()
    login = session.post(url, payload)
    problem_url = session.get(target_url)

    html_text = problem_url.text
    parsed_html_content = BeautifulSoup(problem_url.content)
    parsed_html = BeautifulSoup(problem_url.text)

    # Getting textarea
    get_textarea = parsed_html.findAll("textarea")
    string = str(get_textarea)
    string_left = string[11:]
    string_right = string_left[:-49]
    print(string_right)

    #problem = html_text[html_text.find("<textarea>")+10:html_text.find("</textarea>")]
    #solution = sort(string_right)

    payload_solution = {"answer": solution}

    result = session.post(target_url, data=payload_solution)
    response = session.get(target_url).text

    if "Incomplete" in response:
        print("Not solved.")
    else:
        print("Solved.")

    print(solution)


login_page(login_url, problem_url, payload_login)

#html_code = login_page(login, url, payload)
#print(html_code)
