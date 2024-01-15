import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BeeyardService } from '../services/beeyard.service';

@Component({
  selector: 'app-beeyard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './beeyard.component.html',
  styleUrls: ['./beeyard.component.scss'],
})
export class BeeyardComponent implements OnInit {
  beeyards: any = [];

  constructor(private beeyardService: BeeyardService) {}
  ngOnInit(): void {
    this.beeyardService.getBeeyards().subscribe((data) => {
      this.beeyards = data;
    });
  }
}
