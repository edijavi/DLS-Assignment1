import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchComponent } from './search/search.component';
import {SharedModule} from '../shared/shared.module';
import {MatAutocompleteModule} from '@angular/material';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [SearchComponent],
  imports: [
    CommonModule,
    SharedModule,
    MatAutocompleteModule,
    FormsModule
  ],
  exports: [SearchComponent]

})
export class SearchengineModule { }
