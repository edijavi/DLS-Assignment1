import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchComponent } from './search/search.component';
import {SharedModule} from '../shared/shared.module';
import {MatButtonModule, MatIconModule, MatInputModule, MatToolbarModule} from '@angular/material';

@NgModule({
  declarations: [SearchComponent],
  imports: [
    CommonModule,
    SharedModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule
  ],
  exports: [SearchComponent]

})
export class SearchengineModule { }
