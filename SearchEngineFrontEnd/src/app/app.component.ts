import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  routes = [
    {route: '/', title: 'Home', icon: 'home'},
    {route: 'searchengine', title: 'Search', icon: 'search'}
    ];
  navBarOpen = true;

  toggleNav() {
    this.navBarOpen = !this.navBarOpen;
  }
}
