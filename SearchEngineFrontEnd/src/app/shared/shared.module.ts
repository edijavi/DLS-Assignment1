import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ToolbarComponent } from './toolbar/toolbar.component';
import {MatButtonModule, MatToolbarModule} from '@angular/material';
import {MatIconModule} from '@angular/material/icon';


@NgModule({
  declarations: [ToolbarComponent],
  imports: [
    CommonModule,
    MatIconModule,
    MatToolbarModule,
    MatButtonModule
  ],
  exports: [ToolbarComponent]
})
export class SharedModule { }
