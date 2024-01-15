import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BeeyardService {
  private apiUrl = 'http://localhost:8000/API_PUBLIC/beeyards/';

  constructor(private http: HttpClient) {}

  getBeeyards(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
