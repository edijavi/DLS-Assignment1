import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ToolbarComponent } from './toolbar/toolbar.component';
import {MatButtonModule, MatToolbarModule} from '@angular/material';
import {MatIconModule} from '@angular/material/icon';
import { MarginIconComponent } from './margin-icon/margin-icon.component';


@NgModule({
  declarations: [ToolbarComponent, MarginIconComponent],
  imports: [
    CommonModule,
    MatIconModule,
    MatToolbarModule,
    MatButtonModule
  ],
  exports: [ToolbarComponent, MarginIconComponent]
})
export class SharedModule { }
