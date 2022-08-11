import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from "rxjs";
import { ISubscription } from '../models/subscription';

@Injectable({
    providedIn: 'root',
})
export class SubscriptionService {

    private server: string = "/subscriptions"

    constructor(private http: HttpClient) { 
    }

    getSubscriptions(){
        return this.http.get<ISubscription[]>( this.server );
    }

    postSubscription( sub: ISubscription ){
        return this.http.post<any>( this.server, JSON.stringify(sub) );
    }

}