import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';

@Component({
  selector: 'app-beeyard',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './beeyard.component.html',
  styleUrl: './beeyard.component.scss',
})
export class BeeyardComponent implements OnInit {
  data: any[] = [];
  private httpClient = inject(HttpClient);
  constructor() {}
  ngOnInit(): void {
    this.fetchData();
  }
  private fetchData(): void {
    this.httpClient
      .get('http://localhost:8002/API_PUBLIC/beeyards/')
      .subscribe((data: any) => {
        this.data = data.results;
        console.log(data);
      });
  }
}
