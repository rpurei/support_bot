import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { environment } from '../environments/environment';

interface MessageData {
  message: string;
  time?: string;
  side: string;
}

@Injectable({
  providedIn: 'root',
})

export class WebSocketServiceFAQ {
  private socket$!: WebSocketSubject<any>;
  public receivedData: MessageData[] = [];

  public connect(): void {
    if (!this.socket$ || this.socket$.closed) {
      this.socket$ = webSocket(environment.webSocketUrlFAQ);
      this.socket$.subscribe((data: MessageData) => {
        this.receivedData.push(data);
      });
    }
  }

  sendMessage(message: string) {
    const formatData = (input: number) => {
      if (input > 9) {
        return input;
      } else return `0${input}`;
    };
    let d = new Date();
    let dformat = [formatData(d.getDate()),
                   formatData(d.getMonth() + 1),
                   formatData(d.getFullYear())].join('.')+' '+
                  [formatData(d.getHours()),
                   formatData(d.getMinutes()),
                   formatData(d.getSeconds())].join(':');
    let msg : MessageData = {message: message, time: dformat, side: 'human'}
    this.receivedData.push(msg);
    this.socket$.next({ message });
  }

  checkState(){
    return !!this.socket$;
  }

  close() {
    this.socket$.complete();
  }
}
