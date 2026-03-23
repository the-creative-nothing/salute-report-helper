from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def salute_report():
    if request.method == 'POST':
        # Get form data
        report_data = {
            'size': request.form.get('size', ''),
            'activity': request.form.get('activity', ''),
            'location': request.form.get('location', ''),
            'unit_uniform': request.form.get('unit_uniform', ''),
            'time': request.form.get('time', ''),
            'equipment': request.form.get('equipment', ''),
            'network' : request.form.get('network', ''),
            'talkgroup' : request.form.get('talkgroup', '')
        }
        now = datetime.now()
        
        # Generate formatted SALUTE report
        report_text = f"""
SALUTE REPORT
{now.month}-{now.day}-{now.year}:{now.hour}:{now.minute}
================
Size: {report_data['size']}
Activity: {report_data['activity']}
Location: {report_data['location']}
Unit/Uniform: {report_data['unit_uniform']}
Time: {report_data['time']}
Equipment: {report_data['equipment']}
Network: {report_data['network']}
Talkgroup: {report_data['talkgroup']}

END REPORT"""

        return render_template('report.html', report=report_text, data=report_data)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)