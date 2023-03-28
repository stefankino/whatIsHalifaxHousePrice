from webHandling import get_html, parse_html  # import the method from webHandling.py

"""This is the main method at first we input the URL we want """


def main():
    url = 'https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup'  # Target URL
    # put the url into get_html method
    html = get_html(url)
    if html:
        # if this url is not empty, then we can parse the html
        datas = parse_html(html, 'reference internal')
        for data in datas:
            print(data.text.strip())

    else:
        print("getting html failed!")


if __name__ == '__main__':
    main()
# class="Text-c11n-8-84-0__sc-aiai24-0 eIEmla"
