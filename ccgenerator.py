import streamlit as st
import ccard
import random
import time


st.set_page_config(page_title='Enigmatic CC Generator', page_icon='cc.png', layout="centered", initial_sidebar_state="auto", menu_items=None)


def generate_credit_cards1():
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>Gate 1</h1></center>",
        unsafe_allow_html=True)

    cType = st.selectbox('Card Type', ['Visa', 'MasterCard', 'AmericanExpress', 'Discover'])

    quantity = st.number_input('Quantity', min_value=1, max_value=500)
    if st.button('Generate'):

        with st.spinner("Generating credit cards..."):
            time.sleep(3)

            if cType == 'Visa':
                details_list = []
                for i in range(quantity):
                    a = ccard.visa()
                    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    c = random.randint(2023, 2028)
                    d = random.randint(0, 999)
                    output_str = f"{a}|{random.choice(b):02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Visa Card", value="\n".join(details_list), height=200)

            elif cType == 'MasterCard':
                details_list = []
                for i in range(quantity):
                    a = ccard.mastercard()
                    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    c = random.randint(2023, 2028)
                    d = random.randint(0, 999)
                    output_str = f"{a}|{random.choice(b):02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated MasterCard", value="\n".join(details_list), height=200)

            elif cType == 'AmericanExpress':
                details_list = []
                for i in range(quantity):
                    a = ccard.americanexpress()
                    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    c = random.randint(2023, 2028)
                    d = random.randint(0, 9999)
                    output_str = f"{a}|{random.choice(b):02d}|{c}|{d:04d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Amex Card", value="\n".join(details_list), height=200)

            elif cType == 'Discover':
                details_list = []
                for i in range(quantity):
                    a = ccard.discover()
                    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    c = random.randint(2023, 2028)
                    d = random.randint(0, 999)
                    output_str = f"{a}|{random.choice(b):02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Discover Card", value="\n".join(details_list), height=200)


def generate_real_credit_cards2():
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>Gate 2</h1></center>",
        unsafe_allow_html=True)

    bin = st.number_input("Enter BIN (Bank Identification Number)", min_value=0, step=1)
    bin_str = str(int(bin))

    def generate_credit_card_number(bin):
        credit_card_number = str(bin)
        while len(credit_card_number) < 16:
            digit = random.randint(0, 9)
            credit_card_number += str(digit)
        return credit_card_number

    quantity = st.number_input('Quantity', min_value=1, max_value=500)
    month = st.selectbox('Month', ['Random', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                   'September', 'October', 'November', 'December'])
    year = st.selectbox('Year',
                        ['Random', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032'])
    cvv = st.checkbox('Custom CVV')

    if month == 'January':
        b = 1
    elif month == 'February':
        b = 2
    elif month == 'March':
        b = 3
    elif month == 'April':
        b = 4
    elif month == 'May':
        b = 5
    elif month == 'June':
        b = 6
    elif month == 'July':
        b = 7
    elif month == 'August':
        b = 8
    elif month == 'September':
        b = 9
    elif month == 'October':
        b = 10
    elif month == 'November':
        b = 11
    elif month == 'December':
        b = 12
    # --------------------Year----------------
    if year == '2023':
        c = 2023
    elif year == '2024':
        c = 2024
    elif year == '2025':
        c = 2025
    elif year == '2026':
        c = 2026
    elif year == '2027':
        c = 2027
    elif year == '2028':
        c = 2028
    elif year == '2029':
        c = 2029
    elif year == '2030':
        c = 2030
    elif year == '2031':
        c = 2031
    elif year == '2032':
        c = 2032

    d = None

    if cvv:
        d = st.number_input('CVV', min_value=0, max_value=9999) if bin_str[0] == '3' else st.number_input('CVV',
                                                                                                          min_value=0,
                                                                                                          max_value=999)
        e = f"{d:04d}" if bin_str[0] == '3' else f"{d:03d}"

    if st.button('Generate'):
        with st.spinner("Generating credit card details..."):
            time.sleep(3)

            details_list = []
            for i in range(quantity):
                credit_card_number = generate_credit_card_number(bin)
                if month == "Random":
                    b = random.randint(1, 12)
                if year == "Random":
                    c = random.randint(2023, 2032)

                if not cvv:
                    if bin_str[0] == '3':
                        d = random.randint(0, 9999)
                        e = f"{d:04d}"
                    else:
                        d = random.randint(0, 999)
                        e = f"{d:03d}"

                output_str = f"{credit_card_number}|{b:02d}|{c}|{e}"
                details_list.append(output_str)

            st.success("Credit card details generated!")
            text_to_download = "\n".join(details_list)
            st.text_area("Your Generated Card", value=text_to_download, height=200)


def generate_real_credit_cards3():
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>Gate 3</h1></center>",
        unsafe_allow_html=True)

    cType = st.selectbox('Card Type', ['Select One', 'Visa', 'MasterCard', 'AmericanExpress', 'Discover'])

    col1, col2, col3 = st.columns(3)

    with col1:
        quantity = st.number_input('Quantity', min_value=1, max_value=500)
    with col2:
        month = st.selectbox('Month',
                             ['Random', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                              'September', 'October', 'November', 'December'])
    with col3:
        year = st.selectbox('Year',
                            ['Random', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032'])

    cvv = st.checkbox('Custom CVV')
    if cvv:
        if cType == 'AmericanExpress':
            d = st.number_input('Cvv', min_value=0000, max_value=9999)
        else:
            d = st.number_input('Cvv', min_value=000, max_value=999)

    # ------------------Month-------------------

    if month == 'January':
        b = 1
    elif month == 'February':
        b = 2
    elif month == 'March':
        b = 3
    elif month == 'April':
        b = 4
    elif month == 'May':
        b = 5
    elif month == 'June':
        b = 6
    elif month == 'July':
        b = 7
    elif month == 'August':
        b = 8
    elif month == 'September':
        b = 9
    elif month == 'October':
        b = 10
    elif month == 'November':
        b = 11
    elif month == 'December':
        b = 12
    # --------------------Year----------------
    if year == '2023':
        c = 2023
    elif year == '2024':
        c = 2024
    elif year == '2025':
        c = 2025
    elif year == '2026':
        c = 2026
    elif year == '2027':
        c = 2027
    elif year == '2028':
        c = 2028
    elif year == '2029':
        c = 2029
    elif year == '2030':
        c = 2030
    elif year == '2031':
        c = 2031
    elif year == '2032':
        c = 2032

    if st.button('Generate'):
        with st.spinner('Generating...'):
            time.sleep(3)
            if cType == 'Visa':
                details_list = []
                for i in range(quantity):
                    a = ccard.visa()
                    if month == "Random":
                        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        b = random.choice(b1)
                    else:
                        month = b
                    if year == "Random":
                        c = random.randint(2023, 2032)
                    else:
                        year = c
                    if cvv:
                        cvv = d
                    else:
                        d = random.randint(0, 999)
                    output_str = f"{a}|{b:02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Visa Card", value="\n".join(details_list), height=200)

            elif cType == 'MasterCard':
                details_list = []
                for i in range(quantity):
                    a = ccard.mastercard()
                    if month == "Random":
                        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        b = random.choice(b1)
                    else:
                        month = b
                    if year == "Random":
                        c = random.randint(2023, 2032)
                    else:
                        year = c
                    if cvv:
                        cvv = d
                    else:
                        d = random.randint(0, 999)
                    output_str = f"{a}|{(b):02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated MasterCard", value="\n".join(details_list), height=200)

            elif cType == 'AmericanExpress':
                details_list = []
                for i in range(quantity):
                    a = ccard.americanexpress()
                    if month == "Random":
                        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        b = random.choice(b1)
                    else:
                        month = b
                    if year == "Random":
                        c = random.randint(2023, 2032)
                    else:
                        year = c
                    if cvv:
                        cvv = d
                    else:
                        d = random.randint(0, 9999)
                    output_str = f"{a}|{(b):02d}|{c}|{d:04d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Amex Card", value="\n".join(details_list), height=200)

            elif cType == 'Discover':
                details_list = []
                for i in range(quantity):
                    a = ccard.discover()
                    if month == "Random":
                        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                        b = random.choice(b1)
                    else:
                        month = b
                    if year == "Random":
                        c = random.randint(2023, 2032)
                    else:
                        year = c
                    if cvv:
                        cvv = d
                    else:
                        d = random.randint(0, 999)
                    output_str = f"{a}|{(b):02d}|{c}|{d:03d}"
                    details_list.append(output_str)
                with st.container():
                    st.text_area("Your Generated Discover Card", value="\n".join(details_list), height=200)



def main():
    st.sidebar.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>CC Generator</h1></center>",
        unsafe_allow_html=True)
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh2ngUWx46iVDcgGarpdl9kXtBbfNIEkLFBQ&usqp=CAU",
        use_column_width=True)
    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 32px;'>Enigmatic Credit Card Generator</h1></center>",
        unsafe_allow_html=True)

    selected_sidebar = st.sidebar.radio("Please Select One", ["Gate 1", "Gate 2","Gate 3"])

    if selected_sidebar == "Gate 1":
        generate_credit_cards1()
    elif selected_sidebar == "Gate 2":
        generate_real_credit_cards2()
    elif selected_sidebar == "Gate 3":
        generate_real_credit_cards3()


if __name__ == "__main__":
    main()
