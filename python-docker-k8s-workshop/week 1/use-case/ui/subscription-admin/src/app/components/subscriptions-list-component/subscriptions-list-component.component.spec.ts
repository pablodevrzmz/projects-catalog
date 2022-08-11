import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubscriptionsListComponentComponent } from './subscriptions-list-component.component';

describe('SubscriptionsListComponentComponent', () => {
  let component: SubscriptionsListComponentComponent;
  let fixture: ComponentFixture<SubscriptionsListComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SubscriptionsListComponentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SubscriptionsListComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
