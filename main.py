from flask import Flask
from flask_socketio import SocketIO, emit

try:
    from oled_status import Status
    oled = Status('ScoreBox Relay', 'Awaiting Sport')
except Exception:
    oled = None

from score import ScoreKeeper

scorekeeper = None # type: ScoreKeeper

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet', logger=False, engineio_logger=False)

@app.get('/')
def index():
    return app.send_static_file('feed.html')

@app.get('/init/<mode>')
def set_mode(mode):
    global scorekeeper
    global oled
    if scorekeeper:
        return 'ScoreKeeper Already Running'
    else:
        scorekeeper = ScoreKeeper(mode)
        if oled:
            oled.update(scorekeeper.sport)
    return 'OK'

@socketio.on('update')
def update_score(payload):
    return emit('update', payload, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9876)