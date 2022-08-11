import { Component, OnInit } from '@angular/core';
import { ISubscription } from 'src/app/models/subscription';
import { SubscriptionService } from 'src/app/services/subscriptions.service';

@Component({
  selector: 'app-subscriptions-list-component',
  templateUrl: './subscriptions-list-component.component.html',
  styleUrls: ['./subscriptions-list-component.component.css']
})
export class SubscriptionsListComponentComponent implements OnInit {

  public displayedColumns: string[] = ['id', 'manifest', 'exp_date', 'status'];

  constructor( private subService: SubscriptionService ) { 
    
  }
  public dataSource: ISubscription[] = [];

  ngOnInit(): void {
    this.subService.getSubscriptions().subscribe( data =>{
      console.log(data);
      this.dataSource = data;
    })
  }

}
