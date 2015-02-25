from datetime import datetime
import json
import os
import re

filenames = next(os.walk('./data'))[2]

prepared_all_stories = {}

for f in filenames:
  daily_stories_json = open('./data/%s' % (f))
  daily_stories_data = json.load(daily_stories_json)

  prepared_daily_stories = []

  fname = re.sub('.json', '', f)

  for story in daily_stories_data:
    if story["points"] and story["date"]:
      # save only time, no date
      t = datetime.utcfromtimestamp(story["date"])
      # time_string = "{:%H%M%S}".format(t)
      # time = 1000000 + int(time_string)

      #save only day of the week
      time = datetime.strptime(str(t), '%Y-%m-%d %H:%M:%S').strftime('%w')

      s = { "points": story["points"], "date": str(time), "id": story["id"] }
      prepared_daily_stories.append(s)

  prepared_all_stories[fname] = prepared_daily_stories

prepared_data = open('prepared_data.json', 'w')
prepared_data.write(json.dumps(prepared_all_stories, sort_keys=True))
prepared_data.close