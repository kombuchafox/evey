from flask import redirect, url_for, flash, session, request, render_template, g
from . import main
from ..convengine import EveyEngine
from config import SECRET_KEY, TOKEN, WEBHOOK, WEBHOOK_TOKEN
from ..utils import fetch_user_data, post_response_msgs
import requests
import json
import traceback

from ..models.users import User
from .. import db, lm
from usermanager import UserManager
from datetime import datetime
from flask.ext.login import UserMixin, login_user, logout_user, current_user, \
                            login_required
from ..oauth import OAuthSignIn


main.secret_key = SECRET_KEY
usr_manager = UserManager()

def save(objs):
  for obj in objs:
    db.session.add(obj)
  db.session.commit()

@main.route('/webhook/' + WEBHOOK, methods=['GET'])
def verification():
  if request.args.get('hub.verify_token') == WEBHOOK_TOKEN:
    return request.args.get('hub.challenge')
  return 'Wrong Verify Token'

@main.route('/webhook/' + WEBHOOK, methods=['POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      print(data)
      for entry in data['entry']:
        sender = ""
        msgs = []
        postbacks = []
        message_uid = entry["id"]

        for message in entry['messaging']:
          if sender == "":
            sender = message['sender']['id'] # Sender ID
            timestamp = message['timestamp']
          if 'delivery' in message:
            return "hello world"
          if 'message' in message:
            msg = message.get('message')
            if 'quick_reply' in msg:
                postbacks.append(msg['quick_reply']['payload'])
            else:
                msgs.append(msg['text'])
          if 'postback' in message:
            print("postback")
            postbacks.append(message['postback']['payload'])
      user = usr_manager.handle_messenger_user(sender)
      if not user.timezone:
          try:
              user_data = fetch_user_data(sender)
              print(user_data)
              user.timezone = int(user_data["timezone"])
          except Exception as e:
              pass

      user.last_date_used = datetime.utcnow()
      if user.last_msg:
        prev_time = int(user.last_msg)
        user.last_msg = str(timestamp)
        if (int(timestamp) - prev_time) < 10:
          return "rapid"
      else:
        user.last_msg = str(timestamp)
      save([user])
      evey = EveyEngine(user.first_name, user, sender)
      if len(postbacks):
        resp_msgs = evey.handle_postback(postbacks)
        post_response_msgs(resp_msgs, sender)
      elif len(msgs):
        print("msgs: %s" % str(msgs))
        resp_msgs = evey.understand(msgs)
        print(resp_msgs)
        post_response_msgs(resp_msgs, sender)
    except Exception as e:
      print traceback.format_exc() # something went wrong
  print("hello")
  return "hello world"

@lm.user_loader
def load_user(id):
  return User.query.get(int(id))


@main.route('/')
def index():
    if current_user != None:
      print(current_user)
      messenger_uid = current_user.messenger_uid

      resp_msg = EveyEngine(current_user.first_name, current_user,
                            messenger_uid).understand(["site visit"])
      for msg in resp_msg:
        payload = {'recipient': {'id': messenger_uid}, 'message':msg}
        r = requests.post(MESNGR_API_URL + TOKEN, json=payload)
    return render_template("index.html")

@main.route('/privacy-policy')
def privacy_policy():
    return render_template("privacypolicy.html")
