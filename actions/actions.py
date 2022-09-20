# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import DataUpdate


class ActionName(Action):

     def name(self) -> Text:
         return "utter_number"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(template="utter_name")

         return [SlotSet('name',tracker.latest_message['text'])]

class ActionNumber(Action):

     def name(self) -> Text:
         return "utter_email"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(template="utter_number")

         return [SlotSet('number',tracker.latest_message['text'])]

class ActionEmail(Action):

     def name(self) -> Text:
         return "utter_description"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(template="utter_email")

         return [SlotSet('email',tracker.latest_message['text'])]




class ActionSubmit(Action):

     def name(self) -> Text:
         return "action_save_candidate"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         
         DataUpdate(tracker.get_slot('name'),tracker.get_slot('number'),tracker.get_slot('email'),tracker.get_slot('description'))
         return [SlotSet('email',tracker.latest_message['text'])]
