import requests
import os
from io import BytesIO
import webbrowser
from tkinter import *
from PIL import ImageTk, Image
from dotenv import load_dotenv  # 1. Import the env loader

# 2. Load the environment variables from the hidden .env file
load_dotenv()
class NewsApp():

    def __init__(self):
        # Fetch news data
        # 1. Fetch the value stored in the environment variable
        full_url = os.getenv('NEWS_API_KEY')

        # 2. Pass the fetched variable string into requests (WITHOUT literal quotes around it)
        self.data = requests.get(full_url).json()

        
        # Initial GUI load
        self.load_gui()
       
        # Load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('Mera News App')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves(): 
            i.destroy()

    def load_news_item(self, index):
        # Clear the previous screen 
        self.clear()

        # Fetch image URL safely
        img_url = self.data['articles'][index].get('urlToImage')
        image_loaded = False

        if img_url:
            try:
                # FIX: Use requests with a browser 'User-Agent' header to bypass 403 Forbidden
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                response = requests.get(img_url, headers=headers, timeout=5)
                
                # Check if the website actually gave us a successful response status
                if response.status_code == 200:
                    raw_data = response.content
                    im = Image.open(BytesIO(raw_data)).resize((350, 250))
                    
                    # Store photo as an instance variable so Python garbage collection doesn't delete it
                    self.photo = ImageTk.PhotoImage(im)
                    
                    lable = Label(self.root, image=self.photo)
                    image_loaded = True
            except Exception as e:
                # If network fails, website times out, or image is corrupt, catch the error gracefully
                print(f"Skipping image due to fetch error: {e}")

        # Fallback if image URL doesn't exist or failed to download
        if not image_loaded:
            lable = Label(
                self.root,
                text='Image unavailable',
                bg='black',
                fg='white',
                height=10,
                font=('vardana', 12)
            )
            
        lable.pack()

        # Heading section
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('vardana', 15))

        # Details section
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350, justify='center')
        details.pack(pady=(10,20))
        details.config(font=('vardana', 11))

        # Control panel frame
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True , fill=BOTH)

        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

    def open_link(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    obj = NewsApp()
    obj.root.mainloop()
