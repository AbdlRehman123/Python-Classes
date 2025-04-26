# import streamlit as st

st.title("Welcome to class ")
st.header("Heading 1")
st.write("Ramzan and Holi Mubarak")
# input
name = st.text_input("Enter your name")

agree=st.checkbox("I agree")
if agree:
    st.write("I agree")

    if st.botton("Click me"):
        st.write(f"My name is {name}.")
        # to run streamlit run filename



st.title("Counter")

if "count" not in st.session_state: #store data
    st.session_state["Count"]=0
    st.session_state = 0
count=0 # temporary data lost
st.header(st.session_state,count)

col1, col2 =st.columns(2)
print("Count>>>",st.session_state.count)
with col1:
    if st.button("Increment"):
        st.session_state.count +=1

        with col2:
            if st.button("Decrement"):
                st.session_state.count -=1
                # store data
                # st.write(st.session_state)

import streamlit as st

st.title("Welcome to class ")
st.header("Heading 1")
st.write("Ramzan and Holi Mubarak")
# input
name = st.text_input("Enter your name")

agree=st.checkbox("I agree")
if agree:
    st.write("I agree")

    if st.button("Click me"): # Corrected typo: 'botton' to 'button'
        st.write(f"My name is {name}.")
        # to run streamlit run filename


st.title("Counter")

if "count" not in st.session_state: #store data
    st.session_state["count"]=0 # Corrected key to 'count' to match usage
    # st.session_state = 0  # Removed this line, as it was overwriting the session state dictionary
count=0 # temporary data lost
st.header(f"Count: {st.session_state.count}, {count}") # Updated header display

col1, col2 =st.columns(2)
print("Count>>>",st.session_state.count)
with col1:
    if st.button("Increment"):
        st.session_state.count +=1

with col2: # Moved this outside the 'Increment' button's block
    if st.button("Decrement"):
        st.session_state.count -=1
        # store data
        # st.write(st.session_state)

def weight_converter(value,from_unit,to_unit):
 weight_unit = {'kilogram': 1 , 'pound':2.20462 , 'gram':1000 , 'ounce':35.274}
def weight_converter(value,from_unit,to_unit):
 weight_unit = {'kilogram': 1 , 'pound':2.20462 , 'gram':1000 , 'ounce':35.274}
 return(value / weight_unit[from_unit])*weight_unit[to_unit]
def area_converter(value, from_unit, to_unit):
 area_unit={'squaremeter': 1 , 'acre':4046.86 , 'squareyed':0.836127, 'square kilo':1000000}
 return(value / area_unit[from_unit])*area_unit[to_unit]
if st.button("convert"):
  if conversion_type == "lenght":
    result = lenght_converter(value, from_unit, to_unit)
elif conversion_type == "weight":
  result = weight_converter(value, from_unit, to_unit)
elif conversion_type == "area":
  result = area_converter(value, from_unit, to_unit)
st.write("result>>>",result)

# import streamlit as st # Importing streamlit

def weight_converter(value, from_unit, to_unit):
    weight_unit = {'kilogram': 1, 'pound': 2.20462, 'gram': 1000, 'ounce': 35.274}
    return (value / weight_unit[from_unit]) * weight_unit[to_unit]

def area_converter(value, from_unit, to_unit):
    area_unit = {'squaremeter': 1, 'acre': 4046.86, 'squareyed': 0.836127, 'square kilo': 1000000}
    return (value / area_unit[from_unit]) * area_unit[to_unit]

# Assume lenght_converter is defined similarly to the others
def lenght_converter(value, from_unit, to_unit):
    # Replace this with the actual logic for length conversion
    # This is just a placeholder
    length_unit = {'meter': 1, 'kilometer': 1000, 'centimeter': 0.01, 'millimeter': 0.001}
    return (value / length_unit[from_unit]) * length_unit[to_unit]

# Need to get

def weight_converter(value,from_unit,to_unit):
 weight_unit = {'kilogram': 1 , 'pound':2.20462 , 'gram':1000 , 'ounce':35.274}
 return(value / weight_unit[from_unit])*weight_unit[to_unit]
def area_converter(value, from_unit, to_unit):
    area_unit={'squaremeter': 1 , 'acre':4046.86 , 'squareyed':0.836127, 'square kilo':1000000} # Added value for 'square kilo'
    return(value / area_unit[from_unit])*area_unit[to_unit] # Indented return statement
import streamlit as st
if st.button("convert"):
 if conversion_type == "lenght":
  result = lenght_converter(value, from_unit, to_unit)
 elif conversion_type == "weight":
  result = weight_converter(value, from_unit, to_unit)
 elif conversion_type == "area": # Corrected condition
  result = area_converter(value, from_unit, to_unit)
st.write("result>>>",result)

try:
    print("1 - length\n2 - Temperature")
    choise = int(input("Enter Your Choiase:")) # 1 =Length 2= Temperature

    # code for length
    if choise == 1:
        length = float(input("Enter Your lemgth in meter:"))
        print("1 - kilometer \n2 - Feet")
        # take choise as input
        length_choise = int(input("Enter Your Choise:")) # 1 = Kilometer, 2 = meter
        if length_choise == 1:
            print(f"{length/1000} kilometer")
        elif length_choise == 2:
            print(f"{length * 3.28084} Feet")
        else:
            print('Invalid choise')

    # code for temperature
    elif choise == 2:
        temp = float(input("Enter your temperature in celcius :"))
        print(f"{(temp * 9/5) + 32} Farenheit")

    else:
        print('INVALID CHOISE')

except:
    print('Please try again')

def check_password_strength(password):
    # strength levels
    # Initialize strength_score, strength, and feedback within the function
    strength_score = 0
    strength = ""
    feedback = []

    # ... (Your logic to calculate strength_score, strength, and feedback) ...

    if strength_score == 5:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    return {"strength": strength, "score": strength_score, "feedback": feedback}

# import streamlit as st  # Import the streamlit library

# streamlit ui
st.title("password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check password"):
    if password:
        result = check_password_strength(password)
        st.write(f"### Strength: {result['strength']}")
        st.progress(result['score']/5)

        if result['feedback']:
            st.write("123SairKanwal1456#@")
            for tip in result ['feedback']:
                st.write(f"-{tip}")

import streamlit as st  # Import the streamlit library

# streamlit ui
st.title("password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check password"):
    if password:
        result = check_password_strength(password)
        st.write(f"### Strength: {result['strength']}")
        st.progress(result['score']/5)

        if result['feedback']:
            st.write("123SairKanwal1456#@")
            for tip in result ['feedback']:
                st.write(f"-{tip}")

#libaray Mangement System - Python project
#A libaray mangenment system keeps track of the books present in the libary. It is an important piece
# of software which is a must at schools and collleges

book_list = list()
# menu items
menue = """
  1) Add Book
  2) Remove Book
  3) Veiw book
  4) Press E to Exit
  """
#add books
def add_book(book_list, book):
    book_list.append(book)
    print("book added sucessfully")
#removed books
def remove_book(booklist, book):
   if book in booklist:
       booklist.remove(book)
       print("book remove sucessfully")
   else:
       print("book not found in this list")

#display all books results
def display_list(booklist,book):
    if booklist:
        print("added book ->",", ".join(booklist))
    else:
        print("No books in the list.")
#exit program
def exit_program():
    print("thank you for visiting the book libaray system.")
    quit()

    #main program loop
    while True:
        print(menu)
        choice = input("your choice: ")

        if choice == "1": #add book
            book_name == input("Enter the book name you want to add:" )
            add_book(book_list, book_name)

        elif choice == "2": #remove book
            book_name = input("enter the book name to remove: ")
            remove_book(book_list, book_name)

        elif choise == "3": # view book list
            display_list(book_list)

        elif choise.lower() == "e": # exit programme
            exit_pragram()

    else:
        print("invalid entry")
        input("press enter to return to the main menu")

import streamlit as st
import json

# load & save library data
def load_library():
    try:
        with open ("library.json", "r") as file:
            return json.load(file)
    except FileExistsError:
        return []

def save_library():
    with open("library.json", "w") as file:
        json.dump(library,file,indent=4)

# initialize library
library = load_library()

st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an option",["Veiw library","remove book","search book","save and exit" ])
if menu == "Veiw library":
    st.sidebar("Your library")
    if library:
            st.table(library)
    else:
            st.write("no book in your library. add some books!")

#Add book
elif menu == "Add Book":
     st.sidebar('Add a new book')
     title = st.text_input("Title")
     author  = st.text_input("Aythor")
     year = st.number_input("Year",min_value=2022, max_value=2100,steps=1)
     genre = st.text_input("Genre")
     read_status = st.checkbox("Mark as Read")

     if st.button("Add Book"):
          library.apppend({"title":title,"author":author,"year":year,"genre":genre,"read_status":read_status})
          save_library()
          st.success("book added successfully!")
          st.rerun()

    #remove book
elif menu == "Remove a book":
    st.sidebar("Remove a book")
    book_titles = [book["title"]for book in library]

    if book_titles:
         selected_book = st.selectedbox("Select a book to remove",book_titles)
         if st.button("Remove Book"):
            library = [ book for book in library if book ["title"] != selected_book]
    save_library()
    st.success("book removed successfully!")
    st.rerun()
else:
     st.warning("No book in your library. Add some books!")
import streamlit as st
import json

# load & save library data
def load_library():
    try:
        with open ("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:
        json.dump(library,file,indent=4)

# initialize library
library = load_library()

st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an option",["Veiw library","Add Book","Remove a book","Search book","Save and Exit" ])
if menu == "Veiw library":
    st.sidebar("Your library")
    if library:
            st.table(library)
    else:
            st.write("No book in your library. Add some books!")

#Add book
elif menu == "Add Book":
     st.sidebar('Add a new book')
     title = st.text_input("Title")
     author  = st.text_input("Author")
     year = st.number_input("Year",min_value=2022, max_value=2100,steps=1)
     genre = st.text_input("Genre")
     read_status = st.checkbox("Mark as Read")

     if st.button("Add Book"):
          library.append({"title":title,"author":author,"year":year,"genre":genre,"read_status":read_status})
          save_library()
          st.success("Book added successfully!")
          st.rerun()

#remove book
elif menu == "Remove a book":
    st.sidebar("Remove a book")
    book_titles = [book["title"]for book in library]

    if book_titles:
         selected_book = st.selectbox("Select a book to remove",book_titles)
         if st.button("Remove Book"):
            library = [ book for book in library if book ["title"] != selected_book]
            save_library()
            st.success("Book removed successfully!")
            st.rerun()
    else:
         st.warning("No book in your library. Add some books!")

#search book
elif menu == "Search book":
    st.sidebar("Search a book")
    search_term= st.text_input("Enter title or author name")

    if st.button("Search"):
        result = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if result:
            st.table(result)
        else:
            st.warning("No book found")

# save and exit
elif menu == "Save and Exit":
    save_library()
    st.success("Library saved successfully")

    if st.button("Search"):
     result = [book for book in library if search_term.lower() in book
     ["title"].lower() or search_term.lower() in book["author"].lower()]


     if result:
          st.table(result)
     else:
          st.warning("No book found")

# save and exit
    elif menu == "Save and Exit":
     save_library()
     st.success("Library saved sucessfully")

# Importing streamlit library


#st.markdown('<h2><b style="color:green">Unit Converter Assignment</b></h2>', unsafe_allow_html=True)
#st.markdown('<h1 style="color:blue">Devan Das Mehrani</h1>', unsafe_allow_html=True)

my_val = st.number_input("Enter value to convert", min_value=0.0, format="%0.3f")

value = st.selectbox("Conversion from", ["Month", "Year", "Day", "Week", "Minute", "Hour"])
to = st.selectbox("Convert to", ["Year", "Month", "Week", "Day", "Hour", "Minute"])

st.markdown(f"Converting from {my_val} {value} to {to}")

btn = st.button("Convert")

def Convertor(my_val, value, to):
    conversion_factors = {
        ("Month", "Year"): my_val / 12,
        ("Year", "Month"): my_val * 12,
        ("Day", "Week"): my_val / 7,
        ("Week", "Day"): my_val * 7,
        ("Minute", "Hour"): my_val / 60,
        ("Hour", "Minute"): my_val * 60
    }

    return conversion_factors.get((value, to), my_val)

if btn:
    conv = Convertor(my_val, value, to)
    st.success(f"Final result: {conv:.3f}")

#import streamlit as st

def main():
    st.title("Unit Converter")
    st.write("Welcome to Unit Conver")

    value = st.number_input("Enter the value you want to convert")
    unit_from =st.text_input("Enter the valuw to convert")
    unit_to = st.text_input("enter the unit want from convert")

import streamlit as st

def convert_units(value, unit_from, unit_to):
    """Performs unit conversion.

    Args:
        value: The numerical value to convert.
        unit_from: The original unit of the value.
        unit_to: The target unit for conversion.

    Returns:
        The converted value, or None if the conversion is not supported.
    """
    # Add conversion logic here
    # Example:
    if unit_from == "meters" and unit_to == "feet":
        return value * 3.28084
    elif unit_from == "feet" and unit_to == "meters":
        return value / 3.28084
    # Add more conversion logic for other units as needed
    else:
        return None  # Indicate unsupported conversion


def main():
    st.title("Unit Converter")
    st.write("Welcome to Unit Converter")

    value = st.number_input("Enter the value you want to convert")
    unit_from = st.text_input("Enter the unit to convert from")
    unit_to = st.text_input("Enter the unit you want to convert to")

    if st.button("Convert"):
        converted_value = convert_units(value, unit_from, unit_to)
        if converted_value is not None:
            st.success(f"{value} {unit_from} is equal to {converted_value:.2f} {unit_to}")
        else:
            st.error("Unsupported conversion")


if __name__ == "__main__":
    main()

#import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import time
import requests
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore
from streamlit_lottie import st_lottie # type: ignore

#set page configuration
st.set_page_config(
    page_title="📚Personal Library Managment System 📚",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

#custom css for styling
st.markdown("""
<style>
    .main-header{
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;
    }

    .sub_header {
        font-size: 1.8rem !important;
        color: #3882F6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .success-message {
        padding: 1rem;
        background-color: #ECFDFS;
        border-left: 5px solid #108981;
        border-radius: 0.375rem;
    }

    .warning-message {
        padding: 1rem;
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        border-radius: 0.375rem;
    }

    .book-card {
        background-color: #3F4F6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 5px solid #3882F6;
        transition: transform 0.3s ease;
    }

    .book-card-hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0,.1);
    }

    .read-badge {
        background-color: #108981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 600;
    }

    .unread-badge {
        background-color: #F87171;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 600;
    }

    .action-button {
        margin-right: 0.5rem;
    }

    .stButton>button {
        border-radius: 0.375rem;
    }

</style>
""", unsafe_allow_html=True)

def save_library():
    try:
        with open("library.json", "w") as file:
            json.dump(st.session_state.library, file, indent=4)
    except Exception as e:
        st.error(f"Error saving library: {e}")

# Load library function
def load_library():
    try:
        if os.path.exists("library.json"):
            with open("library.json", "r") as file:
                st.session_state.library = json.load(file)
                return True
        else:
            return False
    except Exception as e:
        st.error(f"Error Loading library: {e}")
        return False

if "library" not in st.session_state:
    st.session_state.library = []
if "search_results" not in st.session_state:
    st.session_state.search_results = []
if "book_added" not in st.session_state:
    st.session_state.book_added = False
if "book_removed" not in st.session_state:
    st.session_state.book_removed = False
if "current_view" not in st.session_state:
    st.session_state.current_view = "Library"

# Add book function
def add_book(title, author, publication_year, genre, read_status):
    book = {
        'title' : title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status,
        'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time.sleep(0.5)  # animation delay

# Remove book function
def remove_book(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()
        st.session_state.book_removed = True

# Search books function
def search_books(search_term, search_by):
    search_term = search_term.lower()
    results = []
    for book in st.session_state.library:
        if search_by == "Title" and search_term in book['title'].lower():
            results.append(book)
        elif search_by == "Author" and search_term in book['author'].lower():
            results.append(book)
        elif search_by == "Genre" and search_term in book['genre'].lower():
            results.append(book)
    st.session_state.search_results = results

# Calculate library state
def get_library_state():
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book['📝read_status'])
    percent_read = (read_books / total_books * 100) if total_books > 0 else 0

    genres = {}
    authors = {}
    decades = {}

    for book in st.session_state.library:
        # Count genres
        genres[book['genre']] = genres.get(book['genre'], 0) + 1

        # Count authors
        authors[book['author']] = authors.get(book['author'], 0) + 1

        # Count decades
        try:
            decade = (int(book['publication_year']) // 10) * 10
            decades[decade] = decades.get(decade, 0) + 1
        except ValueError:
            pass

    # Sorting by count
    genres = dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
    authors = dict(sorted(authors.items(), key=lambda x: x[1], reverse=True))
    decades = dict(sorted(decades.items(), key=lambda x: x[0]))

    return {
        'total_books': total_books,
        'read_books': read_books,
        'unread_books': total_books - read_books,
        'percent_read': percent_read,
        'genres': genres,
        'authors': authors,
        'decades': decades
    }

# Visualization creation
def create_visualization(stats):
    if stats['total_books'] > 0:
        fig_read_status = go.Figure(
            data=[go.Pie(
                labels=['Read', 'Unread'],
                values=[stats['read_books'], stats['unread_books']],
                hole=0.4,
                marker_colors=['#108981', '#F87171']
            )]
        )
        fig_read_status.update_layout(
            title_text='Read vs Unread Books',
            showlegend=True,
            height=400
        )
        st.plotly_chart(fig_read_status, use_container_width=True)

    if stats['genres']:
        genres_df = pd.DataFrame({
            'Genres': list(stats['genres'].keys()),
            'Count': list(stats['genres'].values())
        })
        fig_genres = px.bar(
            genres_df,
            x='Genres',
            y='Count',
            color='Count',
            color_continuous_scale=px.colors.sequential.Blues
        )
        fig_genres.update_layout(
            title_text='Books by Genre',
            xaxis_title='Genre',
            yaxis_title='Number of Books',
            height='400'
        )
        st.plotly_chart(fig_genres, use_container_width=True)

    if stats['decades']:
        decades_df = pd.DataFrame({
            'Decade': [f'{decade}s' for decade in stats['decades'].keys()],
            'Count': list(stats['decades'].values())
        })
        fig_decades = px.line(
            decades_df,
            x='Decade',
            y='Count',
            markers=True,
            line_shape='spline'
        )
        fig_decades.update_layout(
            title_text='Books by Publication Decade',
            xaxis_title='Decade',
            yaxis_title='Number of Books',
            height=400
        )
        st.plotly_chart(fig_decades, use_container_width=True)

st.sidebar.markdown("<h1 style='text-align: center;'> Navigation</h1>", unsafe_allow_html=True)

# Lottie animation
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

lottie_book = load_lottie_url("https://assets9.lottiefiles.com/temp/1f20_aKAFIn.json")
if lottie_book:
    with st.sidebar:
        st_lottie(lottie_book, height=200, key='book_animation')

nav_option = st.sidebar.radio(
    "Choose an option:",
    ["View Library", "Add Book", "Search Book", "Library Statistics"]
)

if nav_option == "View Library":
    st.session_state.current_view = "Library"
elif nav_option == "Add Book":
    st.session_state.current_view = "Add"
elif nav_option == "Search Book":
    st.session_state.current_view = "Search"
elif nav_option == "Library Statistics":
    st.session_state.current_view = "Stats"

# Main header
st.markdown("<h1 class='main-header'> Personal Library Manager </h1>", unsafe_allow_html=True)

if st.session_state.current_view == "Add":
    st.markdown("<h2 class='sub_header'> Add a New Book</h2>", unsafe_allow_html=True)

    # Adding book input form
    with st.form(key='add_book_form'):
        col1, col2 = st.columns(2)

        with col1:
            title = st.text_input("Book Title", max_chars=100)
            author = st.text_input("Author", max_chars=100)
            publication_year = st.number_input("Publication Year", min_value=1000, max_value=datetime.now().year, step=1, value=2023)

        with col2:
            genre = st.selectbox("Genre", [
                "Fiction", "Non-Fiction", "Science", "Technology", "Fantasy", "Romance", "History", "Thriller", "Psychology", "Philosophy", "Biographies"
            ])
            read_status = st.radio("Have you read this book?", ("Yes", "No"))

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            add_book(title, author, publication_year, genre, read_status.lower() == "yes")
            st.success("Book added successfully!")

elif st.session_state.current_view == "Library":
    st.markdown("<h2 class='sub_header'> Your Library </h2>", unsafe_allow_html=True)
    for index, book in enumerate(st.session_state.library):
        book_card = f"""
        <div class="book-card">
            <h3>{book['title']}</h3>
            <p>by {book['author']}</p>
            <p>Published: {book['publication_year']}</p>
            <p>Genre: {book['genre']}</p>
            <p>Status: {'Read' if book['read_status'] else 'Unread'}</p>
            <p>
                <button class="action-button" onClick="remove_book({index})"> Remove </button>
            </p>
        </div>
        """
        st.markdown(book_card, unsafe_allow_html=True)

elif st.session_state.current_view == "Search":
    st.markdown("<h2 class='sub_header'> Search Books </h2>", unsafe_allow_html=True)

    search_term = st.text_input("Enter search term")
    search_by = st.radio("Search by", ["Title", "Author", "Genre"])

    search_button = st.button("Search")
    if search_button:
        search_books(search_term, search_by)
        if st.session_state.search_results:
            for book in st.session_state.search_results:
                st.write(f"**{book['title']}** by {book['author']} ({book['publication_year']})")
        else:
            st.warning("No matching books found.")

elif st.session_state.current_view == "Stats":
    stats = get_library_state()
    st.markdown("<h2 class='sub_header'> Library Statistics </h2>", unsafe_allow_html=True)
    st.write(f"Total books: {stats['total_books']}")
    st.write(f"Books read: {stats['read_books']}")
    st.write(f"Books unread: {stats['unread_books']}")
    st.write(f"Percentage read: {stats['percent_read']:.2f}%")

name = "PythonRocks"
name[5] = "s"
print(name)