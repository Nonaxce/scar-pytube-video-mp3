from pytube import YouTube
import re
# MUST import pytube for this to work `pip install pytube` on terminal
# Probably illegal but it's cool
# HOWEVER please support the artist you like whenever you financially can..
# ..it would mean a lot them <3

def downloadAudio(url_arr):
    # checks if the array is empty, which will return a message
    if not url_arr:
        print("You don't have a url entered, please try again")
    else:
        # loops through the array of urls
        for url in url_arr:
            # checks if user entered a valid yt video url
            # EDIT NI PLS LATER THX ME vvv
            regex_url = '^https:\/\/www\.youtube\.com\/watch\?v='
            url_regex_match = re.match(regex_url, url)
            
            if(url_regex_match):
                try: 
                    # accesses only the mp3
                    video = YouTube(url)
                    stream = video.streams.filter(only_audio=True).first()
                    # downloads the video to the local Downloads folder
                    stream.download(('C:/Users/USER/Documents/YTDDL_FILES'),filename=f"{video.title}.mp3")
                    # displays which video has finished downloading
                    print(f"( {url} ) This video has finished downloading")
                except KeyError:
                    # if error
                    print(f"( {url} ) This download failed, please try again")

            # reminds the user that that the url which the user entered is incorrect
            else:
                print(f"""   '\033[31m{url}\033[0m' is not a url""")
        # alerts if all song(s) has been downloaded`
        print(f"   Your video{isArrayPlural(url_arr)} have finished downloading")

# will return s char if the array has 2 or more items
# just to be fancy
def isArrayPlural(url_arr):
    if (len(url_arr) < 2):
        return "s"
    else:
        return ""