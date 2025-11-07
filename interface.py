import streamlit as slt
from recommender import recommender

slt.title("Book recommender for the book lovers 📖")
book_name = slt.text_input("Please input the name of the books you want to find a similar book to: ")
authors_name = slt.text_input("Please enter the author(s): ")
description = slt.text_input("Please input a smaller description of what the book is about: ")
category = slt.text_input("Please enter what genre your book is: ")
button = slt.button("Get the recommendations !")
#chose to ignore the other categories as they are not important/evident to get

if button:
    textual_representation = f"""Title: {book_name}
    Authors: {authors_name}
    Description: {description}
    Categories: {category}"""
    recommendations = recommender(textual_representation)
    
    if recommendations.empty:
        slt.info("Sadly no book matches what you are looking for. Try with another one !")
    else: 
        slt.write("Top 5 books that you will probably enjoy")
        for indx, book in recommendations.iterrows():
            col1, col2 = slt.columns([1, 3])
            with col1:
                slt.image(book["thumbnail"], use_container_width=True)
            with col2:
                slt.subheader(book["title"])
                slt.write(f"**Authors:** {book["authors"]}")
                slt.write(f"**Category:** {book["categories"]}")
                slt.write(f"**Average Rating:** {book["average_rating"]}")
                slt.write(f"**Number of Pages:** {book["num_pages"]}")
                slt.write(f"**Published Year:** {book["published_year"]}")
                with slt.expander("**Description:**"):
                    slt.write(book["description"])
            slt.markdown("---")
