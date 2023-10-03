from flask_socketio import SocketIO
from application import create_app
from application.database import DataBase
import config

# 初始化
app = create_app()
socketio = SocketIO(app)  # 网络通信

# 监听事件
@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)

if __name__ == "__main__":
    # 启动web服务
    socketio.run(app, debug=True, host=str(config.Config.SERVER))
