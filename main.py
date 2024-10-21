import sys, datetime, time
from PyQt6.QtWidgets import  *
from plyer import notification

class NotificationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Schedule Notification')
        self.setFixedSize(370, 270)
        
        layout = QFormLayout()
        time_layout = QHBoxLayout()

        self.playertime_label = QLabel('Time:')
        self.divisionsymbol_label = QLabel(':')
        self.playertime_input1 = QLineEdit()
        self.playertime_input1.setFixedSize(20, 25)
        self.playertime_input2 = QLineEdit()
        self.playertime_input2.setFixedSize(20, 25)
        time_layout.addWidget(self.playertime_input1, 0)
        time_layout.addWidget(self.divisionsymbol_label)
        time_layout.addWidget(self.playertime_input2, 0)
        time_layout.addStretch(1)

        layout.addRow(self.playertime_label, time_layout)

        self.title_label = QLabel('Title:')
        self.title_input = QLineEdit()
        self.title_input.setFixedSize(200, 25)
        layout.addRow(self.title_label, self.title_input)

        self.message_label = QLabel('Message:')
        self.message_input = QTextEdit()
        self.message_input.setFixedSize(200, 80)
        layout.addRow(self.message_label, self.message_input)

        submit_btn = QPushButton("Schedule Notification")
        submit_btn.clicked.connect(self.schedule_notification)
        submit_btn.setFixedSize(200, 20)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def schedule_notification(self):
        notification_title = self.title_input.text()
        notification_message = self.message_input.toPlainText()

        hour = int(self.playertime_input1.text())
        minute = int(self.playertime_input2.text())

        self.close()
        while True:
            currentHour = datetime.datetime.now().hour
            currentMinute = datetime.datetime.now().minute
            time.sleep(1)
            if currentHour == hour and currentMinute == minute:
                notification.notify(
                    title= notification_title,  
                    message= notification_message,
                    app_icon= None,
                    timeout= 5,
                    toast= True
                )
                break

app = QApplication(sys.argv)
app.setStyleSheet('QLabel{font-size: 11pt;}')
window = NotificationWindow()
window.show()
sys.exit(app.exec())