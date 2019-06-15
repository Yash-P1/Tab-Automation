import webbrowser
import time

techmedia = ["www.techcrunch.com"]
socailmedia = ["www.facebook.com", "www.twitter.com", "www.youtube.com"]

if __name__ == "__main__":
    for i in techmedia:
        webbrowser.open_new(i)
    time.sleep(2)
    for i in socailmedia:
        webbrowser.open_new(i)
