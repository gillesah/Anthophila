import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommoModule } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true, // Ajoutez le drapeau standalone: true ici
})
export class AppComponent implements OnInit {
  beeyards: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http
      .get<any[]>('http://localhost:8000/API_PUBLIC/beeyards/')
      .subscribe((data) => {
        this.beeyards = data;
      });
  }
}
