# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:07:07 2023

@author: bishn
"""

import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from docx import Document
import PyPDF2
import openai


openai.api_key = "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"


def input_file():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", ".pdf"), ("all files", ".*")))
    read_file(root.filename)
    root.destroy()


def download_file():
    root = Tk()
    root.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Save file", filetypes = (("Word files", ".docx"), ("all files", ".*")))

    # Create a new Word document
    document = Document()

    # Add the draft_assignment text to the document
    document.add_paragraph(draft_assignment)

    # Save the document
    document.save(root.filename)
    root.destroy()
    
def read_file(filename):
    global draft_assignment
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        assignment_criteria = pdf_reader.pages[0].extract_text()
        evaluation_criteria = pdf_reader.pages[1].extract_text()
        tasks = pdf_reader.pages[2].extract_text
        learning_outcomes = pdf_reader.pages[3].extract_text()
        
        
        prompt_context = "Context for draft : \n\nAssignment Criteria: {assignment_criteria} \n\nEvaluation Criteria: {evaluation_criteria} \n\nTasks: {tasks} \n\nLearning Outcomes: {learning_outcomes} \n\n"
        openai.Completion.create(engine="text-davinci-002", prompt=prompt_context, temperature=0.8, max_tokens=2000, frequency_penalty=0.8, presence_penalty=0.4)
        
        
        prompt_context = "Make a Outline on the above assignment in 500 words with headings and subheadings and mention what will be included inside each subheading divide word count among each sub headings, wordlimit 2000 "
        draft_assignment = openai.Completion.create(engine="text-davinci-002", prompt=prompt_context, temperature=0.8, max_tokens=2000, frequency_penalty=0.8, presence_penalty=0.4).choices[0].text
        print(draft_assignment)
        #print("***Done***")
        
        
draft_assignment = ""
root = Tk()

root.title("Assignment Generator")

input_button = Button(root, text = "Input", command = input_file)
input_button.pack()

download_button = Button(root, text = "Download", command = download_file)
download_button.pack()


root.mainloop()