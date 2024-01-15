import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BeeyardComponent } from './beeyard.component';

describe('BeeyardComponent', () => {
  let component: BeeyardComponent;
  let fixture: ComponentFixture<BeeyardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BeeyardComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BeeyardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
