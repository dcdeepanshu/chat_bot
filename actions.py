import logging

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted,ConversationPaused


logger = logging.getLogger(__name__)
class ActionFaqs(Action):

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        if intent in ['ask_login', 'ask_mobile_email','ask_otp','ask_setpass','ask_reset','login_issue' ,'ask_appoint' ,'search_doc','search_hosp','search_speciality','ask_appoint_confirm','ask_invoice','e_card','enroll','policy_details']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []
