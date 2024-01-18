import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  beeyards: any = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getBeeyards().subscribe((data) => {
      this.beeyards = data;
    });
  }
}
