import { Component, OnDestroy } from '@angular/core';
import { WebSocketServiceFAQ } from './websocket.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})

export class AppComponent implements OnDestroy {
  message = '';
  title: string | undefined;

  constructor(public webSocketService: WebSocketServiceFAQ) {
    this.webSocketService.connect();
  }

  sendMessage(message: string) {
    this.webSocketService.connect();
    if (!this.webSocketService.checkState()) alert('Бот спит, давайте пообщаемся с ним чуть позже');
    else this.webSocketService.sendMessage(message);
  }

  ngOnDestroy() {
    this.webSocketService.close();
  }

  scroll_bottom() {
    let el = document.getElementById("history");
    if (el != null) el.scrollTo(0, el.scrollHeight);
  }
}
