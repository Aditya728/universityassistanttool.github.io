# importing required packages
import requests
import json
import pyttsx3
import speech_recognition as sr
import re

# foot print for loading and accessing the data from parsehub file
class Data1:
    def __init__(self, A, P):               # gives universities information (national and liberal arts college)
        self.api_key = A
        self.project_token = P
        self.params = {
            'api_key': self.api_key
        }
        self.data = self.get_data()

    def get_data(self):                     # sets all data of universities (national/ liberal arts)
        response = requests.get(f"https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data", params=self.params)
        data = json.loads(response.text)
        return data

    def get_state(self, Uname):            # gives the state of user searched university (national/ liberal arts)
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['state']

    def get_city(self, Uname):             # gives the city of user searched university (national/ liberal arts)
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['city']

    def get_us_rank(self, Uname):          # gives the US rankings of user searched university (national/ liberal arts)
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['us_rank']

    def get_world_rank(self, Uname):                # gives the World rankings of user searched university (national)
                                                    # not used for liberal arts colleges
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['world_rank']

    def get_liberal_arts_rank(self, Uname):        # gives the Liberal arts rankings of user searched university (liberal arts)
                                                   # not used for national universities
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['liberalarts_rank']

    def get_overall_score(self, Uname):                # gives the overall score of user searched university (national)
                                                         # not used for liberal arts colleges
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['overall_score']

    def get_research_quality_score(self, Uname):                # gives the research quality score of user searched university (national)
                                                                # not used for liberal arts colleges
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['research_output']

    def get_education_quality_score(self, Uname):                # gives the overall score of user searched university (national)
                                                                # not used for liberal arts colleges
        present_data = self.data['university']
        for items in present_data:
            if items['name'].lower() == Uname.lower():
                return items['quality_education']

    def get_universities(self):                    # gives all the universities in the database (national/ liberal arts)
        present_data = self.data['university']
        university_list = []
        for items in present_data:
            university_list.append(items['name'].lower())
        return university_list

# text to audio conversion
def txt_audio(text):
    vehicle = pyttsx3.init()
    vehicle.say(text)
    vehicle.runAndWait()

# audio to text conversion
def audio_txt():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        recorded = recorder.listen(source)
        audio_text = ''
    try:
        audio_text = recorder.recognize_google(recorded)
    except Exception as e:
        print("Exception : " + str(e))
        print()
    return audio_text.lower()

# the main program
def main():
    API_KEY = 'tOSMBfVXT6V7'
    PROJECT_TOKEN = ['tdMwaSaNeHTC', 'tozrDwKVjwvo']
    National_univ = Data1(API_KEY, PROJECT_TOKEN[0])
    Liberalart_colz = Data1(API_KEY, PROJECT_TOKEN[1])
    End_Phrase = ['exit', 'end']
    txt_audio('Hey user! I am on... Your University Assistant Tool. Firstly, please say me your name.')

    # taking User's name
    while True:
        user_name = audio_txt()
        if user_name != '':
            txt_audio('Hey user! Did you say ...' + user_name.upper() + ' as your name?')
            voice_prompt1 = audio_txt()
            if 'yes' in voice_prompt1.split():
                break
        txt_audio('I am extremely sorry for the inconvenience! Please repeat your name.')

    # user interface
    print('So, ' + user_name.upper() + ' Welcome! A greetings from me...')
    print()
    txt_audio('So, ' + user_name + ' Welcome! A greetings from me. Before you ask me a question, I want to give you some idea about the type of data that I have in my database.')
    txt_audio('I have parsed the data from The Higher Education World University ranking. This data will allow you to ask about any national university or liberal arts college that is present in US.')
    txt_audio('For the national universities, I will say you the World ranking and US national ranking for the university. Along with this, I will say you the city and the state where the university is located.')
    txt_audio('For the liberal arts college, I will say you the Liberal Arts ranking and US national ranking of the college. Along with this, I will say you the city and the state where the college is located.')
    txt_audio('Hey ' + user_name + '! I have to mention you one thing. I also parse the data from US news and Niche. But, today the parsing is unavailable. So, I will not be able to give any additional information about the university.')
    print('Please say the university or college name you want to know about...')
    txt_audio('Hope you are clear! Lets start now. Please say the university or college name you want to know about.')

    # the main processing codes which use pattern recognition, google assistant, and parsing
    while True:
        check_flag = False
        # taking university name
        while True:
            user_input = audio_txt()
            if user_input != '':
                print('Did you say, ' + '\"' + user_input + '?\"...')
                print()
                txt_audio('Hey' + user_name + '! Did you say ...' + user_input)
                voice_prompt1 = audio_txt()
                if 'yes' in voice_prompt1.split():
                    break
            txt_audio('I am extremely sorry for the inconvenience! Please repeat your university name.')

        # finding the user intended university from the database
        for university in National_univ.get_universities():
            if re.search(university, user_input):
                print(university.upper() + ' found in database...')
                print()
                txt_audio(university + ' found in database.')
                print('Name = ' + university.upper())
                txt_audio('So, ' + university)
                print('Education Quality Ranking = ' + National_univ.get_education_quality_score(university).upper() + '...')
                txt_audio('According to The World University Ranking, ' + university + '\'s education quality ranking is '+ National_univ.get_education_quality_score(university) + ' in the world.')
                print('Research Output Ranking = ' + National_univ.get_research_quality_score(university).upper() + '...')
                txt_audio('According to The World University Ranking, ' + university + '\'s research quality ranking is '+ National_univ.get_research_quality_score(university) + ' in the world.')
                print('Overall Ranking = ' + National_univ.get_overall_score(university).upper() + '...')
                txt_audio('According to The World University Ranking, ' + university + '\'s overall score is '+ National_univ.get_overall_score(university) + ' out of 100.')
                print('US Ranking = ' + National_univ.get_us_rank(university).upper() + '...')
                txt_audio('According to The World University Ranking, ' + university + ' is ranked ' + National_univ.get_us_rank(university) + ' in USA.')
                print('World Ranking = ' + National_univ.get_world_rank(university).upper() + '...')
                print()
                txt_audio('According to The World University Ranking ' + university + ' is ranked ' + National_univ.get_world_rank(university) + ' in the world.')
                check_flag = True
                break
        for university in Liberalart_colz.get_universities():
            if re.search(university, user_input):
                print(university.upper() + ' found in database...')
                print()
                txt_audio(university + ' found in database.')
                print('Name = ' + university.upper())
                txt_audio('So, ' + university)
                print('City = ' + Liberalart_colz.get_city(university).upper() + '...')
                txt_audio(university + ' is located in ' + Liberalart_colz.get_city(university) + ' city.')
                print('State = ' + Liberalart_colz.get_state(university).upper() + '...')
                txt_audio('The ' + Liberalart_colz.get_city(university) + ' city is located in ' + Liberalart_colz.get_state(university) + ' state.')
                print('Liberal Arts Ranking = ' + Liberalart_colz.get_liberal_arts_rank(university).upper() + '...')
                txt_audio('According to The World University Ranking, ' + university + ' is ranked ' + Liberalart_colz.get_liberal_arts_rank(university) + ' in USA among all liberal arts colleges.')
                print('US Ranking = ' + Liberalart_colz.get_us_rank(university).upper() + '...')
                print()
                txt_audio('According to The World University Ranking, ' + university + ' is ranked ' + Liberalart_colz.get_us_rank(university) + ' in the USA among all colleges and universities.')
                check_flag = True
                break
        if check_flag == False:
            print('No university found with ' + user_input + '...')
            print()
            txt_audio('No university found with ' + user_input + ' in my database.')

        # ending the program
        print('Do you want to exit the program?...')
        print()
        txt_audio('Do you want to exit the program? If yes, just say: Exit.')
        while True:
            user_input = audio_txt()
            if user_input != '':
                print('Did you say, ' + '\"' + user_input + '?\"...')
                print()
                txt_audio('Hey' + user_name + '! Did you say ...' + user_input)
                voice_prompt1 = audio_txt()
                if 'yes' in voice_prompt1.split():
                    break
            txt_audio('I am extremely sorry for the inconvenience! Please repeat your exit or stay response. To end the program, just say exit.')
        if re.match(End_Phrase[0], user_input) or re.match(End_Phrase[1], user_input):
            if re.search('don\'t', user_input):
                pass
            elif re.search('do not', user_input):
                pass
            elif re.search('not', user_input):
                pass
            else:
                txt_audio('Thank you ' + user_name + ' to be with me! I had a delightful time with you!... Have a wonderful day. Goodbye my friend.')
                break
        print("Ask about another university...")
        print()
        txt_audio('So, ' + user_name + '. Ask about another university to me.')

# calling the main class
main()

