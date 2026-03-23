# SALUTE Report Helper

Look, its hard to remember what SALUTE means when you are facing down a snarling ICE agent threatening you with chemical weapons. This incredibly simple, mostly vibe coded (on a local LLM using qwen-code), web form that gives you fields to fill out to generate your SALUTE report.

That report is then rendered in an easy to copy format for sending to Signal groups and other text based networks.

The imagined workflow is the following:
- You are in the field and you see something you want to report to local ICE Watch
- You pull out your phone and go to the URL for the reporting app
- The app takes in your information and then generates an easy to copy and paste report
- You copy that SALUTE report into Signal and send to local response teams

Using tools like this helps ensure that we are using consistent reporting methods, conveying clear information, and doing all of that on a platform that does not persist data.

The application runs as a simple Flask API, which does nothing more than take in request data, extract specific information, and then formats it into a response. No information is persisted anywhere outside of live Flask process memory.