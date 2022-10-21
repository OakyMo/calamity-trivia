"""
skill farting-skill
Copyright (C) 2020  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
from datetime import datetime, timedelta
from os import listdir, path
from os.path import abspath, dirname, isfile, join, splitext
from tinytag import TinyTag

from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.messagebus.message import Message

class CalamityTrivia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        # retained to avoid errors 
        valid_codecs = ['.mp3']
        self.path_to_sound_files = path.join(abspath(dirname(__file__)), 'sounds')
        self.sound_files = [f for f in listdir(self.path_to_sound_files) if splitext(f)[1] in valid_codecs]
        self.audio_service = AudioService(self.bus)
        self.random_farting = False  # flag to indicate whether random farting mode is active
        self.counter = 0  # variable to increment to make the scheduled event unique

    @intent_file_handler('trivia.intent')
    def trivia(self):
        self.log.info("Comment")
        self.speak_dialog('category')
        
    @intent_file_handler('hodgepodge.intent')
    def hodgepodge_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('hodgepodgetrivia')
        
    @intent_file_handler('nobrainers.intent')
    def nobrainers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('nobrainerstrivia')
        
    @intent_file_handler('brainstumpers.intent')
    def brainstumpers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('brainstumperstrivia')
        
    @intent_file_handler('thatsentertainment.intent')
    def thatsentertainment_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('thatsentertainment')
        
    @intent_file_handler('animallovers.intent')
    def animallovers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('animallovers')
        
    @intent_file_handler('connasewers.intent')
    def connasewers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('connasewerstrivia')
        
    @intent_file_handler('oddballs.intent')
    def oddballs_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('oddballstrivia')
        
    @intent_file_handler('aroundtheworld.intent')
    def aroundtheworldtrivia(self):
        self.log.info("Comment")
        self.speak_dialog('aroundtheworldtrivia')
        
    @intent_file_handler('backintheday.intent')
    def backintheday_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('backinthedaytrivia')
        
    @intent_file_handler('forthekids.intent')
    def forthekids_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('forthekidstrivia')
        
    @intent_file_handler('movielovers.intent')
    def movielovers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('movieloverstrivia')
        
    @intent_file_handler('musiclovers.intent')
    def musiclovers_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('musicloverstrivia')
        
    @intent_file_handler('forthemasses.intent')
    def forthemasses_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('forthemassestrivia')
        
    @intent_file_handler('forthenerds.intent')
    def cforthenerds_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('forthenerdstrivia')
        
    @intent_file_handler('sportsfans.intent')
    def sportsfans_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('sportsfanstrivia')
        
    @intent_file_handler('forthegeeks.intent')
    def forthegeeks_trivia(self):
        self.log.info("Comment")
        self.speak_dialog('forthegeekstrivia') 

def create_skill():
    return CalamityTrivia()

