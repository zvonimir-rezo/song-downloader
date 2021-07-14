from tkinter import *
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from os import listdir
from os.path import isfile, join

options = Options()
options.add_argument('window-size=100,100')
options.add_argument('window-position=500,500')


def main():
    root = Tk()
    root.geometry("450x150")
    root.title("Song Downloader!")
    root.configure(background="light yellow")

    text_variable = StringVar()
    text_variable.set("Youtube link: ")

    text_label = Label(root, textvariable=text_variable, font=('Helvetica bold', 20), bg="red")
    link_entry = Entry(root, width=40, font=('Helvetica', 12))
    download_button = Button(root, text="Download", font=('Helvetica bold',15), command=(lambda: download(link_entry.get())), bg="green")

    text_label.pack()
    link_entry.pack()
    download_button.pack()

    root.mainloop()


def download(link):
    driver = webdriver.Chrome(options=options)
    driver.get('https://ytmp3.cc/youtube-to-mp3/')
    inputbox = driver.find_element_by_xpath('//*[@id="input"]')
    inputbox.send_keys(link)
    convert_button = driver.find_element_by_xpath('//*[@id="submit"]')
    convert_button.click()

    while True:
        try:
            download_button = driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
            if download_button.text == "Download":
                break
            else:
                continue
        except ElementNotInteractableException:
            continue

    song_name = driver.find_element_by_xpath('//*[@id="title"]').text
    song_name = song_name.replace("/", "")
    download_button.click()
    download_dir_path = r"C:\Users\Zvone\Downloads"

    while song_name not in [f.rsplit('.', 1)[0] for f in listdir(download_dir_path) if isfile(join(download_dir_path, f))]:
        continue

    driver.close()


if __name__ == "__main__":
    main()