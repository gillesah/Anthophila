import { TestBed } from '@angular/core/testing';

import { BeeyardService } from './beeyard.service';

describe('BeeyardService', () => {
  let service: BeeyardService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BeeyardService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
