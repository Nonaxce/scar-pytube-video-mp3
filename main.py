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
        print(f"   Your video{is_this_specific_array_have_more_than_one_thing_in_it_aka_plural_like_has_or_have_questionmark(url_arr)} finished downloading")

# will return s char if the array has 2 or more items
# just to be fancy
def is_this_specific_array_have_more_than_one_thing_in_it_aka_plural_like_has_or_have_questionmark(url_arr):
    if (len(url_arr) > 1):
        return "s have"
    else:
        return " has"

# function that displays url
def show_url_arr(url_arr):
    # list number
    i = 1
    print(f"""   ----Download Queue---------""")
    if (len(url_arr) != 0):
        for x in url_arr:
            if (i%2 == 0):
                print(f"""     {i}.  \033[36m{x}\033[0m""")
            else:
                print(f"""     {i}.  \033[35m{x}\033[0m""")
            i += 1
    else:
        print(f"""    Download queue empty :<""")
    print(f"""   --------------------------""")
    
# collects user urls and then adds it the array
def get_user_input():
    collecting = False
    # array for the urls
    video_url_arr = []
    # loops/keeps on asking for urls until the user says quit
    while collecting == False:
        # user input to string
        video_url = str(input("Enter URL: "))
        # checks if user wants to stop adding urls to queue
        if (video_url == "1"):
            show_url_arr(video_url_arr)
            return video_url_arr
            collecting = True
        else:
            # remove the previous url entered
            if (video_url == "2"):
                # checks kung wala na unod ang queue
                if (len(video_url_arr) == 0):
                    print("download queue is already empty ;-;")
                else: 
                    video_url_arr.pop()
                    show_url_arr(video_url_arr)
            # removes all urls in the list
            elif (video_url == "3"):
                video_url_arr.clear()
                show_url_arr(video_url_arr)
            else:
                try:
                    regex_url = '^https:\/\/www\.youtube\.com\/watch\?v='
                    url_regex_match = re.match(regex_url, video_url)
                    if(url_regex_match):
                        # adds the url to the list 
                        video_url_arr.append(video_url)
                        show_url_arr(video_url_arr)
                    else:
                       print(f"'\033[31m{video_url}\033[0m' is not a url")

                # if error does happen
                except KeyError:
                    print("Sorry something went wrong")


def main():
    print(f"""\033[31m
    +==============YT TO MP3===============+
    |           Built with Pytube          |
    +______________________________________+
    | Enter 0 to quit                      |
    | Enter 1 to stop                      |
    | Enter 2 to remove previous           |
    | Enter 3 to remove all                |
    +--------------------------------------+
    \033[0m""")
    video_arr = get_user_input()
    downloadAudio(video_arr)


# runs the program
main()
